---
name: chn-house-style
description: Apply John's Christian History Nerd (CHN) house style for @ourdailyrice when researching, scripting, blocking, captioning, editing an episode, or preparing its TikTok video description. Use alongside the production tool's skill for implementation.
---

# CHN house style

Apply the established series style to the current episode. John's latest directions and the current footage/blocking script are authoritative. Episode-specific examples do not become universal requirements.

## Read the relevant guidance

- Research, evidence, sources or script writing: [research and scripts](references/research-and-scripts.md).
- TikTok video descriptions / short source lists for posting: [video description workflow](references/research-and-scripts.md#tiktok-video-description).
- Blocking, footage framing, sticker placement, title cards, quotation punctuation or ALL CAPS emphasis captions: [visuals and captions](references/visuals-and-captions.md).
- Recurring generated “Hey! I’m a Christian history nerd” opening, replacement/splice, speed or lip-sync fixes: read [generated opening](references/generated-opening.md) **before editing**.
- Red pulse, heartbeat, tension vignette or the **red pulse heartbeat effect**: read the [red pulse heartbeat effect](references/red-pulse-heartbeat.md) recipe for the combined visual/audio treatment, source asset, gain and synchronization across cuts.
- Cutting, speed, dialogue cleanup, music, SFX or loudness changes: [editing and audio](references/editing-and-audio.md).
- HDR/iPhone footage, HDR-to-SDR conversion, washed-out skin or color matching: [color management](references/color-management.md).
- HyperFrames scene organization, asset preparation or performance: [HyperFrames workflow](references/hyperframes-workflow.md), plus the available HyperFrames production skill. For scientific-notation export failures or rounding-induced extra timeline rows, read [timestamp precision](references/hyperframes-workflow.md#timestamp-precision-and-scientific-notation-export-errors).
- Any visual edit: inspect the relevant [CHN6–9 contact sheets and source-video references](references/reference-videos.md). The sheets and emphasis font are bundled; stills do not establish motion or audio timing.

Read only the references needed for the current task. A whole-episode edit needs visuals/captions, editing/audio and the applicable production workflow.

## Essential constraints

- **Blocking: bare 🎥 for each new pose/cut, with dialogue and visual/SFX cues nested underneath. No section labels or shot/angle descriptions unless explicitly requested.**
- **Every script and variant must be 130–160 spoken words, never more than 160. Count the complete spoken text before handoff; see [research and scripts](references/research-and-scripts.md).**
- Stickers are static by default: no animation or keyframes unless explicitly requested in the blocking script or chat. Use clip timing for reveals and keep placement/scale directly adjustable in the HF web UI.
- Preserve quotation boundaries and source-omission ellipses exactly as marked in the active blocking script, including across caption clips. See [visuals and captions](references/visuals-and-captions.md).
- Keep all text and the complete identifying title-card rectangles inside the inner 80% title-safe area. Check rendered/animated bounds with safe guides or coordinates; remove temporary overlays afterward.
- Check the actual dialogue waveform at every scene boundary and remove accidental lead-in/trailing silence; do not trust ASR start times alone. Keep all layers synchronized and ripple subsequent timing. See editing and audio.
- **Final-scene ending: when John walks off screen, keep the footage through his complete exit and cut when he is fully out of frame, not immediately after the last spoken word.** Inspect the video to locate that endpoint; preserve the walk-off even though the dialogue has ended. This takes precedence over the general trailing-silence trim rule.
- **Export or render a video only when John explicitly requests an export.** Editing, fixes, footage replacements and graphics updates do not authorize a preview-video or final-video export. Keep changes in the editable project/browser editor and use still snapshots for review until he requests an export.
- Keep original video footage in each episode’s `chn<x>/footage/` folder, with source manifests and scripts referencing that location. See editing and audio for the folder convention.
- Recorded framing stays native unless John explicitly requests a punch-in. Match the foreground matte to the footage. A requested punch zoom includes footage, foreground matte, stickers/title cards and captions together, plus the CHN whoosh; see [punch zooms](references/visuals-and-captions.md#punch-zooms).
- Inspect the CHN6–8 contact sheets for large, layered sticker scale and styling. Keep real footage beneath graphics. Place both stickers and their identifying title cards behind John’s aligned foreground matte; in seated shots use the space above his head and preserve the connection to the furniture.
- Match title-card text to the normal dialogue-caption font size, resizing the card to fit its text and line breaks.
- Vertically center the complete text block inside every title card, including multiline labels; see [visuals and captions](references/visuals-and-captions.md) for the layout implementation.
- Give introduced non-biblical people compact black identifying labels. Outside these criteria, do not add title cards unless John explicitly asks. ALL CAPS cues in the active blocking script become large NType82 Headline bold italic emphasis captions, fitted inside title-safe margins with the approved soft black shadow.
- **Recurring generated opening: original isolated dialogue is authoritative; mute generated audio and keep “Hey” through “nerd” as one continuous video. Align the video to the voice; do not apply the general `1.1×` default blindly or fix timing by splitting the shot/replacing the voice. Follow [generated opening](references/generated-opening.md), including playback with sound before claiming pace/lip-sync verification.**
- Default recorded talking heads to 1.1× with pitch and all layers synchronized, unless directed otherwise. Isolate dialogue through ElevenLabs Voice Isolator and retain original audio.
- Never use audio keyframes/time-varying automation. Use constant gain and explicitly requested native clip-edge fades; reuse John's approved settings. Source available SFX instead of programmatically synthesizing substitutes, and fit risers to their intended payoff.
- Keep scene layers independently editable inside shot-based sub-compositions, with spanning music at the root. Give clips semantic names. Images exceeding 16 MiB estimated decoded memory are resized proportionally to at most 8 MiB; preserve originals.
- Do not interact with HF Studio/the desktop app or its symlinks unless John asks. Use project files and the browser editor.

The episode copy at `/Users/johnamadeo/Desktop/content/chn9/chn-house-style.md` remains a readable project reference. This installed skill packages the approved conventions for reuse across episodes. Do not silently overwrite newer episode-specific decisions from this baseline. Maintain both the episode notes and relevant bundled reference when John explicitly asks to update the house style.
