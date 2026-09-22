# Workflows

## Contents

1. Generate concepts
2. Extend an IP
3. Draft a Style Profile from images
4. Review a proposal
5. Difference check
6. Prompt assembly

## 1. Generate concepts

### A. Resolve the style

Read `assets/style-profiles/registry.json` from the skill root first. Resolve the user's category or style name to a registry key.

For an `active` registered style:

1. Validate the entry with `scripts/validate_style_assets.py`.
2. Load `profile_path` as the exact structured rule authority.
3. Load `style_bible_path` as the method, interpretation, and explanation authority.
4. Do not rewrite or normalize either asset.

For a native profile that is not registered, use `scripts/validate_style_profile.py`. If only a draft exists, explain that the style has not been validated. Ask whether to use it for exploration or wait for publication.

### A1. Keep the working process private

The style registry, validation commands, history ledger, canonical facial IDs, frequency calculations, contrast matrix, prompt assembly and regeneration logic are internal implementation details.

Do not narrate them before or during ordinary concept generation. In particular, never show user-facing statements such as:

- which recent eye IDs are being avoided;
- which previous structure templates will not be repeated;
- which body type, pose or facial grammar has been assigned to each proposal;
- that a script, JSON profile, history file or negative-prompt rule is being used.

The normal visible experience contains only:

1. the one lightweight brand-relationship question when needed;
2. three concise, natural-language character proposals;
3. one short acknowledgment after the user chooses;
4. the generated image and a concise caption.

If a progress message is operationally required, say only that the selected direction is being refined and generated. Do not expose the recipe behind it. Explain internal mechanics only after an explicit technical request.

### B. Build the brief

Extract:

- brand/product context;
- audience;
- personality;
- desired brand cues, plus any constraints the user volunteers;

Analyze the brief as a professional IP designer. Infer the likely emotional role, audience attraction, brand fit, recognition strategy and extension potential. Keep these judgments internal and express them through the proposed archetype and five visual fields.

Do not ask about personality or audience before the first concept round. If brand positioning and desired brand cues are both missing, use the single lightweight question defined below.

Collect purpose, use cases and production needs later, when the user asks for applications, expressions, merchandise, animation or other extensions.

### B1. Minimal-request handling

Treat a request as vague when it mainly specifies a subject or species, such as “我要一个小羊 IP”, while leaving personality, audience and brand relationship undefined.

For a vague request, ask one concise open question covering:

1. the character's relationship to a brand or product;
2. the impression or style the brand hopes to convey;
3. any existing brand cue the user would like naturally integrated.

Recommended reference phrasing:

> 为了让角色更准确地承接品牌气质，想先了解一下：这个[用户指定的角色原型]与什么品牌或产品相关？希望它传达怎样的感觉，或者有没有现成的品牌线索想自然融入？如果暂时没有特别设定，也可以直接说“自由发挥”，我会根据角色特点给出三个方向。

Adapt the opening naturally to the brand, character, conversation tone and information already supplied. Do not repeat it mechanically, ask for information the user already gave, or display the placeholder. However, every adapted version must end with an explicit sentence offering the user the option to say `自由发挥`; never imply this option silently or omit it for brevity. A valid natural alternative is: `它主要代表怎样的品牌？有没有现成的品牌线索，希望我自然融入角色里？如果暂时没有特别设定，也可以直接说“自由发挥”，我会根据角色特点给出三个方向。` Do not proactively ask for avoided elements; if the user volunteers a restriction, record and honor it.

Do not turn this into a questionnaire. Do not ask follow-up questions about personality or audience. If the user says `随意发挥／都可以／没有特别设定／你来决定`, or explicitly asks not to be questioned, record the delegation and proceed directly. If the original request already supplies brand positioning and desired brand cues, skip the question.

Infer temperament, emotional energy and audience appeal through professional design judgment. Use the three internal proposals to express distinct plausible interpretations without exposing a separate assumptions report.

