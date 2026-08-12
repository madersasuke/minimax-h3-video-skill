---
name: minimax-h3-local-video-generator-pre-bgm
description: Turn a theme, film type, style-reference images or videos, optional user-supplied character images, and optional exact copy into one or more fully designed 15-second MiniMax H3 videos generated through the user's local ComfyUI workflow. Use for character or product PVs, game trailers, title sequences, music-led motion-design films, image or video style-reference analysis, bidirectional visual-density matching, style-derived non-uniform rhythm mapping, momentum-linked shot changes, pause-free motion continuity, temporal motion-signature extraction, character-palette extraction, reference-specific motion routing, Disney Twelve Principles-based motion design, style-matched multi-stage typography choreography, differentiated variants, local H3 queueing and monitoring, optional assembly, technical and visual QA, and a final Image 2 cover. Route projects without user-supplied character references to text-only generation with the FL2VA checkpoint; route projects with character references to Ref2VA.
---

# MiniMax H3 Local Video Generator

Produce an end-to-end local video package from a short creative request. Treat design development, H3 prompting, generation, review, optional editing, and cover creation as one production chain.

## Required companion skills

- Read and follow `$h3-prompt-writing` for every H3 prompt. For text-only generation, read its `references/base-en.txt`; for Ref2VA, read its `references/ref-en.txt`.
- Use `$imagegen` for the final Image 2 cover.
- Read and follow `$hyperframes` when building deterministic HTML/GSAP titles, transitions, or assembly.
- Read and follow `$video-use` when editing generated clips. Obtain its required strategy confirmation before touching the cut.

## Production workflow

### 1. Resolve the brief

Accept any combination of:

- subject or campaign theme;
- film type and target audience;
- written style direction;
- one or more style reference images;
- one or more style reference videos;
- one or more character reference images;
- required copy, logo, product, character, music, or sound constraints.

Do not force a long questionnaire. Infer non-critical choices and ask only for information that changes the production materially.

Before inventing a character or writing promotional copy, explicitly ask whether the user wants to upload character reference images or supply exact copy. Skip any answered part when the user has already provided or declined that asset. Do not present a production prompt for approval until these asset choices are resolved.

Keep the inputs in distinct roles:

- **Style-reference images or videos** control medium, composition, geometry, visual density, typography, material treatment, motion grammar, edit rhythm, tempo, easing, transition family, camera logic, and spatial tendency.
- **Character references** control identity anchors, silhouette, face and hair cues, costume, accessories, proportions, and the video's palette hierarchy.
- **User copy** controls every visible name, title, label, slogan, subtitle, and CTA verbatim.

When the user supplies character images, inspect them separately from the style references. Extract a compact character anchor covering silhouette, face, hair, costume, accessories, proportions, and three to six dominant or accent colors. Re-map the style reference's contrast hierarchy and graphic roles onto the character-derived palette instead of copying the style reference's literal colors. Preserve the style reference's motion system even when its palette differs from the character. If the supplied assets conflict, prioritize character identity and character-derived color over the style reference's subject and literal colors, while prioritizing the style reference for motion, layout, material, and typography behavior.

Route the generation mode from character-reference availability before writing the prompt:

- If the user supplies no character reference, create an original character and use text-only T2VA prompting with the locally installed FL2VA UNET `minimax_h3_fl2va_pruned_int8_convrot.safetensors`. Style-reference images and videos remain analysis-only and are not attached to generation.
- If the user supplies one or more character references, use Ref2VA. Use the six-section full-reference prompt structure from `$h3-prompt-writing/references/ref-en.txt`.
- Attach and label only approved character assets. Style-reference images and videos remain analysis-only unless the user explicitly authorizes them as generation references.
- Do not downgrade a character-reference project to text-only generation for speed. Do not use Ref2VA when character references are absent.

If the user declines to provide a character image, create an original character that fits the brief. If the user declines to provide copy, create concise original copy. Clearly label invented names and copy as proposals that may be replaced before generation.

When style-reference images or videos are supplied, inspect every asset. Extract the following reusable style DNA from images and from representative video frames:

1. medium and rendering language;
2. palette and contrast hierarchy;
3. geometry, silhouettes, and motifs;
4. texture and surface treatment;
5. composition, grid, whitespace, and focal hierarchy;
6. typography family, weight, outline or shadow treatment, scale hierarchy, alignment, cropping, overlap, masking role, and implied text behavior;
7. camera, transition, rhythm, and motion signatures;
8. visual complexity: whitespace ratio, occupied area, layer depth, element count, texture and motif density, overlap and edge cropping, and typography coverage;
9. elements to preserve and elements to avoid.

