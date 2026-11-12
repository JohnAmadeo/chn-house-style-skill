# Red pulse heartbeat effect

Use this exact name when John requests the **red pulse heartbeat effect**. It means the combined red edge vignette and recorded heartbeat sound, synchronized for the requested tension/question beat. This recipe standardizes the existing CHN treatment; it does not add the effect automatically to every hook or rewrite older edits.

## Visual recipe

At 1080 × 1920, cover the canvas with a transparent-centered red vignette. Keep the actual footage, stickers and aligned foreground person visible underneath; captions stay above it. Use a timed, independently editable graphics wrapper (`z-index:40`, or an equivalent position above the presenter and below captions), `inset:0;pointer-events:none`. Animate its inner child, not the timed wrapper. Keep it outside any camera/punch-zoom container so the vignette remains attached to the screen edges.

```html
<div id="red-pulse-heartbeat" class="clip"
     data-start="0" data-duration="3" data-track-index="6"
     data-track-kind="graphics" data-timeline-label="Red pulse heartbeat effect · visual"
     style="position:absolute;inset:0;z-index:40;pointer-events:none"
     data-layout-ignore>
  <div id="red-pulse-heartbeat-inner" style="width:100%;height:100%;opacity:.25;
    background:radial-gradient(ellipse at center,rgba(255,0,0,0) 35%,rgba(255,0,0,.4) 58%,rgba(230,0,0,.95) 82%,#ff0000 100%);
    box-shadow:inset 0 0 170px 55px rgba(255,0,0,.95)"></div>
</div>
```

- Baseline opacity **0.25**, peak **0.50**. Each thump rises over **0.08 s**, then returns to baseline over **0.16 s**, with linear easing (`ease:"none"`). Retain the edge tint between thumps. Scale the shadow dimensions proportionally for other canvas sizes.
- Red is the default. CHN14's pink `#ff258a` love/heart-eye treatment is an episode-specific color variant, not the default. Desaturation, punch zooms, sticker movement, heart rain and risers are separate cues; the effect alone does not authorize them.

## Audio recipe

- Copy the bundled [audio-heartbeat-loop.mp3](../assets/audio-heartbeat-loop.mp3) into the project assets. It is the existing approximately 9.985 s CHN8/12/13/14 recording, not synthesized audio. SHA-256: `e69b8e5789bfbfe765ff7659d4fa30ecf87ce06547ac58a554185f4f2e28095b`.
- Original source: “Heartbeat Sounds effects No Copyright HD,” YouTube Sound Effects, https://www.youtube.com/watch?v=R2vb92bCKR0 . The original approximately 4.969 s file is also stored at `/Users/johnamadeo/Desktop/content/shared/audio-heartbeat-chn11.mp3` (SHA-256 `f348bce6ceda04c56ff72dba298a99b9f38884995e3171ca3bc1f6de59900f69`). The loop extends that recording; both have essentially the same source amplitude. Keep provenance with copied assets.
- Start a fresh tension passage at **source offset 1.0 s**, normal playback speed. Match the effect's visual and audio intervals. Use a separate, semantically named SFX clip with a stable ID, constant gain and editable source trim.
- **New default gain: 0.36**, twice the quieter legacy `0.18` treatment. This is a standardized starting level, not an instruction to overwrite existing tuned clips. Preserve John's current episode-specific gain when reusing an approved instance. CHN4 used `0.45`; CHN11 used `1.0`; CHN14 also used `0.45` for the pink variant. Do not blindly copy those louder values into every mix. Check speech intelligibility and combined peaks before handoff; the source itself has high decoded peaks.
- **Replace the jazz/music bed during the tension interval** unless John explicitly asks to layer it. Split or trim spanning music at both boundaries; preserve unrelated music outside the effect. Dialogue remains audible. Restore the intended bed on the release/reveal. Do not add volume keyframes or hidden automation; use constant gains and only requested native clip-edge fades.

```html
<audio id="red-pulse-heartbeat-audio" class="clip"
       src="assets/audio-heartbeat-loop.mp3"
       data-start="0" data-duration="3" data-media-start="1"
       data-hf-media-start-basis="local" data-volume="0.36"
       data-track-index="7" data-track-kind="audio" data-timeline-role="sfx"
       data-timeline-label="Red pulse heartbeat effect · heartbeat"></audio>
```

## Synchronize the thumps, including across cuts