Treat material as a conditional design field. Show `质感` only when the concept or active substyle depends on a distinctive material system. AI digital life, glass, jelly, plush, ceramic and metal-led themes usually qualify. For an ordinary mascot, keep material inside the generation prompt and apply the active profile's default rendering without displaying a separate field.

Do not ask about initial use cases. Proceed to three concise text directions, then let the user select, combine or modify one before rendering.

### C. Develop independent concepts

Start each direction from a blank slate. Do not use the previous direction as a base.

Do not assign proposal numbers while developing concepts. For each request, vary the creative entry point according to the brief: a concept may begin from personality, species behavior, silhouette, gesture, brand metaphor, material behavior or negative space. These are possibilities, not mandatory lanes or a coverage checklist.

For each direction, independently create:

- a one-sentence character truth;
- one visual or behavioral memory hook;
- an emotional energy;
- a body-and-action relationship that expresses the character;
- a color or material attitude;
- optionally, in any round, one simple character-driven accessory, garment, prop or context clue when identity, behavior, brand or scene naturally supports it.

Do not assign baseline, refinement, moderate or experimental roles. Do not force the set to cover specific component categories.

Do not reuse a stable mapping such as “first = round fused body, second = separate head and torso, third = seated or unusual.” High-frequency profile options are weighted tendencies across multiple requests, not guaranteed members or leading positions in every set.

Keep attributes decoupled. A body structure must not repeatedly inherit the same expression, limb solution, pose or degree of cuteness merely because that combination worked before. If recent generations are present in the conversation, compare against their ordering and reroll any repeated proposal-number-to-design mapping.

For an animal origin, use Style-Bible-first stable recognition unless the user has explicitly requested or approved stronger morphological abstraction. Retain two or three strong mutually supporting cues, but rebuild the character as a simple toy-like whole with hidden, compact, integrated or graphically extended limbs. Species recognition should come from ears, nose/muzzle, head-face relation, tail, coat block, posture or another selected cue—not from reproducing a realistic chest, abdomen, joint system, paw anatomy or natural quadruped stance. Reject both extremes: an unknown blob or other species, and a realistic pet model merely rendered as a toy.

For first-round animals, use a familiar attractive toy-like species base and vary it moderately. Build each proposal around one clear memory hook drawn from the ear/head relationship, proportion, pose, facial attitude, color or material. Do not pursue extreme abstraction merely to make the set different, but do not remove so much variation that all three become generic plush templates.

Keep first-round animal recognition stable but leave color open. Natural, transformed-natural, brand-led and concept-led nonliteral colors are all valid when the dominant color can be justified by the brand, personality, character concept, scene or material. Vary value, temperature, saturation, material and large color-block relationships. Add a supporting or accent color only when it can be justified by the brand, character concept, function, material transition or structural readability.

Do not invent a nonliteral color or decorative accent merely to make a proposal feel more designed or different. High-saturation and nonliteral palettes still require few colors, large clean blocks and clear hierarchy. Morphological abstract-mode opt-in is independent from color; species recognition must survive without relying on color alone.

Run `scripts/manage_facial_history.py summary` before assigning faces. Use its eye and nose-mouth frequency summaries as soft context. Apply the active profile's 65:35 no-sclera-to-graphic-sclera target across the rolling newest-eight window and the planned conventional-face directions. Treat it as a soft preference, not a quota. Do not force every three-image set into a fixed 2:1 split; 3:0, 2:1 and 1:2 may all occur among eyed characters. Every eye and pupil must remain flat and matte with no catchlight, white reflection dot, glossy highlight or glass-eye effect.

Create a signature table for the whole set. For every conventional-face direction, use canonical IDs from the active profile and record eye family ID, scale/spacing, facial-zone ID, brow-eye relation, nose/muzzle ID, mouth-family ID and primary expression. Under the AI digital-life child profile only, a low-frequency single-lens or nonstandard state-window facial direction may instead record focal type, orientation, internal state, deformation and motion. Do not create a faceless, light-core-only or ambient-mass character; use those references only for material behavior. Exactly one signature mode must be complete for each direction.

