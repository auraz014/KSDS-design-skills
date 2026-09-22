#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  convert_webm_to_webp.sh INPUT.webm --loop N [options]

Required:
  INPUT.webm             Source animated WebM
  --loop N               0=infinite, 1=play once, N=N total plays

Options:
  --output FILE.webp     Default: INPUT stem with .webp
  --quality N            Lossy WebP quality, 0-100 (default: 85)
  --preset NAME          default|picture|photo|drawing|icon|text
                         (default: default)
  --overwrite            Replace an existing output
  -h, --help             Show this help
EOF
}

die() {
  printf 'Error: %s\n' "$*" >&2
  exit 2
}

input=""
output=""
loop=""
quality="85"
preset="default"
overwrite="0"

while (($#)); do
  case "$1" in
    --loop)
      (($# >= 2)) || die "--loop requires a value"
      loop="$2"
      shift 2
      ;;
    --output)
      (($# >= 2)) || die "--output requires a path"
      output="$2"
      shift 2
      ;;
    --quality)
      (($# >= 2)) || die "--quality requires a value"
      quality="$2"
      shift 2
      ;;
    --preset)
      (($# >= 2)) || die "--preset requires a value"
      preset="$2"
      shift 2
      ;;
    --overwrite)
      overwrite="1"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    -*)
      die "unknown option: $1"
      ;;
    *)
      [[ -z "$input" ]] || die "only one input file is supported per run"
      input="$1"
      shift
      ;;
  esac
done

[[ -n "$input" ]] || die "missing INPUT.webm"
[[ -n "$loop" ]] || die "missing --loop; expected 0=infinite, 1=play once, N=N total plays"
[[ -f "$input" ]] || die "input file does not exist: $input"
case "$input" in
  *.[Ww][Ee][Bb][Mm]) ;;
  *) die "input must use the .webm extension" ;;
esac
[[ "$loop" =~ ^[0-9]+$ ]] || die "--loop must be an integer from 0 to 65535"
awk -v n="$loop" 'BEGIN { exit !(n >= 0 && n <= 65535) }' ||
  die "--loop must be no greater than 65535"
[[ "$quality" =~ ^[0-9]+([.][0-9]+)?$ ]] ||
  die "--quality must be a number from 0 to 100"
awk -v q="$quality" 'BEGIN { exit !(q >= 0 && q <= 100) }' ||
  die "--quality must be a number from 0 to 100"

case "$preset" in
  default|picture|photo|drawing|icon|text) ;;
  *) die "unsupported preset: $preset" ;;
esac

for command_name in ffmpeg ffprobe webpmux; do
  command -v "$command_name" >/dev/null ||
    die "required command is missing: $command_name"
done

if [[ -z "$output" ]]; then
  output="${input%.*}.webp"
fi
case "$output" in
  *.[Ww][Ee][Bb][Pp]) ;;
  *) die "output must use the .webp extension" ;;
esac
[[ -d "$(dirname "$output")" ]] ||
  die "output directory does not exist: $(dirname "$output")"
if [[ -e "$output" && "$overwrite" != "1" ]]; then
  die "output already exists; choose an unused path or use --overwrite when replacement is authorized: $output"
fi

codec="$(
  ffprobe -v error -select_streams v:0 \
    -show_entries stream=codec_name -of default=nw=1:nk=1 "$input"
)"
source_dimensions="$(
  ffprobe -v error -select_streams v:0 \
    -show_entries stream=width,height -of csv=p=0:s=x "$input"
)"
source_duration="$(
  ffprobe -v error -show_entries format=duration \
    -of default=nw=1:nk=1 "$input"
)"
alpha_mode="$(
  ffprobe -v error -select_streams v:0 \
    -show_entries stream_tags=alpha_mode -of default=nw=1:nk=1 "$input" ||
    true
)"

decoder_args=()
if [[ "$codec" == "vp9" ]]; then
  decoder_args=(-c:v libvpx-vp9)
fi

temp_dir="$(mktemp -d "${TMPDIR:-/tmp}/webm-to-webp.XXXXXX")"
trap 'rm -rf "$temp_dir"' EXIT
encoded="$temp_dir/encoded.webp"
verified="$temp_dir/verified.webp"

ffmpeg -hide_banner -loglevel error -y \
  "${decoder_args[@]}" -i "$input" -an \
  -c:v libwebp_anim -lossless 0 -preset "$preset" \
  -quality "$quality" -compression_level 6 -pix_fmt yuva420p \
  -loop "$loop" "$encoded"

webpmux -set loop "$loop" "$encoded" -o "$verified" >/dev/null
info="$(webpmux -info "$verified")"

actual_loop="$(
  awk '/Loop Count/ {
    for (i = 1; i <= NF; i++) if ($i == "Count") {
      value = $(i + 2)
      gsub(/[^0-9]/, "", value)
      print value
      exit
    }
  }' <<<"$info"
)"
[[ "$actual_loop" == "$loop" ]] ||
  die "loop verification failed: expected $loop, got ${actual_loop:-unknown}"

output_dimensions="$(
  awk '/Canvas size:/ { print $3 "x" $5; exit }' <<<"$info"
)"
[[ "$output_dimensions" == "$source_dimensions" ]] ||
  die "dimension verification failed: source=$source_dimensions output=$output_dimensions"

if [[ "$alpha_mode" == "1" ]] &&
  ! grep -q "transparency" <<<"$info"; then
  die "alpha verification failed: source declares alpha but output does not"
fi

output_duration_ms="$(
  awk '/^[[:space:]]*[0-9]+:/ { total += $7 }
       END { printf "%.0f", total }' <<<"$info"
)"
if [[ "$source_duration" != "N/A" && -n "$source_duration" ]]; then
  duration_ok="$(
    awk -v source_seconds="$source_duration" -v output_ms="$output_duration_ms" \
      'BEGIN {
        delta = source_seconds * 1000 - output_ms
        if (delta < 0) delta = -delta
        print (delta <= 100 ? "yes" : "no")
      }'
  )"
  [[ "$duration_ok" == "yes" ]] ||
    die "duration verification failed: source=${source_duration}s output=${output_duration_ms}ms"
fi

cp "$verified" "$output"

source_bytes="$(wc -c <"$input" | tr -d ' ')"
output_bytes="$(wc -c <"$output" | tr -d ' ')"
size_change="$(
  awk -v before="$source_bytes" -v after="$output_bytes" \
    'BEGIN {
      if (after <= before) {
        printf "reduction %.1f", (1 - after / before) * 100
      } else {
        printf "increase %.1f", (after / before - 1) * 100
      }
    }'
)"
transparent="no"
grep -q "transparency" <<<"$info" && transparent="yes"
frame_count="$(
  awk '/Number of frames:/ { print $4; exit }' <<<"$info"
)"

printf 'Created: %s\n' "$output"
printf 'Codec: WebP animation\n'
printf 'Canvas: %s\n' "$output_dimensions"
printf 'Duration: %sms\n' "$output_duration_ms"
printf 'Frames: %s\n' "${frame_count:-unknown}"
printf 'Transparency: %s\n' "$transparent"
printf 'Loop count: %s\n' "$actual_loop"
printf 'Quality: %s (%s preset)\n' "$quality" "$preset"
printf 'Size: %s -> %s bytes (%s%% vs WebM)\n' \
  "$source_bytes" "$output_bytes" "$size_change"
