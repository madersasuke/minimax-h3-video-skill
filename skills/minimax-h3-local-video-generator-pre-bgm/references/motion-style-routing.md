# Motion Style Routing

Use this reference to derive motion from a supplied visual style. The goal is not to classify the image into a fixed preset. Build a motion system that feels native to that image.

## Core rule

Derive in this order:

`medium → composition → geometry → typography → material behavior → visual density → spatial tendency → rhythm contour → tempo → transition family → prohibitions`

Do not start from a favorite effect, camera move, or previous successful prompt.

Use this routing together with `animation-principles.md`. The routed style controls how strongly each of Disney's Twelve Principles appears; the principles control motion clarity, weight, preparation, overlap, timing, construction, and appeal.

## 1. Extract motion evidence

Record the following before writing shots:

1. **Medium**: vector, cel animation, paper collage, ink, screen print, glass, metal, fabric, pixel art, pencil, oil paint, clay, photography, or a hybrid.
2. **Composition**: centered, symmetrical, modular grid, free collage, deep perspective, circular, scroll-like, panel-based, or whitespace-led.
3. **Geometry**: rounded or sharp; heavy blocks or fine lines; regular or organic; continuous or fragmented.
4. **Typography role**: impact object, collage block, elastic character, architectural form, archive label, instrument scale, or quiet signature.
5. **Subject anchor**: silhouette, face, clothing blocks, product contour, emblem, or other features that must survive motion.
6. **Motif family**: four to seven shapes already present in the reference or naturally implied by it.
7. **Avoid list**: effects, materials, lighting, camera language, and spatial treatments that would contradict the reference.

## 2. Match visual density

Measure the reference before designing shots:

- approximate whitespace versus occupied area;
- number of primary masses, secondary modules, and micro accents;
- visible background, middle-ground, subject, and foreground depth bands;
- texture, pattern, and motif density;
- typography coverage and number of type scales;
- frequency of overlap, masking, repetition, and edge cropping;
- surface richness such as outlines, shadows, borders, grain, and internal detail.

Assign a relative density profile:

- **Low**: few primary elements, broad deliberate whitespace, limited motifs, shallow overlap, and restrained surface detail.
- **Medium**: several coordinated modules, moderate whitespace, recurring motifs, two or three depth bands, and selective texture.
- **High**: layered background fields, multiple secondary modules, micro accents, frequent overlap or edge cropping, broad typography coverage, and distinct foreground, subject, middle-ground, and background bands.

Treat these as relational profiles rather than fixed quotas. Match the reference's distribution and hierarchy, not merely its raw object count.

- For a high-density reference, make every major landing composition comparably rich. Name the layer stack, repeated modules, patterns, overlaps, edge crops, outline or shadow treatment, and occupied regions. Do not let the final card or later shots collapse into a plain background.
- For a low-density reference, protect negative space and precise focal hierarchy. Do not add patterns, cards, sparkles, micro-labels, or decorative geometry merely to make the film feel finished.
- When adapting portrait art to landscape, redistribute density through side columns, cropped edge elements, wider typography, and foreground or background relays. Do not stretch the source layout or leave accidental empty bands.
- Separate visual density from simultaneous motion. A rich frame may retain many static or subordinate layers while only one to three carriers animate on a beat.

## 3. Analyze video references

When a style or motion reference is a video, inspect both its frames and its time behavior.

1. Use `ffprobe` to record duration, aspect ratio, frame rate, video stream, and audio presence.
2. Extract representative frames or contact sheets from the opening, every cut boundary, action or layout peaks, typography beats, transitions, and ending.
3. Derive the art style from those frames using the same medium, composition, geometry, typography, material, and density analysis used for still references.
4. Derive a temporal motion signature:
   - shot cadence and average hold length;
   - entry carrier, path, landing, hold, and exit carrier;
   - easing character, acceleration, deceleration, overshoot, bounce, or snap;
   - movement amplitude, speed, dominant direction, and local counter-movement;
   - camera movement, depth behavior, and parallax;
   - cut, wipe, mask, morph, panel, occlusion, or material-driven transition family;
   - typography entry, deformation, reflow, masking, hold, and exit;
   - background and supporting-layer persistence between beats;
   - climax construction and final-hold behavior;
   - visible audio synchronization when it materially shapes the motion.