Among conventional-face directions in the default three-direction set, `NS01`, `NS02` and `GS01` together may appear in at most one proposal. `M01` and `M06` together may appear in at most one proposal. Do not repeat an exact nose-mouth pair. Treat `NM03+M04` and `NM05+M04` as one perceptually equivalent rounded-nose-plus-symmetric-W-mouth group and use that group at most once. All conventional eye IDs and complete facial signatures must differ, and every pair of conventional faces must differ in at least three signature dimensions. A gaze shift, brow-angle change, reversed mouth corner or recolor is not a new signature. Focal-signature directions must differ through focal type, state behavior and silhouette, not merely color.

Use the newest eight ledger entries only to adjust preference. Deprioritize an exact signature, a recently frequent eye ID or a recently frequent nose-mouth pair when equally suitable alternatives exist, but allow reuse whenever the species, brand or character truth makes that face the strongest choice. Never manufacture variety through malformed alignment, random asymmetry or incompatible symbols.

Keep the underlying character complete without relying on clothing. In any round, a direction may use one simple accessory or garment derived from role, personality, behavior, brand or scene. Use at most one primary item and one very weak functional detail. Preserve the face or focal system, species cues and icon silhouette; use the existing palette unless a new color has an explicit reason. Do not turn every direction into a dressed character and do not treat an accessory swap as a complete new concept.

Apply only the exact active Style Profile and its paired Style Bible. Do not add a hardcoded design envelope in the workflow. Let overall proportion, silhouette, facial construction, limb treatment, color, material and memory hook be decided within those active assets.

Natural similarities may occur. Reject a direction only when it repeats another direction's overall body-expression-pose template or feels like a recolor/accessory swap. Seek moderate difference through personality, facial or focal attitude, ear/head relationship, pose, proportion, palette or material before stronger structural transformation.

Keep all directions inside the selected Style Profile's aesthetic judgment: youthful, emotionally direct, playful, clean, memorable and commercially extensible.

### D. Present directions, then render

After internal proposals pass the difference check, build a batch contrast matrix with one row per direction:

- character truth and creative seed;
- archetype and recognition cues;
- body structure, limb treatment and pose;
- complete facial signature with canonical IDs, or one complete focal signature when the AI digital-life exception applies;
- palette and its rationale;
- one primary memory hook;
- optional accessory and its rationale.

Present three concise text directions in lettered order. Each direction contains only:

- `角色原型` only when the user did not already specify one;
- `性格`;
- `特征`;
- `外形`;
- `五官`;
- `色彩`;
- `质感` only when material defines the concept or active substyle.

Keep every field to one concise phrase or short sentence:

- `性格`: use exactly three concise comma-separated descriptors by default, such as `聪明、安静、反应灵敏`, `温柔、可靠、有陪伴感` or `好奇、活泼、略带机灵感`. Each item may be an adjective or a very short phrase. Do not turn it into a sentence, personality joke, metaphor, audience description or style-positioning explanation.
- `五官`: use one compact phrase containing only two or three immediately visible cues, such as `细长白眼、短平嘴` or `眯眼、小圆嘴`. For a low-frequency AI digital-life focal-signature direction, use an equally compact description such as `单镜头焦点，随状态转向`. Never propose `无传统五官` or a light-core-only face. Mention the overall expression only when it is not already obvious. Do not display pupil construction, feature spacing, canonical IDs or generation-level geometry unless one of them is the concept's defining memory hook.
- `特征` may describe the main memory hook, accessory, gesture or local detail.
- `外形` should combine body structure, posture and proportion in natural language.

Keep the full canonical facial signature or complete AI digital-life focal signature internally for image generation even when the user-facing `五官` line is shortened. Do not expose canonical IDs, the batch matrix, prompts, negative constraints, internal assumptions or style traces. Shuffle completed proposals before assigning A/B/C so letters carry no recurring morphology role.

