# Splicing the recurring generated CHN opening

Use this workflow for the recurring overhead/book-floor “Hey! I’m a Christian history nerd” clip. It is a replacement visual for an established recorded performance. Follow it before applying the general talking-head speed or silence-trimming defaults.

## Keep the original performance authoritative

- Use John’s original recorded, isolated dialogue as the audio and timing reference. Preserve its approved speed, pitch, source trim, pauses, constant gain and complete words. If that dialogue has already been cleaned, reuse it; do not process it again just because the visuals changed.
- Mute the generated clip’s audio. A prompt asking Higgsfield to preserve audio does not establish that its output actually preserves John’s voice, pace or wording. Do not substitute generated speech, isolate it and call that the original dialogue.
- Keep the generated opening as **one continuous video clip and one scene** from “Hey” through “nerd.” Do not cut between “Hey” and “I’m,” delete the intervening motion, or independently retime fragments to fit a previously split placeholder.
- Preserve the generated shot’s composition and orientation. Crop only its unused lead-in/tail as supported by the original performance; do not add a freeze-frame inside the spoken introduction.

## Start from the existing working edit

Read the actual CHN9 setup before rebuilding this opening:

`/Users/johnamadeo/Desktop/content/chn9/dual-engine/chn9-hf/compositions/scene-01-hey.html`

Its implementation uses:

- One generated video, source offset `0`, playback rate `1.4473684210526`, scene duration `2.5333333333333` seconds.
- Original dialogue: `assets/dialogue-isolated-110.wav`, source offset `0`, duration `2.401` seconds, constant gain `0.63`.
- The generated video is muted; original dialogue is a separate audio clip.
- Caption groups: `Hey` at `0.1`; `I’m a` at `1.2333333333333`; `Christian history nerd` at `1.6666666666667` seconds.

These are a concrete reference, **not universal speed/gain/timing presets for every new generation**. CHN11’s replacement had matching generated-speech timestamps, so the CHN9 setup was reused in its saved correction. That correction is not user-approved merely because the files were saved. Do not copy CHN9’s legacy audio keyframes; retain the current episode’s approved constant gains/native fades.

## Align the replacement without changing the voice

1. Identify the original dialogue’s actual “Hey,” “I’m,” “Christian,” “history,” and “nerd” timing and the end of its final consonant. Inspect the waveform and listen; ASR timestamps only assist.
2. Inspect the new generated clip at those same spoken/mouth landmarks. Account for a lead-in, a silent/frozen tail, and any speed already baked into an asset.
3. Adjust the **continuous video’s** source in-point and one playback rate to follow the authoritative audio. Reuse the established setup when the source timing matches. Do not blindly apply the normal `1.1×` talking-head default, double-apply a baked speed, slow the voice, or change the audio duration to make an arbitrary video trim fit.
4. If one offset/rate cannot align both the beginning and the end, the generation may have changed the performance timing. Diagnose that drift explicitly; do not hide it with a jump cut, generated-audio substitution, or an unannounced pacing change.
5. Keep the established continuous opening’s timing when replacing its visuals. A split placeholder is not the timing authority. If a correction requires restoring the established duration, ripple all following scenes, captions, music and SFX together, preserving their relative timing and music source offsets. State the duration change.

## Verify the thing that actually failed

Play the complete opening **with sound**, including the cut into the next spoken line. Compare the original delivery and replacement at normal playback speed: the voice must retain its pace/pitch, the video must remain continuous, and mouth movements must follow the same words through “nerd.” Check captions and the outgoing cut too.

A contact sheet, passing layout check, duration/codec probe or successful decode cannot establish correct pace or lip sync. Report exactly what was checked; do not label playback/listening verified if it was not performed. Save for browser review if that check is unavailable.

Keep source provenance, original dialogue, generated source, source in/out, effective playback rate and scene duration in the episode notes. **Do not export until John explicitly requests it; a pending replacement must be spliced in before an authorized export starts.**