5. Convert the signature into transferable rules. Do not copy the reference's characters, products, narrative, dialogue, visible copy, branding, exact shot sequence, exact frames, or soundtrack.

Prefer video evidence over still-frame inference for timing, easing, camera, and transitions. Use still frames from the same video to control art direction and visual density.

## 4. Infer material behavior

Motion should obey the implied material:

- Paper: tear, fold, flip, slide, overlap, tape, stamp.
- Ink or print: bleed, spread, overprint, misregister, press, reveal through halftone.
- Glass or transparent plastic: refract, split, slide by facets, focus, produce restrained caustics.
- Fabric: pull, fold, ripple, wrap, unveil.
- Pixel or digital UI: quantize, scan, cascade, tile, buffer, reorganize by modules.
- Hand drawing: draw on, retrace, erase, redraw, circle, underline.
- Liquid vector: melt, stretch, swell, splash, swallow, fold, recombine.
- Fine-line diagram: trace, calibrate, orbit, align, lock, unfold symmetrically.
- Metal or industrial product: scan contours, assemble panels, track details, wipe with hard highlights.

If the motion could be applied unchanged after replacing the medium, it is too generic.

## 5. Infer spatial tendency

- Grid composition → modular swapping, aligned slides, controlled reflow.
- Scroll or panoramic composition → continuous lateral travel and motif relay.
- Deep perspective → tunnel travel, scale inversion, portal or corridor transitions.
- Centered composition → convergence, radial expansion, impact from the center.
- Symmetrical composition → mirrored construction, calibration, ritual unfolding.
- Panel composition → frame replacement, nested windows, page logic.
- Whitespace-led composition → few precise moves, large negative-shape changes, strong reveal.

Choose one dominant direction or spatial tendency for continuity. Local counter-movements may appear only as brief anticipation or impact.

## 6. Infer tempo from visual weight

- Sharp angles and hard blocks favor impact, cutting, snap stops, and short holds.
- Rounded organic shapes favor elasticity, breathing, and continuous morphing.
- Fine lines favor tracing, precision, calibration, and layered reveals.
- Dense collage favors rapid panel changes with clear pose islands.
- Minimal luxury favors fewer moves, longer negative space, and one decisive reveal.

Slow does not mean static. Even ceremonial or minimal work should complete a structural change about every 0.8–1.8 seconds unless the final card is holding.

Do not convert these tendencies into equal shot lengths. Design a rhythm contour before assigning timestamps:

1. identify the style's implied attack, flow, weight, and breathing behavior;
2. choose a contour such as burst–hold–burst, accelerate–reset–climax, long setup–decisive reveal–long hold, elastic long–short–long, or another project-specific shape;
3. distribute short attacks, medium developments, longer pose islands, internal microbeats, and the final readable hold;
4. make cut intervals visibly non-uniform unless strict metronomic regularity is supported by the reference;
5. avoid reusing one timestamp skeleton across unrelated projects.

For still references, infer rhythm from visual evidence:

- sharp, heavy, high-contrast graphics suggest short attacks, hard stops, and asymmetric pauses;
- rounded or soft graphics suggest elastic long–short phrasing, continuous carries, and gentle deceleration;
- dense editorial or collage layouts suggest rapid module flurries separated by readable pose islands;
- sparse luxury layouts suggest a longer setup, one or two quick structural reveals, and confident holds;
- fine-line or diagrammatic work suggests staged traces, calibration beats, and precise locks;
- repeated grids may justify periodic rhythm, but introduce hierarchy through accent beats, grouping, or a contrasting hold rather than making the whole film flat.

These are evidence mappings, not presets. A 15-second film should normally contain at least one clear acceleration, deceleration, syncopated interval, breath, or tempo shift before the final hold.

Do not make a non-uniform rhythm by reducing shot changes. Set both a cut-interval contour and a shot-change budget from the reference:

