# Data and output contracts

## Contents

1. Style Profile
2. Design Brief
3. Character Proposal
4. User-facing response
5. Publication readiness

## 1. Style Profile

The native schema below applies to new profiles drafted by this skill. A user-supplied registered profile may retain its own schema unchanged. In that case, `assets/style-profiles/registry.json` is the adapter: it identifies the structured rule authority, the paired Style Bible, activation status, and read-only policy. Never convert a registered read-only profile merely to fit the native schema.

Required top-level fields:

```json
{
  "schema_version": "1.0",
  "style_id": "lowercase-hyphen-id",
  "name": "Human-facing name",
  "category": "Navigation category only",
  "version": "0.1.0",
  "status": "draft",
  "source_summary": {
    "reference_count": 0,
    "analysis_date": null,
    "notes": ""
  },
  "rules": {
    "visual_language": [],
    "shape": [],
    "proportion": [],
    "silhouette": [],
    "face_expression": [],
    "color": [],
    "material_rendering": [],
    "detail": [],
    "commercial_application": [],
    "avoid": []
  },
  "prompt_template": {
    "required_slots": [],
    "ordering": [],
    "negative_constraints": []
  }
}
```

A native child profile may additionally declare `parent_style_id` and `inheritance`. The registry must declare its `parent_style_key`. Apply the parent for shared commercial and quality principles, and give the child precedence only for the scopes explicitly named in its inheritance block.

Each item in a rule array uses:

```json
{
  "id": "shape-01",
  "statement": "Observable, actionable rule",
  "strength": "dominant",
  "evidence": "Observed in 24 of 30 references",
  "confidence": 0.86
}
```

Allowed strengths: `dominant`, `supporting`, `optional`, `avoid`.

Use observable statements. Avoid vague entries such as “高级”“潮流” unless the profile also defines the visible properties that produce that effect.

## 2. Design Brief

```json
{
  "purpose": "",
  "brand_or_product": "",
  "brand_attributes": [],
  "audience": [],
  "personality": [],
  "use_cases": [],
  "must_include": [],
  "must_avoid": [],
  "user_facts": [],
  "assumptions": [],
  "open_questions": []
}
```

Never mix assumptions into `user_facts`.

For a vague request, ask one combined open question about brand/product positioning, desired impression and any existing brand cue the user hopes to integrate. The same message must explicitly offer the user the option to answer `自由发挥`; this sentence is mandatory even when the rest of the question is adapted. Do not proactively ask for prohibited elements, personality or audience. If the user volunteers a restriction, preserve it in `must_avoid`. If the user delegates with `自由发挥／随意发挥／都可以／没有特别设定／你来决定`, record that delegation in `user_facts`, record professional creative decisions in `assumptions`, and proceed directly. Leave production use cases unresolved until application and extension work.

Internal assumptions must result from design analysis of the likely brand/product context, emotional role, audience appeal, recognizability and commercial extensibility. Do not expose this internal analysis unless requested, and do not use arbitrary variation as a substitute for professional judgment.

## 3. Character Proposal

Each proposal contains:

```json
{
  "working_name": "",
  "archetype": "",
  "creative_seed": "",
  "character_truth": "",
  "role_positioning": "",
  "personality": [],
  "story": "",
  "recognition_cues": [],
  "appearance": {
    "structure": "",
    "proportion": "",
    "limb_treatment": "",
    "pose": "",
    "facial_signature": {
      "eye_family_id": "",
      "eye_scale_spacing": "",
      "facial_zone_id": "",
      "brow_eye_relation": "",
      "nose_muzzle_id": "",
      "mouth_family_id": "",
      "expression": "",
      "signature_key": ""
    },
    "focal_signature": {
      "focal_type": "",
      "orientation": "",
      "internal_state": "",
      "deformation": "",
      "motion": "",
      "signature_key": ""
    },
    "color": "",
    "palette_rationale": "",
    "material": "",
    "signature_feature": "",
    "accessory": "",
    "accessory_rationale": ""
  },
  "memory_hook": "",
  "design_rationale": [
    {
      "decision": "",
      "brief_basis": "",
      "style_rule_ids": []
    }
  ],
  "applications": [],
  "positive_prompt": "",
  "negative_constraints": []
}
```

Use `facial_signature` for a conventional face. Under the AI digital-life child profile only, a low-frequency single-lens or nonstandard state-window facial direction may leave `facial_signature` empty and use `focal_signature` instead. Completely faceless, light-core-only and ambient-mass characters are not allowed; their references inform material only. Exactly one signature mode must be complete. A focal-signature direction is not written to facial usage history and does not affect the 65:35 eye-system tendency.

### Facial usage history

`state/facial-usage-history.json` is mutable runtime state, not a visual-style authority. Keep only the newest eight accepted characters. Use it to adjust selection preference, never as a hard prohibition against a face that genuinely fits the concept.

Each entry uses:

```json
{
  "accepted_at": "ISO-8601 timestamp",
  "batch_id": "",
  "archetype": "",
  "eye_system": "no_sclera | graphic_sclera",
  "eye_family_id": "",
  "eye_scale_spacing": "",
  "facial_zone_id": "",
  "brow_eye_relation": "",
  "nose_muzzle_id": "",
  "mouth_family_id": "",
  "expression": "",
  "signature_key": ""
}
```

Build `signature_key` from the seven facial-signature fields in a stable order. Record only images that pass visual inspection. Never record rejected or abandoned generations.

## 4. User-facing response

Use this order before rendering:

1. **方案 A** — `角色原型` only when not already supplied; then `性格`、`特征`、`外形`、`五官`、`色彩`; add `质感` only when concept-defining.
2. **方案 B** — the same conditional structure.
3. **方案 C** — the same conditional structure.
4. One short instruction inviting the user to select, combine or modify.

Default to three text directions unless the user requests another count. Letter labels are display labels only and do not imply a hierarchy. Keep every field concise, concrete and visual. For `性格`, show exactly three comma-separated adjectives or very short phrases by default, never a sentence, personality joke or extended explanation. For `五官`, show one compact phrase with only two or three visible cues; keep pupil construction, spacing and other generation-level facial details internal unless they define the concept. Do not expose prompts, negative constraints, canonical facial IDs, the batch matrix, internal assumptions or style traces.

Do not precede the proposals with an explanation of how they were diversified. Never mention recent-history checks, eye IDs, scripts, profile fields, fixed structure assignments, avoided templates or prompt fallback controls. The proposals should feel authored from three complete character ideas rather than assembled from a visible component matrix.

After the user clearly selects, combines or modifies a direction:

1. compile the selected direction's generation prompt internally;
2. if a progress acknowledgment is needed, use one short designer-facing sentence without technical details;
3. generate immediately without another confirmation;
4. return the finished image with only a short identifying caption when useful;
5. do not display prompts or internal mechanics unless explicitly requested.

Image-count contract:

- text proposal stage: three directions by default;
- selected or combined direction: one image by default;
- full visual comparison set: three images only when explicitly requested;
- another count: only when explicitly requested;
- never default to five images.

## 5. Publication readiness

A profile can be `published` only when:

- `reference_count` is greater than zero;
- every rule category contains reviewed content or is explicitly marked not applicable in `source_summary.notes`;
- every rule has a unique ID, evidence, and confidence;
- `required_slots` and `ordering` are non-empty;
- no prompt instruction contains a protected character name, brand-copy request, or named living artist;
- a human reviewer has confirmed the profile. Record this in `source_summary.notes`.
