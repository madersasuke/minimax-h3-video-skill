# Production specification

## Local configuration

- ComfyUI URL: `http://127.0.0.1:8188` by default; override with `--server`.
- T2VA template: pass `--template-png` or set `MINIMAX_H3_T2VA_TEMPLATE`.
- Text-only FL2VA UNET: `minimax_h3_fl2va_pruned_int8_convrot.safetensors`.

The user must install compatible MiniMax H3 checkpoints, ComfyUI nodes, and a known-good workflow separately. Model weights and workflow exports are not included in this repository.

The template PNG contains the known-good ComfyUI API graph in its `prompt` metadata, but its embedded UNET value is stale and points to Ref2VA. `scripts/queue_t2va.py` must overwrite that value with `minimax_h3_fl2va_pruned_int8_convrot.safetensors` for every no-character-reference text-only job. Preserve the remaining loader and decoder nodes.

## Mandatory generation routing

| Character input | Prompt mode | UNET route | Reference handling |
|---|---|---|---|
| No character reference | T2VA three-field text prompt | FL2VA: `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | Style images and videos are analysis-only |
| One or more approved character references | Ref2VA six-section prompt | Ref2VA checkpoint in the local reference graph | Attach and label approved character assets; keep style assets analysis-only unless explicitly authorized |

Do not use Ref2VA solely because style-reference images or videos exist. Do not submit a character-reference project through `scripts/queue_t2va.py`. Before queueing, expose the selected route and UNET in the confirmation or dry-run output.

## Default generation parameters

| Parameter | Default |
|---|---|
| Mode | T2VA |
| Duration | 15 seconds |
| Aspect ratio | `16:9 (Widescreen)` |
| Resolution budget | 0.8 MP |
| Frame rate | 24 fps |
| Sampler | `euler` |
| Scheduler | `beta` |
| Steps | 10 |
| Output codec | H.264 MP4, `yuv420p` |
| CRF | 19 |
| Audio | H3 generated audio included |
| Concurrency | one generation at a time |

Changing duration, aspect ratio, megapixels, or steps requires explicit confirmation. Randomize the seed for every creative variant. Do not lower the default to 0.6 MP without approval.

## Intake defaults

If the user gives only theme and style, assume:

- 15-second promotional or title-sequence structure;
- 16:9 landscape delivery;
- one clip unless multiple variants are requested;
- 0.8 MP and 10 steps;
- sound design and instrumental music generated in H3;
- no narration, dialogue, or subtitles unless requested;
- final cover generated after clip approval;
- no final assembly for a single successful clip.

## Variant matrix

Build a table before writing multi-clip prompts. Use one row per variant and fill every column.

| Variant | Spatial system | Hero motion | Typography layout | Camera logic | Transition family | Motif | Climax/end card |
|---|---|---|---|---|---|---|---|
| A | radial | orbital/swinging | curved type | fisheye arc | iris/ring wipe | web rings | circular lockup |
| B | editorial grid | panel-to-panel | asymmetric columns | snap zoom + truck | panel shutters | crops/rules | modular title grid |
| C | diagonal | pursuit/slash | steep vertical stack | chase tracking | diagonal cuts | arrows/speed bars | split diagonal lockup |

Examples are structural, not mandatory. Invent project-specific rows. Each pair of variants must differ in at least four columns.

## Fifteen-second arc

Use these macro functions in a style-derived order and duration rather than as fixed equal sections:

1. iconic hook and style declaration;
2. subject, world, or product reveal;
3. development or capability escalation;
4. optional breath, pose island, reset, or contrast beat;
5. climax or transformation;
6. stable title, product, logo, or CTA hold.

Build a new rhythm map and shot-change budget for every project. Mix short attacks, medium developments, moving holds, internal microbeats, and strategically added short-shot bursts according to the reference's visual weight and implied material behavior. Do not reuse fixed timestamps, place every cut in the same narrow duration range, or make rhythm irregular by reducing shot changes. Include at least one meaningful acceleration, deceleration, syncopated interval, breath, or tempo contrast unless the reference clearly demands strict regularity.

For a 15-second film, use roughly four to six distinct compositions only for restrained or deliberately slow references, six to eight for medium-energy work, and seven to ten for dense, playful, editorial, action-led, or high-energy work. Treat these as reference-driven guidance rather than quotas. A longer shot may contain several visible microbeats, while an acceleration burst may contain two or three short successive shots. Keep the final readable layout stable for at least 1 second while subtle supporting motion remains alive.

## Quality-preserving motion rules

- Give each action a clear start pose, readable path, and landing pose.
- Cut while the outgoing camera or element motion still carries energy, and let the incoming camera, subject, shape, panel, typography, foreground wipe, particle stream, or light direction inherit, redirect, transform, or absorb it.
- Define screen direction, speed, scale trend, or rotational energy across every adjacent shot pair. Avoid rest-to-rest cuts and unmotivated direction reversals.
- Treat breath beats, pose islands, and title locks as reduced-amplitude moving states rather than complete stops. Preserve a subtle continuity carrier and let motion decay gradually.
- Stage every major action with a readable setup, anticipation, primary action, secondary response, follow-through or overlap, and settle. Compress or expand these phases to match the approved rhythm rather than giving them equal duration.
- Apply Disney's Twelve Principles across the complete motion system with style-appropriate intensity. Treat them as design logic, not as a demand for literal cartoon deformation.
- Use pose-to-pose control for identity, anatomy, product geometry, typography locks, and critical layouts; reserve straight-ahead motion for suitable secondary materials such as hair, fabric, particles, ink, liquid, light trails, or loose graphic accents.
- Use slow in and slow out, arcs, timing contrast, secondary action, and controlled exaggeration to make motion feel intentional. A straight path or constant speed must be justified by mechanical, grid-based, or deliberately metronomic style logic.
- Preserve solid construction during motion: character volume and anatomy, product proportions, perspective, typography spelling, and layer order must remain coherent through anticipation, deformation, overlap, and impact.
- Maintain appeal at every hero pose and final lock: silhouettes, focal hierarchy, facial expression, product readability, typography composition, and negative space should remain intentional.
- Avoid demanding a close-up face, complicated limb interaction, rapid camera roll, dense parallax, and large text reveal simultaneously.
- Use silhouette frames, MG wipes, foreground occlusion, impact frames, or motivated cuts at the hardest pose transitions.
- Keep the principal subject large enough to read during hero beats.
- Limit isolated flashes and inversions to named beats; forbid uncontrolled continuous strobing.
- Treat exact typography as a held layout, not a texture spread across a deforming action shot.
- Let process typography perform style-matched multi-stage entry, assembly, masking, reflow, or transformation before reaching a readable lock.
- Coordinate typography by letter, word, line, and block hierarchy; do not animate every glyph simultaneously.
- Repeat stable identity, costume, product, and color anchors where continuity matters.

## Output layout and naming

Create one directory per project:

```text
<project-root>/
├── brief/
├── references/
├── prompts/
├── generations/
├── review/
├── edit/
└── cover/
```

Use stable ASCII slugs:

```text
<project>_v01_<concept>
<project>_v02_<concept>
```

Store the prompt as `<slug>.txt` and set the ComfyUI filename prefix to the same slug under a project folder.

## Queue and crash safety

1. Verify ComfyUI responds before submission.
2. Inspect both running and pending queues.
3. Submit one job, record `prompt_id`, and verify it appears in `queue_running` or `queue_pending`.
4. Do not submit six heavy jobs concurrently on the 12GB GPU.
5. Monitor GPU utilization, temperature, VRAM, and history without disturbing the running job.
6. Treat sustained 100% GPU use as expected when progress events continue.
7. If the job errors, capture the error and stop; never auto-queue the remaining batch blindly.
8. Preserve the user's existing virtual-memory configuration. More virtual memory may prevent a crash but does not accelerate sampling.

## QA checklist

### Technical

- output exists and is non-zero length;
- duration matches the brief within practical encoder tolerance;
- expected aspect ratio and resolution;
- 24 fps unless approved otherwise;
- both video and audio streams present;
- no truncated tail or missing final frame.

### Visual

- style DNA remains stable;
- Disney's Twelve Principles are visibly represented across the overall motion system, with intensity and deformation adapted to the approved style rather than applied as a uniform cartoon preset;
- major actions have readable staging, anticipation, primary action, follow-through or overlap, and settle, while secondary actions support rather than compete with the focal action;
- motion uses deliberate timing, slow in and slow out, and arcs where appropriate; straight paths, constant-speed moves, or abrupt stops are retained only when the style or material clearly justifies them;
- connected layers do not all start, peak, and stop simultaneously unless a deliberate impact or graphic lock requires synchronization;
- exaggeration strengthens clarity and appeal without breaking identity, anatomy, object geometry, perspective, typography spelling, or layer order;
- hero poses, product views, title locks, and transitions preserve solid construction, readable silhouettes, focal hierarchy, and visual appeal;
- visual density matches the reference's low, medium, or high complexity profile;
- complex references preserve background, middle-ground, subject, and foreground richness through the final card;
- simple references preserve intentional whitespace without gratuitous filler decoration;
- supporting detail remains mostly static or subordinate instead of creating simultaneous motion overload;
- when a style-reference video exists, generated cadence, holds, easing, direction, camera behavior, transition mechanics, typography choreography, layer persistence, and climax structure match its approved temporal motion signature;
- when only still references exist, cut intervals and internal microbeats follow a deliberate style-derived rhythm contour;
- shot spacing is not approximately uniform unless strict metronomic regularity is justified by the reference;
- rhythm variation does not come from simply reducing the number of shots;
- the shot-change budget matches the reference's energy and density, with additional short shots or two- to three-shot bursts at justified acceleration, escalation, reveal, or climax beats;
- every cut introduces new information and bridges an outgoing motion carrier into an incoming camera or element motion;
- adjacent shots preserve compatible direction, speed, scale, rotation, or impact response, and any reversal has a visible pivot, anticipation, rebound, or counter-movement;
- ordinary cuts are not rest-to-rest, and the overall film has no obvious dead pauses;
- breath beats, pose islands, readable locks, and the final card keep subtle camera, parallax, material, particle, light, background, or typography motion alive;
- the film contains a readable acceleration, deceleration, syncopation, breath, or tempo contrast before the final hold;
- typography animation matches the reference's material, geometry, visual density, layout, and rhythm;
- important text has explicit entry, construction or transformation, interaction, readable lock, and motivated exit;
- process typography participates in masks, panels, crops, transitions, spatial divisions, or subject reveals where appropriate;
- type motion does not collapse into basic fades, uniform scale-ups, identical slide-ins, or an end-card-only treatment;
- letter-, word-, line-, and block-level movement remains hierarchically controlled and readable;
- no unauthorized character, product, narrative, dialogue, visible copy, logo, watermark, exact frame, or soundtrack is copied from a style-reference video;
- focal subject is readable during movement;
- anatomy or object geometry does not collapse;
- no unexplained subject duplication;
- exact copy is correct and legible;
- palette stays within the approved hierarchy;
- transitions are motivated and beat-aligned;
- flashes are intentional and non-continuous;
- final hold is long enough to read;
- no accidental watermark, unrelated logo, or random letters.

### Batch

- every promised variant exists;
- variants differ on at least four design axes;
- filenames, prompts, and outputs map one-to-one;
- failed or rejected variants are clearly marked and not delivered as finals.