- restrained, ceremonial, or minimal references may use roughly four to six distinct compositions, with continuous internal motion and one or two decisive changes;
- medium-energy character, product, or editorial references normally use roughly six to eight distinct compositions;
- dense, playful, collage, action-led, or high-energy references normally use roughly seven to ten distinct compositions, including one or more two- or three-shot acceleration bursts;
- treat these ranges as guidance, not quotas; increase or reduce them only when the reference's temporal evidence justifies it.

Add short shots where energy rises, new information arrives, a pose detail deserves emphasis, typography escalates, or a climax needs compression. Do not insert redundant cuts that show the same information.

## 6A. Bridge momentum across every cut

For each adjacent shot pair, define:

1. the outgoing carrier: camera pan, push, orbit, subject gesture, hair or cloth sweep, panel travel, shape expansion, typography stroke, foreground wipe, particle stream, or light direction;
2. its screen direction, speed, scale trend, rotation, and energy at the cut;
3. the incoming carrier that inherits, redirects, transforms, or absorbs that energy;
4. whether the bridge is a match-on-action, directional match, speed match, scale match, rotational match, shape morph, occlusion wipe, or impact-response cut.

Cut before the outgoing motion fully settles. Start the incoming shot already carrying compatible energy. Do not end one shot at rest and begin the next at rest. When the next action reverses direction, show a pivot, impact, anticipation, rebound, or counter-movement so the reversal feels motivated.

Breath beats reduce amplitude and information rate without stopping the film. Keep at least one continuity carrier alive through subtle camera drift, parallax, breathing, hair or cloth overlap, particles, light travel, background motif relay, or typography micro-motion. The final title or CTA may hold a stable layout, but supporting motion should decay gradually rather than freezing abruptly.

## 7. Build a project motion dictionary

Define:

- 6–12 allowed motion verbs;
- one dominant motion engine;
- one optional secondary engine;
- one dominant direction or spatial tendency;
- four to seven recurring motifs;
- four to eight explicit prohibitions.

Use roughly 70% dominant and at most 30% secondary behavior. Every shot must draw from this shared dictionary.

## 8. Match typography to motion

- Fashion or product typography: crop, collide, wipe, compress, mask the subject.
- Editorial collage typography: tile, repeat, swap panels, behave like paper blocks.
- Ritual or archival typography: fade with precision, align to axes, behave like labels or scales.
- Brutalist typography: slam, fracture, misalign, dominate the frame.
- Swiss typography: align, reorder by grid, slide with exact timing.
- Handwritten typography: draw, underline, circle, cross out, rewrite.

Do not animate every type family with the same scale-up and fade-in.

Build a typography motion dictionary alongside the project motion dictionary. For every important string, define:

- role: hero title, process headline, label, caption, data strip, transition carrier, or final lockup;
- hierarchy: font family, weight, scale, tracking, line spacing, alignment, outline, shadow, fill, and layer depth;
- entry: carrier, direction, path, easing, grouping level, and whether letters, words, lines, or blocks arrive together;
- construction: crop, repeat, tile, reorder, assemble, trace, stamp, stretch, compress, collide, mask, or reflow according to the reference;
- interaction: pass behind or in front of the subject, cut the frame into panels, reveal the subject, mask a transition, or respond to a graphic motif;
- lock: final position, spelling, readable hold length, and whether process text may remain partially cropped;
- exit: carrier, direction, transformation, or handoff into the next shot.

Important text should normally complete multiple meaningful stages before locking, but complexity must remain proportional to the reference. A minimal reference may use precise tracking changes, alignment, cropping, masking, and measured reordering; a dense reference may add repeated blocks, layered outlines, collisions, panel swaps, and foreground or background masking. Neither case is satisfied by a generic fade, uniform scale-up, or identical slide-in.

Coordinate motion by hierarchy. Animate a controlled subset of letters, words, lines, or blocks on each beat while the rest remain stable or subordinate. Synchronize text choreography with the approved rhythm contour and material behavior instead of adding independent decorative movement.

### Typography-presence rule

When deliberate typography or editorial layout is visible in a reference, treat it as structural motion evidence. Design type into most suitable shots and let it form masks, panels, crops, wipes, spatial divisions, or subject reveals. Do not postpone all typography to the final card. Keep the final title fully readable; process typography may be cropped or briefly obscured when that behavior matches the reference.

