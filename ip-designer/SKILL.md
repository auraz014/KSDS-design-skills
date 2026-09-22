---
name: ip-designer
description: Create structured, commercially usable IP character concepts, including the registered AI-era digital-life substyle for AI assistants, agents and smart hardware; ask at most one lightweight question about brand positioning and brand cues for a minimal request, present three concise text directions, then render the user's selected, combined or modified direction immediately without exposing prompts or asking again; and extend a selected character into a professionally art-directed expression-and-action board. Use when ChatGPT or Codex needs to turn either a detailed brand request or a vague prompt such as “我要一个小羊 IP” into mascot concepts, design a warm non-mechanical AI companion, respond to “帮我延展” with a default hero-plus-six-variants sheet, review an existing proposal, or draft a Style Profile from a coherent batch of reference images. Do not use it to imitate a named artist or copy an existing protected character.
---

# 品牌IP设计师

Treat the registered Style Profile as the only source of visual-style rules. Use its paired Style Bible for design method, interpretation, and user-facing explanations. Never infer visual rules from the category name or silently fill empty fields.

The registry currently exposes one top-level family, `brand-mascot`, and its child substyle, `brand-mascot-ai-digital-life`. Route an AI assistant, Agent, voice assistant, smart-hardware companion or explicitly requested AI digital life to the child substyle without asking the user to choose a separate top-level category. Use the parent style for generic brand mascots. When loading the child, apply its declared inheritance and child-precedence rules.

## Route the request

Choose one mode:

1. **Generate concepts** — turn a user request plus one active Style Profile into three independently conceived concise text directions, then render the direction selected, combined or modified by the user.
2. **Extend an IP** — preserve a selected character and compose one default visual sheet with one enlarged hero and six expression/action extensions.
3. **Draft a Style Profile** — analyze a coherent reference-image set and produce a draft profile for human review.
4. **Review a proposal** — evaluate a text proposal against its brief and exact Style Profile.

Read [references/workflows.md](references/workflows.md) for the selected mode. Read [references/contracts.md](references/contracts.md) whenever creating or validating structured data.

## Core rules