Ask the user to select A/B/C, combine elements or state a modification. A clear response counts as final authorization. Compile the selected or combined direction's positive prompt only after that response. Name only its chosen facial or focal construction; never include a menu of unused alternatives.

Add direction-specific negative constraints blocking likely fallback families. For example, when a proposal uses `NS08`, block generic dot, oval and capsule eyes if they are not part of that design. Keep shared profile negatives separate.

Before the first image call, compile the entire requested set and verify:

- the requested output count;
- distinct complete facial or focal signatures;
- no repeated or perceptually equivalent nose-mouth pair among conventional-face directions;
- distinct character ideas and silhouettes;
- direction-specific fallback blocks.

Generate immediately without showing the prompt or asking for confirmation again. Generate one image by default. If the user explicitly requests `N` directions, make exactly `N` planned image-generation calls. Do not add a replacement because of a duplicate or inconsistency that should have been caught during preflight. Regenerate only for a genuine rendering artifact; when that exception is necessary, clearly mark the earlier image as discarded so the final set remains unambiguous.

After accepted images pass the visual quality gate, run `scripts/manage_facial_history.py append` once per accepted rendered conventional-face character using one shared batch ID. Do not append low-frequency single-lens or state-window focal-signature directions. Text-only proposals are never added to the ledger. The script keeps only the newest eight.

After delivering a Style-Bible-first stable-recognition animal result, ask whether the user wants to see a more morphologically abstract exploratory direction. This is a post-delivery option, not a gate before the initial result.

### E. Visual quality gate

Inspect each generated image before accepting it:

- facial expression or nonfacial state behavior reads as intentional;
- each proposal preserves its planned complete facial or focal signature;
- gaze, feature placement, focal orientation and asymmetry support the concept;
- limb count, connection and pose are coherent;
- no accidental melting, duplication or anatomical artifacts are present.
- the result remains within the exact active profile and Style Bible.
- an animal-origin first-round result is immediately recognizable without its caption, has a familiar attractive toy-like base and one clear restrained memory hook, and reads as neither a generic template nor an overly abstract object;
- the rolling newest-eight eye-system tendency is considered across conventional-face directions without overriding character fit, and no eye contains catchlights, white reflection dots, glossy highlights or glass-eye rendering.
- conventional faces draw from meaningfully different observed construction families rather than one repeated eye mold with cosmetic changes.
- nose-mouth designs do not collapse into the same rounded dark nose connected to a symmetric W-shaped mouth with only thickness or material changed.
- at reduced size, no two conventional-face proposals read as the same generic face with only ears, color, gaze or expression changed.
- if planned signatures collapse into the same dot-eye, oval-eye, capsule-eye or short-line-mouth result, regenerate those directions.

Preserve intentional character decisions supported by the active assets. Reject accidental gaze conflict, feature drift, any completely faceless character output, malformed anatomy, weak brief fit and unsupported visual drift. Regenerate the failed direction rather than explaining an artifact as creativity. Do not append a conventional facial signature to history until the rendered character passes all gates; never append a focal signature.

## 2. Extend an IP

Trigger this mode when the user says `帮我延展`, asks for an expression/action system, or requests a character extension board.

### A. Resolve and lock the character

- Use the clearly selected image from the current conversation.
- Ask for a source only when more than one candidate is genuinely ambiguous or no image is available.
- Lock dominant silhouette, proportions, head/ear geometry, facial grammar, palette, material, signature feature and rendering style.
- Do not convert the character into a new body type while creating actions.

### B. Default content

Without further questions, create one complete sheet containing:

- one enlarged hero rendering of the selected IP;
- exactly six smaller expression/action extensions;
- a landscape canvas with the hero on one side and the six extensions on the other;
- a large English display title in the left half, plus concise microcopy without numbered labels.