For every style-reference video:

1. verify duration, aspect ratio, frame rate, video stream, and audio presence with `ffprobe`;
2. extract representative frames or contact sheets covering the opening, every cut boundary, motion peaks, typography moments, transitions, and the ending;
3. separate the visual-art analysis from the temporal-motion analysis;
4. extract a motion signature covering shot cadence, hold duration, entry and exit carriers, easing character, acceleration and deceleration, movement amplitude and speed, dominant direction, camera behavior, transition mechanics, typography choreography, layer persistence, material response, and climax structure;
5. note audio-visual synchronization only when it visibly shapes the motion, without copying the original soundtrack.

When only still style references are supplied, derive an implied rhythm signature from visual evidence instead of falling back to uniform shot lengths. Use angle sharpness, curve softness, block weight, line fineness, visual density, whitespace, contrast, typography scale, directional force, repetition, and implied material behavior to choose a rhythm contour. Build deliberate contrast between short attacks, medium developments, longer pose or layout holds, acceleration, breath, climax, and final hold. Treat equal or near-equal shot spacing as an exception that requires clear metronomic evidence from the style. Do not create rhythm variation by merely reducing the number of shots. Add short insert shots or cut bursts at appropriate acceleration points when the reference supports them, while quieter beats retain internal motion.

Describe the style in transferable visual terms. Do not reproduce watermarks, unrelated logos, or accidental defects from the reference.

Treat a style-reference video as design evidence rather than a shot-by-shot remake. Do not copy its characters, products, narrative, dialogue, visible copy, logos, watermarks, exact frames, or soundtrack unless the user separately supplies and authorizes those assets.

Assign a low, medium, or high visual-density profile relative to the supplied style reference. Match complexity bidirectionally: preserve restraint and negative space when the reference is simple, and preserve layered richness when it is complex. Do not apply a fixed amount of decoration to every project. When adapting a portrait reference to landscape, redistribute its density into side columns, edge crops, foreground overlaps, and background modules instead of stretching the original layout or leaving large accidental gaps.

Read `references/motion-style-routing.md`. Derive a project-specific motion system from the reference's medium, composition, typography, geometry, and implied material behavior. Treat its listed families as examples, not presets. Never apply a visually exciting motion style merely because it worked for an unrelated reference.

Read `references/animation-principles.md` for every project. Apply Disney's Twelve Principles across characters, cameras, graphic elements, panels, transitions, typography, and secondary motion. Adapt their intensity to the approved style and material; do not force cartoon squash and stretch or exaggerated acting into rigid, minimal, luxury, diagrammatic, or industrial work.

Treat this routing as mandatory rather than decorative analysis:

- derive a distinct motion grammar for each reference type instead of reusing one fixed animation recipe;
- derive a distinct non-uniform rhythm contour for still references; do not divide the duration into approximately equal shots or reuse the same cut timestamps across projects;
- derive a style-specific shot-change budget as well as shot lengths; medium, dense, playful, editorial, action-led, or high-energy references normally need more visible compositions and strategically placed short-shot bursts than restrained references;
- never reduce shot changes solely to make intervals irregular; increase cuts at acceleration, reveal, escalation, or climax beats when doing so improves energy and information flow;
- include at least one meaningful tempo change, syncopated interval, breath, or acceleration before the final hold unless the style clearly calls for strict regularity;
- map every cut as a momentum bridge: name the outgoing carrier, direction, speed or rotational energy and the incoming camera, subject, typography, panel, shape, foreground wipe, or light motion that inherits it;
- cut while motion is still carrying energy instead of letting one shot stop before the next begins; use a pivot, impact, or deliberate counter-movement when direction changes;
- treat breath beats and pose islands as reduced-amplitude motion, not dead stops; preserve camera drift, parallax, hair or cloth overlap, particles, light travel, typography micro-adjustment, or another style-appropriate continuity carrier;
- when a video reference exists, derive timing, easing, camera, transitions, typography choreography, and material behavior from its temporal motion signature instead of guessing motion from still frames alone;
- match the reference's visual-density profile in every major landing composition, including the opening, hero beats, and final card;
- keep static graphic density separate from simultaneous motion complexity: a richly layered frame may contain many supporting elements, but only a few carriers should animate at once;
- prevent complex references from collapsing into plain backgrounds or sparse end cards, and prevent simple references from gaining filler patterns or gratuitous ornaments;
- when a reference contains deliberate typography or editorial layout, make dynamic typography and changing layout a recurring part of the video by default, not an end-card-only treatment;
- match type motion to its role in the reference: editorial blocks reflow and replace panels, handwritten type draws and revises, industrial labels scan and lock, and organic type stretches or recombines;
- treat typography as an active structural motion system rather than a decorative overlay; avoid generic fade-in, scale-up, or simple slide-in as the complete animation;
- give important text a style-matched multi-stage path such as entry, assembly or transformation, subject or panel interaction, readable lock, and motivated exit;
- match typography complexity to the reference: complex references require richer hierarchy, masks, crops, reflow, repetition, collisions, or multi-layer outlines, while simple references require restrained but still distinctive precision rather than generic motion;
- coordinate letter-, word-, line-, and block-level behavior hierarchically instead of animating every glyph at once;
- stage each major beat as an observable chain of staging, anticipation, primary action, graphic or environmental response, follow-through or overlap, and readable settle;
- use pose-to-pose anchors for identity, anatomy, products, typography locks, and precise layouts, with straight-ahead development reserved for suitable fabric, particles, ink, liquid, trails, or organic secondary motion;
- apply style-appropriate squash and stretch, arcs, slow in and slow out, timing, secondary action, exaggeration, solid construction, and appeal without breaking identity, geometry, hierarchy, or readability;
- omit recurring typography only when the user explicitly requests image-only motion or the reference clearly treats type as a minor signature.