- Act as a professional IP designer, not a prompt formatter. Automatically analyze the user's subject, likely brand or product context, audience appeal, emotional role, recognizability, and commercial extensibility before proposing directions.
- Keep that analysis internal unless the user asks for it. Convert the conclusions into concrete, visually judgeable choices rather than showing a long design report.
- Keep all operational mechanics invisible by default. Never tell the user that you are reading a profile, running a script, checking a ledger, applying canonical IDs, cooling down recent faces, filling a contrast matrix, assigning structure slots or blocking prompt fallbacks.
- Do not announce a recipe such as “the three directions will use these three body types or eye grammars.” Present each proposal as a complete character idea, not evidence of combinatorial coverage.
- When a short progress update is necessary during generation, use designer-facing language only, such as `我会按你选定的方向继续完善角色并生成图像。` Do not include filenames, commands, IDs, percentages, internal nicknames, rule names or prompt details.
- If the user asks why a design decision was made, explain it in ordinary design language. Reveal technical rule IDs, history data or prompt mechanics only when the user explicitly asks for implementation details.
- When information is missing, use design judgment to create three credible alternatives; do not produce random archetypes or generic template variations merely to fill slots.
- Separate facts supplied by the user, explicit inferences, and unresolved items.
- Never run a personality or audience questionnaire before the first three directions.
- When the request is vague or minimal, ask one concise open question combining only: the brand/product positioning or desired impression, and any existing brand cue the user would like naturally reflected in the character. Let the user answer freely. Always end this question with an explicit low-pressure option equivalent to `如果暂时没有特别设定，也可以直接说“自由发挥”，我会根据角色特点给出三个方向。` Never omit the free-play option when adapting the wording. Do not proactively ask what should be avoided; record such constraints only when the user volunteers them.
- If the user says `随意发挥／都可以／没有特别设定／你来决定`, explicitly asks not to be questioned, or already provides sufficient brand positioning and desired brand cues, skip further clarification and proceed directly.
- Infer personality, emotional energy and audience appeal through professional design judgment so the three directions retain creative range.
- Do not ask about use cases during initial concept exploration; collect them later only when developing applications and extensions.
- Load only an `active` registered style or a native `published` profile for final concept generation. A `draft` profile may be used only when the user explicitly asks for an exploratory preview.
- Preserve registered read-only assets verbatim. Do not normalize, translate, rename, or rewrite their rule content.
- Ground design rationales in exact JSON fields and explain them through the paired Style Bible. Do not claim compliance with rules that do not exist in those assets.
- Treat observed tendencies as selectable evidence, not a checklist. Apply only the profile options that serve the brief.
- Permit intentional winks, raised brows, offset mouths, asymmetrical poses and unusual anatomy when the character concept supports them. Treat accidental gaze conflict, feature drift, melting or duplication as failed generation.
- Produce three independent proposals unless the user requests another count. Do not assign baseline/refinement/exploration roles and do not force geometry, face or limb coverage quotas.
- Never bind proposal numbers to recurring morphology roles. A first image is not automatically the fused round character, a second is not automatically the articulated body, and a third is not automatically the seated or experimental character.
- Treat profile frequencies as tendencies across requests, not slots within every set. Develop the concepts first, then shuffle their display order.
- Do not repeatedly couple the same structure, limb treatment and expression. Recombine them from the character truth; when recent outputs exist in the conversation, avoid their previous number-to-design mapping.
- Treat the user's explicit aesthetic adjectives as the main direction for the set.
- For animal concepts, default to Style-Bible-first stable recognition. Retain two or three strong species cues, while rebuilding anatomy into a simple toy-like relationship with hidden, compact, integrated or graphically extended limbs. “Stable recognition” limits aggressive morphological abstraction; it never authorizes realistic pet anatomy, natural quadruped proportions, articulated chests or detailed paws. Do not reuse one generic animal head and merely swap ears, horns, muzzle patches or color.
- For first-round animal concepts, follow the same moderate generation logic used by the original Style Bible examples: keep a familiar, attractive toy-like animal base and create visible but restrained differences through ear/head relationship, overall proportion, pose, facial attitude, color and material. Give each proposal one clear memory hook, but do not force extreme abstraction or remove all distinctive structure. Similarity is acceptable when the three characters still read as intentionally different designs.
- Treat supporting and accent colors as optional. Add an accent only when it has an explicit brand, concept, function, material or structural reason; otherwise omit it.
- In the first round, keep species recognition stable but leave color open. Natural, transformed-natural, brand-led and concept-led nonliteral colors are all valid when the choice has a clear rationale and uses simple large color relationships. Nonliteral color does not require morphological abstract-mode opt-in.
- Across the rolling history window of conventional eyed characters, target roughly 65% matte no-sclera eyes and 35% graphic sclera eyes; do not force every three-image set into the same 2:1 arrangement. Low-frequency AI digital-life single-lens or state-window facial directions are excluded from this ratio. Never allow catchlights, white reflection dots, glossy eye highlights or glass-eye effects.
- Before prompting images, assign every conventional-face proposal a complete facial signature using canonical IDs from the active profile: eye family, scale/spacing, facial zone, brow-eye relation, nose/muzzle family, mouth family and primary expression. Three conventional-face proposals must use three different eye IDs and differ pairwise in at least three signature dimensions. Under the AI digital-life child profile only, a low-frequency single-lens or nonstandard state-window facial direction may instead use a complete focal signature covering focal type, orientation, internal state, deformation and motion. Never generate a faceless, light-core-only or ambient-mass character; use those references only for material behavior. Do not add a focal signature to the eye-history ledger or count it toward the 65:35 eye-system tendency.
- Among conventional-face directions in a three-direction set, the overselected eye pool `NS01/NS02/GS01` may contribute at most one proposal in total, the overselected mouth pool `M01/M06` may contribute at most one, and no exact nose-mouth pair may repeat. Treat `NM03+M04` and `NM05+M04` as one perceptually equivalent rounded-nose-plus-symmetric-W-mouth group and use that group at most once. Changing only gaze, brow angle, mouth corner or color is not a new face.
- Before concept development, use the newest eight accepted conventional-face results available in writable local state as a soft frequency reference: reduce the priority of recently repeated signatures, common eye IDs and common nose-mouth pairs, but reuse them when they are genuinely the best fit for the character. When script execution and writable skill state are available, use `scripts/manage_facial_history.py summary` and append accepted signatures with the same script. Otherwise, use accepted results visible in the current conversation and continue without exposing or treating missing persistent state as an error. Never append an AI digital-life focal signature.
- Keep the character body and expression system complete without relying on styling. In any round, a direction may use one simple character-driven accessory or garment when identity, behavior, brand or use scene naturally supports it. Use at most one primary item, keep construction minimal, preserve species cues, and do not add a new color without a reason.
- Under the AI digital-life child profile, treat elongated continuous unjointed limbs as a low-frequency concept-led exception. Use them only when role, action or silhouette clearly benefits, never as a required contrast slot or recurring proposal position.
- Default to character-first design. Unless the user explicitly asks to embody product functions in the IP, do not force product attributes, workflow concepts, interface semantics or functional metaphors into the character's anatomy, silhouette, cutouts, markings, props or pose. Let the base IP earn recognition through character origin, personality, proportion, face, material and natural silhouette; express product fit through role, behavior, state, motion, application and art direction instead.
- Default standalone character renders to a clean near-white neutral-gray studio background, approximately `#F7F8F8` in visual lightness, with only a barely visible neutral contact shadow. The background should read as white at first glance, not as a visibly gray surface. Keep it free of cream, beige, ivory, warm-yellow, sepia, muddy-gray or dirty off-white casts. For white or very pale characters, use only a subtly deeper near-white neutral gray for separation rather than warming or noticeably darkening the background. Override this only when the user explicitly requests another background, a transparent asset or a specific brand scene.
- When the user says only `帮我延展` and a selected character is clear from context, do not ask preliminary questions. Default to one finished extension sheet containing one enlarged hero character and six smaller expression/action variants.
- Art-direct extension sheets with the sensibility of a young contemporary Korean graphic designer: youthful, fashion-aware, clean, confident negative space, disciplined grid composition, and strong custom-type hierarchy. Preserve simplicity and do not imitate a named studio or designer.
- Use the same near-white neutral-gray ground as the default extension-sheet canvas. A user-provided brand color or explicitly requested art direction may override it, but never introduce an unrequested warm cream, yellow or muddy-gray cast.
- Treat the selected character as an identity lock. Preserve its dominant silhouette, proportions, ear/head geometry, facial construction, palette, material and signature feature across all seven appearances. Extend expression, gesture, body squash/tilt, ear/tail behavior and only necessary simplified limbs.
- Use exact provided copy. If no name or copy exists, use one or two short neutral English phrases such as `MOOD SET` or `CHARACTER DESIGN`; do not use numbered labels, invent a brand identity, or fill the board with decorative text.
- After delivering the Style-Bible-first stable-recognition animal set, ask one short optional follow-up: whether the user wants a more morphologically abstract exploratory set. Do not ask this before producing the first round.
- Start every direction from a fresh character truth and creative seed. Let anatomy, proportions, facial language, limbs, pose, color and material emerge from that concept instead of a reusable morphology template.
- Keep every concept inside the exact active Style Profile and interpret it through the paired Style Bible. Do not add a separate visual constraint system in the Skill.
- Natural similarity is allowed, but if a result repeats another direction's overall body-face-pose template, regenerate the repeated concept rather than editing one feature.
- After the brief is sufficient—or after the single lightweight answer—present three concise text directions using the response contract.
- In user-facing proposals, write `性格` as three concise comma-separated descriptors. Each may be an adjective or a very short phrase such as `反应灵敏` or `有陪伴感`, but never a sentence, personality joke or extended explanation. Write `五官` as one compact phrase covering only the most visible eye, mouth or expression cues. Keep detailed facial construction in the internal generation prompt rather than displaying it.
- Ask the user to select A/B/C, combine elements or state a modification. A clear choice or combination is final authorization: generate the selected direction immediately without another confirmation.
- Generate one image by default after selection. Generate all three directions only when the user explicitly requests the complete comparison set.
- When the user requests exactly `N` images, finish the whole batch contrast, facial-signature and prompt preflight before the first image call, then make exactly `N` planned generation calls. Do not discover an avoidable duplicate after generation and add an unrequested replacement image. Reserve regeneration for genuine rendering artifacts, and identify the earlier image as discarded if that exception occurs.
- Keep generation prompts internal by default. Show them only when the user explicitly asks to inspect or copy the prompt.
- Mark all character names as working names; do not imply trademark clearance.
- Keep negative constraints separate from positive prompts.
- Reject a render or sheet whose nominally neutral background reads yellowed, creamy, beige, sepia, muddy or visibly warm-tinted.
- Avoid named-artist style imitation and near-copying of existing characters. Extract only high-level, non-exclusive design principles.