The six extensions must include both facial and physical change. Build a coherent set from emotions such as delight, curiosity, surprise, mild grumpiness, calm/sleepiness or confidence, and actions such as bouncing, leaning, waving, stretching, crouching or turning. These are a pool, not a fixed sequence.

Preserve the active eye rules across all variants. Expression may change the eye construction only when it still reads as the same character family. Never add catchlights or glossy eye effects.

### C. Art direction and typography

Work with a young contemporary Korean graphic-design sensibility:

- youthful, fashionable and clean;
- strong hierarchy between hero, variants and typography;
- a disciplined column-and-row grid with shared alignment axes;
- especially generous safe margins on all four sides, with no title or character close to an edge;
- comfortable gutters and internal breathing room;
- one confident large English display title, supported by concise custom grotesk or rounded microtypography;
- limited palette derived from the character;
- only a few purposeful typographic or geometric marks;
- no crowding, random placement, decorative clutter, gradients or stickers.

Use user-provided names and copy exactly. If none exists, use one neutral English phrase such as `MOOD SET`, `CHARACTER DESIGN` or `EXPRESSIONS` as the large display title, with at most one small supporting phrase. Place the display title in the left half and align it with the hero field. Do not number the variants. Keep supporting text sparse and verify spelling.

### D. Multiple layout options

When the user asks for multiple options, keep the same locked character and six-extension requirement, but vary the board system:

- preferred: left display title plus left hero, with a right 2-by-3 expression grid;
- right hero plus left modular expression grid;
- unequal landscape columns with one spacious hero field and one compact but uncrowded extension field.

Do not map option order to conservative or experimental roles. Each must remain clean and commercially usable.

### E. Extension quality gate

Reject and regenerate when:

- any small character no longer matches the hero;
- ear, tail, face, color, material or main proportions drift;
- fewer or more than six variants appear;
- all six variants are nearly identical;
- text is garbled or excessive;
- typography competes with the IP;
- the board becomes a collage without hierarchy;
- the canvas is not landscape;
- variants are numbered;
- elements ignore shared grid axes, gutters or margins;
- any title or character sits too close to a canvas edge;
- the layout feels crowded, scattered or arbitrarily overlapped;
- eye highlights or malformed anatomy appear.

## 3. Draft a Style Profile from images

### A. Prepare the set

- Accept an image folder or extracted archive.
- Count readable images and note duplicates.
- Create a contact sheet when useful.
- Identify obvious outliers and ask whether to exclude them when exclusion could change the result.

### B. Observe in passes

Pass 1 — inventory:

- subjects and archetypes;
- 2D/3D presentation;
- views, poses, and intended applications.

Pass 2 — formal properties:

- outer silhouette;
- primary geometry;
- relative proportions;
- facial construction;
- palette relationships;
- material and rendering;
- detail density.

Pass 3 — behavioral and commercial properties:

- emotional range;
- signature features;
- small-size legibility;
- plush/figure/animation feasibility;
- repeated avoidances.

### C. Aggregate

For every proposed rule:

- state what is visible;
- estimate how often it appears;
- record exceptions;
- assign confidence;
- classify it as dominant, supporting, optional, or avoid.

Do not treat a one-image feature as a category rule unless the user explicitly selects it.

### D. Human review

Present:

- dominant findings;
- meaningful variations;
- conflicting evidence;
- outliers;
- uncertain items.

Keep the profile in `draft` until the user confirms it.

## 4. Review a proposal

Use a 1–10 score only when the user requests scoring. Otherwise prioritize diagnosis.

Check:

1. Does the proposal answer the Design Brief?
2. Which Style Profile rules are followed, missed, or contradicted?
3. Is the memory hook visible and describable in one phrase?
4. Will the character remain legible in its primary use case?
5. Can the form extend to expressions, poses, merchandise, or motion?
6. Is it too close to a known character or dependent on a generic cliché?