### 2. Expand the creative direction

Create a compact design proposal before writing prompts:

- an input-provenance summary distinguishing style references, character references, and user copy;
- one-line campaign idea;
- 15-second narrative and rhythm arc;
- visual system and motif family;
- visual-density profile, expected whitespace or occupancy, and the background, middle-ground, subject, and foreground layer stack for each major beat;
- character identity anchors and character-derived palette mapping, or an explicit original-character proposal when no character reference is used;
- motion grammar and beat logic;
- rhythm map with a style-specific shot-change budget, irregular cut intervals, strategically added short-shot bursts, internal microbeats, acceleration or deceleration, breath points, climax timing, and final-hold duration derived from the style;
- cut-to-cut momentum bridge map naming the outgoing motion vector or carrier and the incoming motion that continues, redirects, transforms, or absorbs that energy;
- Twelve Principles plan for hero beats, including staging, anticipation, pose anchors, action paths, easing, arcs or justified straight paths, secondary action, follow-through, exaggeration level, construction safeguards, and final appeal;
- video-reference motion signature when present, including cadence, easing, amplitude, direction, camera logic, transition family, typography choreography, and final-hold behavior;
- typography system, exact user copy or clearly labeled proposed copy, role of each string, shot coverage, scale hierarchy, alignment, layer treatment, entry, assembly or transformation, subject or panel interaction, readable lock, and exit behavior;
- camera strategy;
- sound and music direction;
- quality risks and how the design avoids them.

Keep motion exciting without overloading a single frame. Use strong pose islands, silhouette beats, motivated cuts, graphic wipes, occlusion, and controlled camera moves to protect anatomy and subject clarity while preserving spectacle.

State why the chosen motion grammar belongs to the supplied reference. Select one dominant motion engine and one coherent directional or spatial tendency. Keep any secondary engine subordinate; as a default, use roughly 70% dominant and no more than 30% secondary behavior.

When the reference uses typography, specify which shots contain type and how it participates in masks, crops, panels, transitions, spatial divisions, or subject reveals. Ensure most appropriate shots contain designed typography or layout changes; do not satisfy the requirement with a single final title card.

### 3. Confirm the generation batch

Before queueing, present one compact confirmation containing:

- number of clips;
- duration;
- aspect ratio;
- megapixels;
- sampler steps;
- generation route: text-only with FL2VA UNET, or character-reference Ref2VA;
- character source: user reference or original;
- copy source: user-supplied or proposed;
- style-reference image or video's role and whether it remains analysis-only;
- whether final assembly is requested.

Use the defaults in `references/production-spec.md` when the user does not specify values. Do not ask for a second confirmation after these parameters are approved unless scope changes materially.

### 4. Design genuinely different variants

For multiple clips, keep the theme and style DNA consistent while changing at least four axes per variant:

- spatial system;
- dominant motion behavior;
- typography layout;
- camera logic;
- transition family;
- graphic motif;
- narrative emphasis;
- climax and end-card composition.

Do not create variants by changing only a seed or a few adjectives. Write a variant matrix first and audit it against `references/production-spec.md`.