## Generate concepts

1. Resolve the requested style through `assets/style-profiles/registry.json`. Route AI assistants, Agents, voice assistants, smart-hardware companions and digital-life briefs to `brand-mascot-ai-digital-life`; otherwise use `brand-mascot` unless the user explicitly requests another registered style.
2. For a registered asset pair, run `scripts/validate_style_assets.py assets/style-profiles/registry.json <style-key> --require-active` when script execution is available. Otherwise, load only entries already marked `active` in the bundled registry.
3. Load the registered JSON as structured rules, then load its Style Bible as the method and explanation layer.
4. For an unregistered native profile, run `scripts/validate_style_profile.py <profile> --require-published` when script execution is available. Otherwise, use it for final generation only when its status is explicitly `published` and required fields are complete.
5. Build the Design Brief from the user's request.
6. If the request is minimal and lacks both brand positioning and desired brand cues, ask one concise combined question and explicitly offer `自由发挥` in the same message. If the answer delegates the decision, record that fact and make professional creative assumptions; never continue into personality or audience questions.
7. Obtain rolling eye-system and recent eye and nose-mouth frequency information from the newest eight accepted characters. Use `scripts/manage_facial_history.py summary` when writable script state is available; otherwise use accepted conventional-face results visible in the current conversation.
8. Independently develop three internal proposals using the expanded Character Proposal contract. Keep product functionality out of the base character's anatomy and visual features unless the user explicitly requests that translation. Do not assign proposal letters yet.
9. Build a three-row batch contrast matrix covering character truth, recognition cues, structure, limb treatment, pose, facial or focal signature, palette rationale and memory hook.
10. Run the brief-fit check, holistic repetition check, conditional canonical facial-ID check, nose-mouth pair check, rolling-ratio check and soft recent-frequency review. Regenerate any internal proposal that misses the user's explicit aesthetic adjectives, lacks a readable memory hook, becomes excessively abstract, is only a cosmetic variation, repeats an eye or nose-mouth grammar among conventional-face directions, produces any faceless, light-core-only or ambient-mass character, or violates applicable current-set high-frequency caps.
11. Shuffle the completed concepts into display order so morphology and emotional roles are not tied to recurring proposal numbers.
12. Present the three text directions in lettered order using the response contract and ask the user to select, combine or modify them.
13. After the user responds, compile every requested image prompt as one coordinated preflight batch. Verify the requested count, within-set facial or focal uniqueness, concept difference and likely fallback blocks before making any image call. Name only each direction's selected facial or focal decisions; never paste a menu of alternatives.
14. Generate immediately without displaying the prompt or asking for another confirmation. Generate one image by default; generate the full three-image comparison set only when explicitly requested.
15. Inspect every generated image against the Style Bible's intentionality and artifact checks. For first-round animals, require a familiar attractive animal base plus one clear, restrained memory hook. Reject both generic template results with no hook and results pushed into obvious morphological abstraction without user opt-in. View faces at reduced size and regenerate any result that falls back to a generic face. Preserve concept-driven asymmetry, but regenerate accidental gaze conflict, drifting or duplicated features, malformed limb connections, or meaningless distortion.
16. Save accepted images when possible. Treat `accepted` here as having passed every brief-fit, appeal, recognition and artifact gate—not merely as successfully generated. When writable state is available, append only accepted conventional facial signatures to `state/facial-usage-history.json`, keeping the newest eight entries; otherwise retain the accepted signatures in the current conversation context. Do not append AI digital-life focal signatures. For an animal-origin result, optionally ask after delivery whether the user wants a more abstract exploratory set.