For each problem, prescribe a specific design change and name the affected field.

## 5. Difference check

Compare the completed concepts holistically:

- Does each have its own one-sentence character truth?
- Does each have a memorable visual or behavioral idea?
- Do any two repeat the same body-expression-pose template?
- Is similarity conceptually meaningful or merely a generation default?
- Does every direction still express the active Style Profile's aesthetic judgment?
- Does the set repeat a proposal-number-to-structure or structure-to-expression mapping used in recent outputs?
- If the origin is an animal, is it immediately recognizable from two or three strong cues while still using Style Bible toy-like masses rather than realistic anatomy?
- Can every supporting or accent color be explained by brand, concept, function, material or structural clarity?
- Does every first-round animal palette—natural or nonliteral—have a clear brand, personality, concept, scene or material rationale while species recognition remains independent from color?
- Has the newest-eight history been considered as a soft 65:35 tendency across conventional-face directions without forcing the current batch, and are all eyes free of highlights and reflection dots?
- Do the conventional faces use distinct reference-observed construction families and complete signatures rather than repeating one eye mold with different gaze or brows?
- Do any two conventional-face proposals reuse the same nose-mouth pair or the same perceptual rounded-nose-plus-symmetric-W-mouth grammar?
- Does each conventional-face proposal differ from every other conventional-face proposal in at least three facial-signature dimensions?
- If an AI digital-life direction uses a low-frequency focal signature, does it still read as a face through a single lens or state windows, rather than becoming a faceless material blob?
- When two face choices are equally suitable, has the less recently used eye and nose-mouth combination been preferred, while still allowing a recent face when it clearly fits better?
- At reduced size, do conventional faces remain visibly different before considering ears, color or accessories?
- For an accessorized direction, is there only one primary item, does it have a character or brand rationale, and do the underlying character and species remain clear without it?

Do not require numerical coverage of shape, limb, color, material or pose categories. Facial-ID uniqueness and high-frequency caps among conventional-face directions are explicit quality controls; the rolling eye-system history is advisory. Focal-signature directions are optional and never a required coverage slot. If two results are cosmetically different but conceptually the same, regenerate one complete direction. If two are naturally related yet independently convincing, keep both. Reject any result that contradicts the active assets.

## 6. Prompt assembly

Prefer a natural-language creative brief assembled from the selected structured proposal:

1. character identity, role and audience;
2. one clear concept and memory hook;
3. appearance decisions supported by the active profile;
4. exactly one selected eye ID, facial-zone ID, nose/muzzle ID, mouth ID and intended expression; or, for the AI digital-life exception, one precise focal type, orientation, internal state, deformation and motion behavior;
5. optional simple accessory or garment only when allowed by round and concept;
6. pose and presentation;
7. application intent;
8. exact active-profile constraints and negative rules.

Do not paste option menus into a positive prompt. Translate canonical IDs into one precise natural-language construction and omit all unused alternatives.

For a standalone character render, always make the presentation instruction explicit: a clean near-white neutral-gray studio background, approximately `#F7F8F8` in visual lightness, low saturation, neutral color temperature and only a barely visible neutral contact shadow. It should read as white at first glance rather than visibly gray. If a white or very pale character would lose separation, deepen the near-white neutral gray only slightly instead of introducing warmth or a medium-gray field. Use another background only when the user explicitly requests a brand scene, another color or transparency.

Keep `negative_constraints` separate. Add direction-specific fallback blocks for overselected eye or mouth families when relevant. For every default neutral-background render, block cream, beige, ivory, warm-yellow, sepia, dirty off-white, muddy gray, visibly medium or dark gray and warm background color casts. Do not add unsupported quality clichés such as “award-winning” or “trending.”

Before accepting the image, inspect the background independently from the character palette. Reject and regenerate when the intended near-white neutral gray appears yellowed, creamy, beige, muddy, visibly warm-tinted or noticeably darker than an off-white studio ground.