Both variants must remain inside the same routed motion system unless the user explicitly asks to compare different motion styles. Vary the choreography and spatial construction, not the design identity.

### 5. Write the routed MiniMax H3 prompt

For projects without character references, write a text-only T2VA prompt and load the FL2VA UNET. Use the exact three-field structure required by `$h3-prompt-writing`:

Use the exact three-field structure required by `$h3-prompt-writing`:

```text
integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: ...
```

Write prompt structure and scene description in English. Preserve visible copy, dialogue, and lyrics verbatim in their original language. Define the global style, subject anchors, palette, and initial composition at the start of Shot 1. Use strictly increasing cut times and land the final frame at the requested duration.

Derive every cut time from the approved rhythm map and shot-change budget. Avoid evenly spaced or near-evenly spaced shots unless strict regularity is an explicit style trait. Use both strategically added short-shot bursts and internal microbeats, layout changes, action accents, or moving holds; do not create variation by reducing shots. At every cut, explicitly carry momentum from the outgoing camera or element motion into an incoming camera, subject, shape, panel, typography, foreground wipe, or light movement. Make the prompt visibly encode where the film accelerates, breathes, hits, redirects, and settles without obvious dead air.

Do not merely write `follow Disney's Twelve Principles`. Translate them into observable instructions for each major beat: how the focal idea is staged, what anticipation prepares the action, which key poses or layouts anchor it, how the action accelerates and decelerates, whether the path follows an arc or justified straight rail, which secondary layers overlap or follow through, what is exaggerated, and how the frame settles into an appealing readable state while a continuity carrier remains alive. Preserve volume, anatomy, product geometry, typography spelling, and layer order.

For projects with character references, do not use the three-field template above. Write the Ref2VA six-section structure in this exact order: `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, and `non_diegetic_music`. Assign stable reference labels and define each character reference's role.

Translate the approved visual-density profile into observable shot instructions. For complex references, specify recurring background, middle-ground, subject, and foreground layers; describe overlaps, edge crops, pattern fields, secondary cards or motifs, and prevent later shots from simplifying into plain fields. For simple references, cap the motif family, protect deliberate whitespace, and omit filler decoration. Never use vague phrases such as `rich detail` or `minimal design` without naming the visible layer structure.

When a style-reference video exists, translate its motion signature into observable shot timing: specify what enters, the path and easing it follows, the landing pose or layout, the hold length, the exit carrier, the camera's type and amplitude, and the next transition. Preserve the reference's motion character without copying its original sequence or subject matter.

Integrate negative requirements as concrete visual invariants inside the main description instead of adding unrelated top-level fields. Specify identity and costume consistency only when a recurring character exists. Limit simultaneous complex body motion, camera roll, fast parallax, and dense typography; distribute them across beats.

For typography-led references, quote every intended visible string and distinguish between process typography, which may be cropped or briefly obscured, and final-card copy, which must hold clearly. Describe observable layout changes at shot level; generic phrases such as `dynamic typography` are insufficient without scale, alignment, entry, transformation, and exit behavior.

For every important visible string, specify its typographic role, scale, alignment, layer depth, surface treatment, entry carrier and direction, easing, word- or line-level assembly, interaction with the subject or graphic panels, transformation or reflow, readable lock duration, and exit carrier. Use at least two meaningful stages before the readable lock when the style supports complexity. In restrained styles, replace spectacle with precise alignment, cropping, tracking, masking, or measured reordering; do not fall back to a plain fade or scale. Keep only a controlled subset of letters, words, or blocks moving simultaneously.

Read `references/t2va-prompt-template.md` only for the no-character-reference text-only route. For a character-reference project, read `$h3-prompt-writing/references/ref-en.txt` instead.

### 6. Run the local ComfyUI workflow

Use the user's local ComfyUI workflow. Do not call the MiniMax cloud API.

1. Check `http://127.0.0.1:8188/queue`.
2. If ComfyUI is offline, launch the user's configured local ComfyUI instance and wait for its configured port.
3. Refuse duplicate submission when the queue is non-empty unless the user explicitly requested queued jobs.
4. Save every final prompt before submission.
5. For a project without character references, submit one GPU job at a time with `scripts/queue_t2va.py`; verify its dry-run reports the FL2VA UNET before queueing.
6. For a character-reference project, use the local Ref2VA graph, attach only the approved character inputs, and verify the Ref2VA UNET and reference labels before queueing. Do not submit any Ref2VA route through `scripts/queue_t2va.py`.
7. Monitor with `scripts/monitor_t2va.py --once`; never spin in a blocking loop longer than 60 seconds.
8. Preserve the user's existing virtual-memory configuration; virtual memory may improve crash tolerance but does not accelerate sampling.

