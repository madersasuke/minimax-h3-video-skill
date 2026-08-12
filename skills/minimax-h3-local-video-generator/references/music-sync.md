# BGM-led audiovisual choreography

Use this reference for every project with generated music. Treat the BGM as the primary temporal spine and the dominant non-verbal audio layer. Sound effects support selected visual events; they do not lead the mix or independently dictate the rhythm unless the user explicitly requests an effects-driven film.

## Uploaded BGM routing

When the user uploads a BGM, it replaces generated music and always becomes the exact temporal spine. Analyze the supplied signal rather than inventing a cue sheet from visual inference. Record duration, approved segment, BPM, meter, beat and onset positions, sections, phrase boundaries, fills, breaks, rises, drops, climax, and final cadence. Derive every cut and animation peak from this actual map.

Ask whether the BGM should also guide the complete artistic style:

- **No**: use the BGM for audio reuse, timing, energy, and synchronization only. Keep the approved style-image or style-video contract in control of rendering, composition, typography, motion materials, camera, transitions, and visual culture.
- **Yes**: use the BGM as the primary cross-modal style contract. Infer visual materials, geometry, density, typography personality, motion weight, camera energy, transitions, and editing behavior from its genre, era, cultural cues, instrumentation, timbre, texture, arrangement, articulation, groove, phrase spacing, dynamics, and emotional energy. Keep style images subordinate and use them only where compatible.

Attach the file as `<Audio 1>` through `LoadAudio` into `MiniMaxH3ReferenceToVideo.ref_audios.ref_audio_0`. Use full-reference prompting. Describe `fully_copy` for 1:1 reuse, `partially_copy` for an approved segment or edited reuse, and `reference` only when the user explicitly requests reinterpretation.

If the BGM duration differs from the target duration, do not silently crop, loop, stretch, or fade it. Obtain approval for the exact treatment before prompt approval and queueing.

## 1. Establish the audio hierarchy

Use this default priority:

1. BGM structure and musical continuity;
2. required dialogue or narration, when present;
3. selected hero sound effects;
4. low ambience and texture.

Keep the BGM clearly foregrounded across the complete film. Do not let repeated impacts, risers, whooshes, clicks, cloth sounds, or environmental transients mask its pulse, melody, bass movement, phrase changes, or final cadence.

## 2. Design the BGM before the visual timing map

Define one coherent musical system before assigning cut times:

- genre or production family derived from the approved visual style;
- tempo or narrow BPM range;
- meter and useful subdivision, such as quarter-note drive, eighth-note pulse, triplet swing, or syncopated sixteenths;
- two to four core instruments or sound sources with stable roles;
- a recurring rhythmic cell or bass pattern;
- phrase structure across the full duration;
- energy contour: pickup, establishment, build, breath or breakdown, climax, and final cadence;
- named musical accents for major reveals, impacts, title assembly, and final lock.

Avoid random instrument swaps, competing melodies, unnecessary genre changes, unrelated percussion fills, or a new musical idea at every shot. Changes in instrumentation must serve an explicit section change and preserve the established rhythm and tonal identity.

### Derive the music style from the visual reference

Use the approved style contract from `style-coherence.md`. Infer the music direction from the combined evidence rather than from a single color or a fixed lookup table:

- era and cultural cues constrain production family and instrument vocabulary;
- material and texture influence timbre, articulation, acoustic or electronic character, and surface treatment;
- visual density influences arrangement density and rhythmic detail;
- geometry and edge character influence attack, sustain, pulse shape, syncopation, and precision;
- composition and whitespace influence phrase spacing, rests, sustained tones, and breathing room;
- contrast and focal hierarchy influence accent strength, build, and climax placement;
- typography personality influences articulation, rhythmic grouping, repetition, and gesture scale;
- implied weight, elasticity, softness, aggression, playfulness, restraint, or ceremony influence BPM, groove, subdivision, dynamics, and cadence.

Write a brief evidence statement explaining why the selected music belongs to this reference. Reject arbitrary fashionable music and any score that would remain equally plausible with an unrelated style image.

## 3. Build a music cue sheet

Create a cue sheet before the shot timeline:

| Time | Music event | Visual event | Sync relationship | Supporting SFX |
|---|---|---|---|---|
| `00:SS.sss` | pickup, downbeat, snare, bass accent, fill, break, rise, drop, or cadence | cut, pose, gesture, camera peak, panel change, type assembly, reveal, or impact | exact hit, anticipation before hit, follow-through after hit, syncopated counterpoint, or sustained phrase | none or one subordinate sound |

Use the cue sheet to determine cut times and internal microbeats. Major actions follow musical phrasing:

- stage and anticipate during the pickup or pre-beat;
- land the main pose, cut, reveal, or typographic lock on the selected accent;
- continue follow-through and overlapping action across the following beat or sustain;
- place acceleration bursts over fills, denser subdivisions, or rising instrumentation;
- place breath beats over a musical breakdown or thinner arrangement while keeping visual motion alive;
- land the climax on the strongest planned musical event;
- let the final stable composition coincide with a clear cadence, sustained chord, or controlled tail.

Do not hit every beat with every layer. Assign different musical subdivisions to camera, subject, graphics, and typography, keep a clear hierarchy, and reserve full synchronization for deliberate hero accents. Visual anticipation may begin before the beat, but the intended impact or landing must coincide with the chosen musical event.

## 4. Preserve music continuity across cuts

Keep one continuous BGM performance across the entire 15-second film unless an intentional break or drop is part of the approved design. Cuts do not restart the music. Motion bridges between shots should inherit the BGM's ongoing pulse, phrase direction, and energy.

When a style-reference video contains audio, analyze only transferable timing evidence such as beat density, phrase length, accent placement, breakdown timing, and the relationship between music and visual events. Do not copy its melody, recording, lyrics, or soundtrack unless the user separately supplies and authorizes the audio.

## 5. Keep sound effects subordinate

Use only sound effects that clarify a hero action, material response, contact, transformation, or spatial transition. For a typical 15-second PV, prefer a small set of distinct hero effects rather than an effect on every cut.

- keep effects perceptually below the BGM;
- use short, clean transients with limited tails;
- avoid stacking impact, whoosh, riser, click, and texture on the same event;
- avoid identical loud impacts on successive cuts;
- keep ambience low and continuous rather than busy and foregrounded;
- do not duck or interrupt the BGM for ordinary effects;
- reserve the strongest effect for one or two genuine climax events.

## 6. Prompt translation

For generated music, compose the BGM plan first, then write the required H3 fields in their mandated order. In `non_diegetic_music`, use one to three information-dense English sentences to name instrumentation, tempo, pulse, phrase development, major accent timing, climax, final cadence, and the requirement for one coherent foreground score without random musical changes.

For uploaded BGM, use the Ref2VA six-section format and cite `<Audio 1>` consistently. Do not describe a replacement score. State whether the approved track is fully or partially copied, and map visual events to its actual timestamps.

In the visual timeline, connect each important cut, action peak, camera peak, graphic transformation, and typography lock to a named event in that BGM plan. In `overall_soundscape`, explicitly keep ambience and physical effects sparse, short, and subordinate beneath the score.

## 7. Acceptance tests

- the BGM is the clearest continuous non-verbal audio layer;
- its tempo, instruments, rhythmic cell, and tonal identity remain coherent;
- its genre family, timbre, instrumentation, arrangement density, rhythm, phrase spacing, dynamics, and cadence are traceable to the approved visual reference;
- major cuts, action landings, camera peaks, graphic changes, and type locks correspond to planned musical events;
- when beat or onset positions are measurable, deliberate exact-hit events land within roughly two frames at 24 fps; anticipation and follow-through may intentionally extend before and after the hit;
- anticipation begins before accents and follow-through continues after them;
- animation density follows musical density without making every layer hit every beat;
- sound effects do not overpower, clutter, restart, or fragment the BGM;
- the climax and final visual lock coincide with a clear musical climax and cadence;
- there are no unexplained music changes, competing grooves, or chaotic fills.
- uploaded BGM is connected to the H3 audio-reference input and not merely described in text;
- the user's audio-style-guide decision is respected without cross-contamination between timing-only and audio-led-art-direction modes.