Do not expose design analysis, long rationale, application advice, or prompt text unless the user explicitly requests it.

## Extend an IP

1. Resolve the selected character image from the conversation or ask for it only when no clear source exists.
2. Load the active Style Profile and paired Style Bible.
3. Preserve the character identity exactly; do not redesign its base anatomy, palette or face system.
4. Default to one complete landscape sheet with one enlarged hero on one side and six smaller expression/action variants on the other.
5. Ensure the six variants cover both facial emotion and physical action. Vary expression, gaze, mouth, body tilt/squash, ear behavior, tail behavior and only necessary simplified limbs; do not use six nearly identical standing poses.
6. Prefer the proven default layout: use the left half for a large English display title and the enlarged hero, and the right half for the six extensions. Keep the title prominent but subordinate to the character, and do not let it crowd the hero.
7. Build the composition on a visible but understated column-and-row grid. Align the hero, variant cells, headings and margins to shared axes; preserve especially generous outer safe margins on all four sides, plus comfortable internal gutters. Do not let titles or characters approach the canvas edges. Do not scatter, overlap or crowd elements.
8. Do not number the six variants. Pair the large English title with only small English microcopy and a few restrained graphic marks when useful.
9. If the user requests several options, keep the left-title/hero and right-extension structure as the preferred option; vary the landscape grid and typographic hierarchy without changing the character identity.
10. Inspect all seven character instances for identity drift, incorrect colors, extra features, eye highlights, malformed limbs and inconsistent materials.
11. Return the finished board image. Do not require the user to approve the six actions in advance.