Use character-reference availability as the mandatory router. Style-reference images or videos alone never trigger Ref2VA. No character reference means text-only prompting with the FL2VA UNET; any approved character reference means Ref2VA. Never infer the route from style assets.

### 7. Review every generated clip

Perform both technical and visual review before delivery:

- verify duration, resolution, frame rate, video stream, and audio stream with `ffprobe`;
- extract representative frames or a contact sheet;
- inspect the opening, every cut boundary, action peaks, typography moments, and final card;
- reject or flag broken anatomy, identity drift, muddy motion, unreadable copy, unwanted photorealism, uncontrolled flicker, palette drift, accidental logos, and weak final holds;
- compare recurring identity anchors and palette against the user-supplied character references when present;
- verify every visible user-supplied string character-for-character and clearly flag model-rendered text errors;
- compare representative frames and the final card against the style reference's visual-density profile; reject both simplification collapse and unjustified complexity inflation;
- when a video reference exists, compare cut cadence, holds, easing, dominant direction, camera behavior, transition mechanics, typography choreography, layer persistence, and climax structure against its approved motion signature;
- when only still references exist, reject flat cadence, near-uniform shot spacing, repeated cut templates, or a film with no style-derived acceleration, breath, syncopation, or tempo contrast;
- reject typography that relies mainly on basic fades, uniform scaling, or identical slide-ins; reject type motion that ignores the reference's material, geometry, density, rhythm, and layout logic;
- verify that process typography drives masks, panels, crops, spatial divisions, subject reveals, or transitions where appropriate, and that final-card typography completes a clear style-matched lock and readable hold;
- reject hero actions without readable staging or anticipation, flat constant-speed movement, simultaneous stopping of all layers, unjustified linear organic motion, missing follow-through, or exaggeration that breaks identity or geometry;
- verify style-adapted use of squash and stretch, pose-to-pose or straight-ahead planning, slow in and slow out, arcs, secondary action, timing, exaggeration, solid construction, and appeal across the complete film;
- reject motion that is generic, template-like, or incompatible with the reference's medium, typography, composition, or material logic even when individual frames look attractive;
- reject a clip when the reference contains prominent typography or layout but the generated film leaves most shots without designed type motion or dynamic layout;
- keep outputs and prompts paired by stable names.

Do not silently present a failed generation as final. If only one region fails, prefer a targeted rerun with one prompt correction. Cap automatic prompt-revision reruns at two per variant, then report the persistent issue.

### 8. Assemble only when it improves the result

After all source clips pass review, choose the lightest suitable route:

- no edit when one clip already functions as the final film;
- `$video-use` for editorial selection, rhythm trimming, audio continuity, grading, and multi-clip assembly;
- `$hyperframes` for deterministic typography, title cards, transitions, captions, or frame-accurate motion packaging.

Preserve H3-generated MG as the primary visual language. Do not replace it with generic post-production overlays. Before editing, present the required plain-language strategy and wait for confirmation.

### 9. Generate the cover

Use Image 2 through `$imagegen` after the final video is selected. Base the cover on the strongest hero frame and the approved style DNA. Match the delivery aspect ratio unless the user requests a platform-specific thumbnail.

When character references exist, preserve their approved identity anchors and character-derived palette in the cover while retaining the style reference's composition and graphic language.

Keep cover copy short. Ask Image 2 to render the exact title verbatim; if text accuracy fails, generate the artwork without text and add exact typography deterministically. Save the selected cover beside the final video.

### 10. Deliver the package

Deliver:

- final video or approved source clips;
- final cover;
- final H3 prompt for each clip;
- a concise parameter summary;
- absolute output paths.

Render local video and image files inline when the client supports it. Keep all working files under a project-specific directory and never overwrite unrelated user files.

## Local resources

- `references/production-spec.md`: local paths, defaults, variant matrix, naming, stability, and QA rules.
- `references/t2va-prompt-template.md`: H3 T2VA production template and prompt quality checklist.
- `references/motion-style-routing.md`: open-ended method for deriving a reference-specific art and motion system; read whenever a style image, style video, motion reference, or design-language request is supplied.
- `references/animation-principles.md`: style-adapted application of Disney's Twelve Principles; read for every project before designing beats or writing prompts.
- `scripts/queue_t2va.py`: validate and submit one no-character-reference text-only job while forcibly selecting the FL2VA UNET.
- `scripts/monitor_t2va.py`: inspect one job without blocking.
