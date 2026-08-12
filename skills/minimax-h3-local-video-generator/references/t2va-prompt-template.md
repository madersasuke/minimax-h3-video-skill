# H3 T2VA prompt template

Use this template only when the user has not supplied a character reference. This route uses text-only prompting with the FL2VA UNET. If a character reference exists, stop and use the Ref2VA six-section guide instead.

Read `$h3-prompt-writing/references/base-en.txt`, `style-coherence.md`, `intra-film-diversity.md`, `animation-principles.md`, and `music-sync.md` first. Preserve the H3 field names and order.

## Template

```text
integrated_multimodal_description: [Shot 1] <global medium and finish>, <film type>, using <palette hierarchy>. <initial composition, environment, subject anchors, graphic system, first action, camera behavior, synchronized visible text and sound events>. <state visual invariants that must remain stable>. [Shot 2] At 00:SS.sss, the camera cuts to <new information: framing, subject action, spatial change, camera motion with type/amplitude/speed, graphic transition, exact beat event>. [Shot N] At 00:SS.sss, <climax and a clear path into the final held state>. Hold <exact final title/product/CTA composition> clearly through 15.00 seconds.

overall_soundscape: <one continuous paragraph, 1–4 English sentences, covering only necessary ambience and selected hero physical sounds; keep every effect sparse, short, and perceptually subordinate beneath the BGM; do not repeat dialogue or music>.

non_diegetic_music: <1–3 information-dense English sentences defining one coherent foreground BGM: two to four core instruments, tempo or BPM range, meter or pulse subdivision, recurring rhythmic cell, phrase structure, named accents, build or breakdown, climax, and final cadence; prohibit random instrument changes, competing grooves, and musical restarts; use N/A only when no background music is wanted>.
```

## Shot-writing checklist

- Begin Shot 1 without a timestamp.
- Number all shots sequentially.
- Give later shots strictly increasing `At 00:SS.sss` cut times.
- Derive cut times from a style-specific rhythm map; do not distribute shots at approximately equal intervals unless strict regularity is explicitly justified.
- Set a style-specific shot-change budget. Do not make rhythm irregular by reducing the number of shots; add short insert shots or two- to three-shot bursts at justified acceleration, escalation, reveal, or climax beats.
- Set a distinct-layout budget and layout IDs before writing shots. Count a landing as distinct only when at least three structural axes change; a new subject crop, word, card image, color accent, or small coordinate shift inside the same poster skeleton does not count.
- Excluding the final readable hold, keep at least 70% of major landings structurally independent unless serial repetition is explicit reference evidence.
- Rotate the primary motion carrier and transformation mechanism between adjacent beats. Dense, editorial, collage, playful, or action-led films should normally use at least four observable reference-derived mechanisms.
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
- Compose the BGM plan and timestamped cue sheet before assigning visual cut times, while preserving the mandated output-field order.
- Make anticipation, cuts, action landings, camera peaks, graphic transformations, and typography locks correspond to named BGM events such as pickups, downbeats, accents, fills, breaks, rises, drops, or cadence.
- Keep the BGM continuous across every cut. Do not restart or abruptly change music at shot boundaries.
- Keep sound effects sparse and lower than the score; avoid loud whooshes, impacts, clicks, or risers on every cut.

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
- BGM-first timing becomes a timestamped cue sheet: visual anticipation starts during pickups, hero actions and important cuts land on selected accents, follow-through crosses the following beat or sustain, acceleration follows fills or denser subdivisions, breath follows a thinner arrangement, and the final lock lands with the musical cadence;
- audio hierarchy becomes one coherent foreground score, a small number of subordinate hero effects, and low continuous ambience rather than competing sound layers;
- the approved reference cluster becomes one cross-modal style contract governing rendering, layout, density, motion, typography appearance, type motion, camera, transitions, edit rhythm, BGM, and sound effects;
- a layout-diversity matrix becomes shot-specific spatial scaffolds, subject scales and crops, focal counts, negative-space shapes, layer topologies, typography-image relationships, graphic operations, motion carriers, and exit transformations; each major landing states the three or more axes that make it structurally new;
- a deliberate layout callback becomes an `A-prime` transformation that preserves recognizable style DNA while changing at least three structural axes and performing a new narrative or rhythmic function;
- motion-family coherence becomes shared material response, easing, motif DNA, and directional logic, while motion diversity becomes rotating carriers and mechanisms rather than repeating one panel move or entry-settle-exit chain;
- reference-derived BGM names the visual evidence behind its genre family, timbre, instrumentation, arrangement density, BPM, rhythmic complexity, phrase spacing, dynamics, and cadence instead of choosing music independently;
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
33. one coherent BGM defines tempo, pulse, instrumentation, phrase structure, energy contour, climax, and final cadence before visual timestamps are assigned;
34. major visual events map to named BGM events, with anticipation before the accent, landing on the accent, and follow-through after it;
35. cuts do not restart or randomly change the BGM, and the music contains no competing groove or unrelated fill;
36. sound effects are sparse, short, and subordinate, with no loud whoosh or impact on nearly every cut;
37. camera, character, graphics, and typography use a controlled hierarchy of musical subdivisions rather than all hitting every beat simultaneously.
38. one approved reference cluster governs every artistic domain, and incompatible references are not averaged into a generic hybrid;
39. typography appearance and motion cite the reference's type, geometry, material, composition, era, density, or tone;
40. BGM genre, timbre, instruments, arrangement density, BPM, groove, phrase spacing, dynamics, and cadence cite evidence from the same reference cluster;
41. no art, motion, typography, rhythm, music, or sound decision would remain equally appropriate after replacing the reference with an unrelated style.
42. a layout-diversity matrix exists and every major landing has a layout ID plus a three-axis distinctness proof;
43. excluding the final hold, at least 70% of major landings have independent spatial skeletons unless approved reference evidence supports serial repetition;
44. no repeated poster template is disguised by different subject crops, words, card contents, colors, or minor coordinate changes;
45. every intentional `A-prime` callback changes at least three structural axes and serves a new function;
46. adjacent beats rotate primary motion carriers and entry-assembly-settle-exit chains, with at least four observable mechanisms in dense or editorial work;
47. global style invariants are stated once and shot descriptions use specific new construction verbs instead of repeating the same style paragraph and motion phrasing.