Route the overall dynamic type by the reference instead of applying one universal treatment:

- Editorial grid: reflow modules, crop headlines, swap cards, and realign columns.
- Manga or collage: replace panels, overlap paper blocks, relay captions, and use cutout travel.
- Minimal or luxury: use precise alignment, controlled whitespace changes, and few decisive reveals.
- Punk or print: tear, paste, stamp, misregister, photocopy-flicker, and collide type irregularly.
- Digital or interface: scan, cascade, quantize, buffer, reorganize modules, and lock data labels.
- Hand-drawn: write on, retrace, underline, circle, erase, and rewrite.
- Industrial or mechanical: assemble panels, scan contours, track scales, and snap labels to measured axes.
- Organic or liquid: stretch, melt, swallow, split, and recombine letterforms with the implied material.

These are routing examples, not reusable presets. Re-derive the exact verbs, density, tempo, and shot coverage from each supplied reference.

## 9. Example families, not presets

- Trend character or industrial product PV: hard kinetic type, pose-to-pose character beats, accent-color silhouette offsets, panel assembly, product detail tracking.
- Japanese manga collage: nested cards, panel replacement, repeated text walls, cutout travel, limited 2D parallax.
- Occult or Art Deco: symmetry, concentric orbits, light apertures, traced geometry, archival windows, luminous final reveal.
- Ink scroll: lateral travel, bleeding ink, growing line work, negative-space reveals, seal impact.
- Retro print: overprint shifts, halftone spread, page flips, stamp impacts.
- Y2K digital: scanning, cascading windows, pixel quantization, translucent refraction.
- Punk paste-up: tearing, tape pulls, photocopy flicker, irregular type collisions.
- Storybook: paper puppetry, stage flats, page turns, chapter reveals.
- Surreal collage: scale mismatch, image apertures, semantic shape matches, folded paper space.
- Minimal luxury: restrained precision, material glints, negative space, one strong unveil.

Invent a new family whenever the reference demands it.

## 10. Shot-writing requirement

For every macro beat, specify:

`staging → anticipation → entry carrier → pose or layout anchor → primary action → graphic response → secondary action → follow-through or overlap → settle and readable hold → exit transformation → next-shot carrier`

Avoid prompts that only describe mood, image content, or a generic camera move. Except for the final card, do not let a composition survive longer than about 1.5 seconds with only drifting, breathing, or a slow push.

## 11. Acceptance tests

Before generation, confirm:

- the motion is traceable to the reference's medium and composition;
- the visual-density profile matches the reference instead of defaulting to either minimalism or maximalism;
- complex references remain layered through the final card, while simple references retain intentional whitespace;
- static layer richness is not confused with simultaneous animation overload;
- video-derived timing, easing, camera, transition, typography choreography, layer persistence, and climax behavior match the approved temporal motion signature when a video reference exists;
- still-reference timing follows a deliberate style-derived rhythm contour rather than approximately equal shot spacing;
- cut times and internal microbeats create visible acceleration, breath, syncopation, or tempo contrast unless strict regularity is justified;
- Disney's Twelve Principles are applied across the complete motion system with intensity adapted to the reference's medium and tone;
- major beats have clear staging, anticipation, primary action, secondary response, follow-through or overlap, and settle;
- volume, anatomy, perspective, product geometry, typography spelling, and layer order remain solid through exaggeration and deformation;
- the typography behavior is style-specific;
- important typography has explicit role, hierarchy, entry, construction or transformation, interaction, readable lock, and exit behavior;
- typography complexity matches the reference and does not collapse into basic fades, uniform scaling, or repeated generic slide-ins;
- letter-, word-, line-, and block-level movement is coordinated hierarchically rather than all moving at once;
- prominent reference typography recurs through the film as designed motion and layout rather than appearing only on the end card;
- transitions are driven by visible motifs rather than generic dissolves;
- the subject anchor survives high-motion sections;
- at least one spatial or structural change occurs every 0.8–1.8 seconds;