## Draft a Style Profile

- Confirm the images form one intended aesthetic set. Flag obvious outliers instead of averaging them away.
- Observe before labeling. Record repeated, visible evidence across the set.
- Distinguish dominant rules, optional variations, contradictions, and unknowns.
- Do not include brand names, character names, or artist names as prompt instructions.
- Create a `draft` profile and validate it without `--require-published`.
- Present uncertain findings for human confirmation before changing status to `published`.

## Review

Score only what can be supported by the brief and profile. Review:

- brief fit;
- style-rule compliance;
- distinctiveness and memory hook;
- application extensibility;
- conflict and imitation risk.

For every issue, give a concrete revision. Do not use unsupported “trend” claims.

## Bundled resources

- `assets/style-profiles/registry.json`: authoritative style-to-asset routing and activation state.
- `assets/style-profiles/brand_mascot_style_profile_v1.json`: read-only structured rules for the active brand-mascot style.
- `references/style-bibles/品牌吉祥物_Style_Bible_v1.0.md`: read-only design method and explanation layer for the active brand-mascot style.
- `assets/style-profiles/brand_mascot_ai_digital_life_v1.json`: read-only structured child rules for AI assistants, Agents, smart hardware and digital-life mascots.
- `references/style-bibles/品牌吉祥物_AI科技数字生命_Style_Bible_v1.0.md`: material, form, light, motion and diversity method for the AI digital-life child style.
- `state/facial-usage-history.json`: optional mutable newest-eight facial-signature ledger used when writable local state is available; otherwise use current-conversation accepted results as the soft history reference.
- `scripts/manage_facial_history.py`: summarize the ledger before planning and atomically append only visually accepted character signatures.
- `assets/style-profiles/profile-template.json`: reusable native-profile template. Unregistered legacy placeholders are not selectable styles.
- `scripts/scaffold_style_profile.py`: create a new blank profile.
- `scripts/validate_style_profile.py`: validate structure and publication readiness.
- `scripts/validate_style_assets.py`: validate a registered asset pair, activation state, schema, and content hashes.
- `references/contracts.md`: schemas and output contract.
- `references/workflows.md`: detailed concept, profile-analysis, and review procedures.
