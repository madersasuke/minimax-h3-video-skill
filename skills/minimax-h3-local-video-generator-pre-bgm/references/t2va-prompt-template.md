# H3 T2VA prompt template

Use this template only when the user has not supplied a character reference. This route uses text-only prompting with the FL2VA UNET. If a character reference exists, stop and use the Ref2VA six-section guide instead.

Read `$h3-prompt-writing/references/base-en.txt`, `animation-principles.md`, and `music-sync.md` first. Preserve the H3 field names and order.

## Template

```text
integrated_multimodal_description: [Shot 1] <global medium and finish>, <film type>, using <palette hierarchy>. <initial composition, environment, subject anchors, graphic system, first action, camera behavior, synchronized visible text and sound events>. <state visual invariants that must remain stable>. [Shot 2] At 00:SS.sss, the camera cuts to <new information: framing, subject action, spatial change, camera motion with type/amplitude/speed, graphic transition, exact beat event>. [Shot N] At 00:SS.sss, <climax and a clear path into the final held state>. Hold <exact final title/product/CTA composition> clearly through 15.00 seconds.

overall_soundscape: <one continuous paragraph, 1–4 English sentences, covering ambience, physical movement, impacts, texture sounds, and non-verbal human sounds; do not repeat dialogue or music>.

non_diegetic_music: <1–3 English sentences describing instrumentation, tempo, rhythmic structure, dynamic changes, and final cadence; use N/A only when no background music is wanted>.
```

## Shot-writing checklist

- Begin Shot 1 without a timestamp.
- Number all shots sequentially.
- Give later shots strictly increasing `At 00:SS.sss` cut times.
- Derive cut times from a style-specific rhythm map; do not distribute shots at approximately equal intervals unless strict regularity is explicitly justified.
- Set a style-specific shot-change budget. Do not make rhythm irregular by reducing the number of shots; add short insert shots or two- to three-shot bursts at justified acceleration, escalation, reveal, or climax beats.
- Use internal microbeats, moving holds, layout accents, acceleration, or deceleration inside longer shots in addition to strategically added cuts.
- At every cut, name the outgoing motion carrier and the incoming camera or element motion that inherits, redirects, transforms, or absorbs its direction, speed, scale, or rotation.
- Cut while outgoing motion still carries energy. Avoid rest-to-rest cuts, frozen breath beats, and shots that visibly stop before the next shot begins.
- Describe each major beat through staging, anticipation, pose or layout anchor, primary action, secondary response, follow-through or overlap, settle, and motivated exit.
- Translate Disney's Twelve Principles into visible actions and easing; do not rely on naming the principles alone.
- Introduce new information at every cut.
- Describe camera movement naturally with type, meaningful amplitude, and speed.
- Quote every visible text string exactly.
- For each important string, specify typographic role, hierarchy, entry carrier, easing, grouping level, construction or transformation, subject or panel interaction, readable lock, and exit carrier.
- Avoid using fade-in, uniform scale-up, or identical slide-in as the complete typography animation.
- Keep visible text in its original language.
- Use stable speaker IDs only when speech or singing exists.
- Land the ending at exactly the approved duration.
- Put diegetic sound events inside the relevant shot and summarize ambience in `overall_soundscape`.
- Put only audience-heard background music in `non_diegetic_music`.

## Design-to-prompt conversion

Translate the approved design proposal into observable instructions:

- an original character becomes explicit silhouette, face, hair, costume, accessory, proportion, and palette anchors derived from the approved brief; this template never consumes a user-supplied character reference;
- a style reference becomes medium, composition, material behavior, spatial tendency, typography behavior, transition family, and beat logic; its literal colors are re-mapped to the character-derived palette when a character reference exists;
- a still style reference becomes a non-uniform rhythm contour inferred from angle sharpness, curve softness, visual weight, line fineness, density, whitespace, contrast, typography scale, directional force, repetition, and material behavior;
- a rhythm contour becomes a style-specific shot-change budget plus explicit short attacks, strategically added cut bursts, medium developments, moving pose islands, internal microbeats, breath points, acceleration or deceleration, climax timing, and final-hold duration rather than equal shot spacing or fewer shots;
- cut-to-cut continuity becomes an explicit outgoing carrier, screen direction, speed, scale or rotation trend, cut-on-motion point, and incoming carrier that inherits, redirects, transforms, or absorbs the energy;
- a style-reference video contributes two separate outputs: representative frames define art direction and visual density, while its temporal motion signature defines cadence, holds, easing, amplitude, direction, camera logic, transition mechanics, typography choreography, layer persistence, and climax behavior;
- video-derived motion becomes observable shot instructions describing entry carrier, path, easing, landing, hold length, exit carrier, camera behavior, and next transition without copying the source sequence or subject;
- a complex style reference becomes an explicit background, middle-ground, subject, and foreground stack with named patterns, secondary modules, overlaps, edge crops, typography coverage, outlines, shadows, and micro accents that persist through the final card;
- a simple style reference becomes a deliberately limited layer stack with protected whitespace, few motifs, restrained typography, and no filler decoration;
- visual density does not mean animating every element at once; keep supporting layers static or subordinate while one to three carriers perform the main beat;
- user-supplied visible copy remains verbatim, while any invented name or slogan is clearly presented for approval before it enters the prompt;
- a style-matched typography system becomes multi-stage choreography: entry, word- or line-level assembly, crop or reflow, foreground or background masking, interaction with the subject or panels, readable lock, and motivated exit;
- a restrained typographic reference becomes precise tracking, alignment, cropping, masking, or measured reordering, while a dense reference may add repeated blocks, layered outlines, collisions, panel swaps, and deeper foreground or background interaction;
- typography complexity does not mean moving every glyph at once; stagger controlled groups of letters, words, lines, or blocks while supporting type remains stable;
- Disney's Twelve Principles become observable staging, anticipation, style-appropriate squash and stretch, pose-to-pose anchors or straight-ahead secondary motion, follow-through, overlap, slow in and slow out, arcs or justified straight paths, subordinate secondary action, timing, controlled exaggeration, solid construction, and final appeal;
- a rigid or minimal style reduces deformation while retaining preparation, easing, overlap, timing, staging, and appeal; an elastic or character-led style may use stronger deformation, arcs, anticipation, and exaggeration;
- `high energy` becomes a BPM range, cut cadence, camera speed, action path, and impact timing;
- `premium` becomes material control, negative space, restrained palette, precise alignment, and clean final holds;
- `MG` becomes named shapes, grids, wipes, symbol behavior, type layout, and beat-synchronized transformations;
- `anime` becomes 2D cel shading, controlled smear frames, impact poses, line hierarchy, and flat color separation;
- `cinematic` becomes lens/framing logic, depth staging, motivated movement, lighting direction, and sound scale.

Avoid relying on abstract mood adjectives when an observable visual or audible instruction can express the same idea.

## Consistency block

Add only relevant constraints as natural sentences near the end of the main description:

```text
The subject keeps the same silhouette, costume, color blocking, face or mask design, and body proportions throughout. The film remains in the approved medium and palette, with no photorealistic or 3D style drift. Typography appears only at the specified beats, remains legible, and contains no random letters or misspellings. Flashes are isolated to the named frames and never become continuous strobing.
```

Adapt this block to products, environments, or abstract films; do not mention characters when none exist.

## Prompt audit

Before submission, verify:

1. the three required fields exist once and in order;
2. the timeline fits the requested duration;
3. no shot asks for multiple incompatible hero actions simultaneously;
4. every graphic motif has a defined appearance and behavior;
5. exact copy is quoted and readable in a held composition;
6. sound effects correspond to visible actions;
7. music dynamics correspond to visual beat events;
8. every negative requirement is concrete and relevant;
9. character identity and palette come from the approved character source, while motion and layout come from the approved style source;
10. every user-supplied visible string is preserved character-for-character;
11. visual density matches the approved style reference instead of defaulting to sparse or maximal;
12. complex references retain their layer richness through later shots and the final card, while simple references preserve intentional whitespace;
13. static layer richness does not create simultaneous motion overload;
14. video-reference art direction and temporal motion signature are analyzed separately when a video is supplied;
15. video-derived cadence, easing, camera, transitions, typography choreography, and final-hold behavior remain visible in the prompt without copying the original sequence;
16. still-reference cut times follow a style-derived rhythm contour rather than an approximately even division of the duration;
17. at least one meaningful acceleration, deceleration, syncopated interval, breath, or tempo contrast appears before the final hold unless strict regularity is justified;
18. every important string has explicit role, hierarchy, entry, construction or transformation, interaction, readable lock, and exit behavior;
19. typography motion matches the reference's material, geometry, density, layout, and rhythm instead of relying on basic fades, uniform scaling, or repeated slide-ins;
20. letter-, word-, line-, and block-level movement remains hierarchically controlled;
21. process typography participates in masks, panels, crops, transitions, spatial divisions, or subject reveals where appropriate;
22. major beats explicitly describe staging, anticipation, pose or layout anchors, primary action, secondary response, follow-through or overlap, settle, and exit;
23. Disney's Twelve Principles are applied across the complete film with intensity adapted to the approved style and material;
24. squash and stretch or exaggeration never breaks volume, identity, anatomy, product geometry, spelling, or layer order;
25. organic paths use arcs while straight or mechanical paths are visually justified;
26. multiple variants do not reuse the same layout, motion, typography, or timestamp skeleton;
27. the final frame is stable, appealing, and readable enough to serve as a cover candidate.
28. rhythm variation does not come from reducing shot changes, and the shot-change budget fits the reference's energy and density;
29. acceleration, escalation, reveal, or climax zones use added short shots or cut bursts when appropriate, and every cut introduces new information;
30. every adjacent shot pair defines an outgoing and incoming momentum carrier through camera or element motion;
31. no ordinary cut is rest-to-rest, and breath beats or pose islands retain subtle continuous motion;
32. the final layout remains readable while supporting movement decays gradually instead of freezing abruptly.