**Follow the recording's paired thumps, rather than pulsing on an unrelated fixed timer.** CHN11 and CHN4 follow its uneven paired pattern; the later `0.66 s` visual loop is a legacy approximation that drifts from the sound. Use the paired pattern for new work, retaining the common vignette/opacity treatment.

The bundled [source timing metadata](../assets/red-pulse-heartbeat-source.json) contains approximate thump centers measured from 20 ms RMS windows. They are source-relative, not scene times. For source offset `1.0`, the first centers are approximately `0.16, 0.48, 1.17, 1.54, 2.21, 2.54, 3.18` seconds into the effect. Verify with sound at normal speed; a waveform measurement does not by itself prove perceptual sync.

For a timed passage starting at `effectStart` with source offset `sourceIn`, place each visual peak at `effectStart + sourcePeak - sourceIn`, starting its attack 0.08 s earlier. In a paused GSAP timeline, schedule finite attack/decay tweens on the inner div. Do not use CSS animation, wall-clock timers or infinite repeats. Keep a timeline hold through the effect end if required by the project's seek runtime, so repeated preview/scrubbing reaches the same settled state.

- If a cut falls within one continuing tension passage, **advance the audio source offset and preserve the visual pulse phase** in the next scene. CHN12 life-question → first-contact and investigate → dismiss, and CHN11 worry → Wright, provide existing examples of continuing the audio source.
- Calculate both scenes from one passage clock. If a cut falls inside an attack/decay, initialize the next scene's opacity to that exact phase and continue its remaining tween; do not restart at baseline or begin a new heartbeat. A new, separate tension passage may restart at source offset 1.0.
- Prefer one spanning audio clip at the root for a continuous passage across cuts, with scene-local visual wrappers calculated from the same absolute clock. If audio must be split, use contiguous source offsets and identical gains without overlap/gaps. Keep scene duration and all dialogue timing unchanged.
- The supplied loop is finite and its end is not guaranteed to be a seamless full heartbeat cycle. If the requested passage exceeds available source material, extend the recording at an inspected matching phase, retain provenance and remeasure the beat positions. Do not silently wrap at the file boundary or leave the last part silent.

## Review

Inspect a baseline frame, pulse peak and any cut inside the effect. Keep captions readable and footage visible, with the vignette covering the complete screen edges. Play with sound across the entrance, paired thumps, every seam and release; check that jazz is absent in the requested interval, heartbeat remains continuous and speech is clear. Use project/browser review and still snapshots; this effect does not authorize a video export. Do not claim listening verification from source markup or stills alone.

## Inspected precedents (11 November 2026)

Source compositions, audio offsets/gains and decoded waveform measurements were inspected; representative frames were extracted from existing exports. This audit did not include listening playback.

| Project | Existing implementation |
| --- | --- |
| CHN1 remake | No red pulse/heartbeat in active HyperFrames compositions. |
| CHN2 remake | No red pulse/heartbeat in active HyperFrames compositions. |
| CHN4 remake | `scene-hook.html`: common red vignette, paired source-aligned pulses, original recording at source offset 1, gain 0.45; jazz excluded. |
| CHN8 remake | `scene-question-one.html`: common red vignette, 0.66 s visual spacing, loop at source offset 1, gain 0.18; jazz starts afterward. |
| CHN11 | `scene-hook.html`, `scene-worry.html`, `scene-wright.html`: common red vignette, paired pulses, original recording gain 1.0; worry → Wright source offsets 1 → 1.7, jazz excluded during effect. |
| CHN12 | `scene-life-question.html`, `scene-first-contact.html`, `scene-investigate.html`, `scene-dismiss.html`: common red vignette, 0.66 s visual spacing, loop gain 0.18; contiguous audio offsets across paired scenes, jazz excluded. |
| CHN13 | `scene-question.html`, `scene-clues.html`: common red vignette and shorter separate tension beats, 0.66 s visual spacing, loop gain 0.18; no jazz over these beats. |
| CHN14 | `scene-meaning.html`: red at gain 0.18. `scene-pharaohs.html`: pink love variant at gain 0.45, beginning scene-local 2.706364; both use 0.66 s visual spacing. Jazz stops for each interval. |

CHN1/2/4/8/11/12/13 sources: `/Users/johnamadeo/Desktop/content/chn<N>/hyperframes/`. CHN14 source: `/Users/johnamadeo/Documents/Codex/2026-10-26/i-make-tiktok-content-on-https-2/outputs/chn14-hyperframes/`. These are evidence locations, not files to modify when applying the skill elsewhere.
