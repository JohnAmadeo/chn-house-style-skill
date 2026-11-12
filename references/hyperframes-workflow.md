## Timeline organization

- **Give every clip a meaningful name visible in the editor timeline.** Avoid generic numbered labels such as “Audio 0” or “Hook Visual 1.” Use explicit display labels where the editor supports them, preserving internal IDs used by timing and animation references.
  - Audio: `Dialogue · <description>`, `Music · <description>` or `SFX · <description>` according to its role (for example, `Dialogue · John · isolated`, `Music · Swing jazz · body`, `SFX · Page turn`).
  - Video: `Video · <description>` (for example, `Video · Opening hook` or `Video · Seated source explanation`).
  - Images: `Sticker · <what the visual depicts>` (for example, `Sticker · Talmud`, `Sticker · Josephus` or `Sticker · Last Supper`).
- **Use one shot-based scene/sub-composition per main video clip and its associated layers.** Keep the footage, aligned foreground person matte, stickers/title cards, captions, dialogue and shot-specific SFX independently editable inside that scene. Consecutive segments of the same shot split only for speed changes may stay together.
- Keep the root timeline lightweight: scene hosts plus music clips that span scenes. Music stays at the root because it crosses scene boundaries. Drill into a scene to edit its individual layers.
- Name each scene `Scene · <the first few words of the script>…` so the spoken opening identifies it (for example, `Scene · Reading the Mekhilta…`).
- Convert timings to scene-local time without changing the finished edit. Preserve source trims, playback rates, footage/matte registration, stacking, caption synchronization, approved constant audio gains/native fades and visual animations. Split cross-cut SFX or other transitions at scene boundaries with continuous source offsets so each scene carries its portion. Do not introduce or perpetuate audio keyframes; the no-audio-automation rule governs audio.
- This scene-based approach supersedes the earlier preference to keep every individual clip on the main timeline. John reports that it has not noticeably improved playback on the root timeline, but drilling into a scene gives a smoother sub-timeline. Treat it as an editing/navigation benefit, not a proven cure for root playback lag.
- Minimize the number of tracks. Reuse a track for clips that do not overlap in time; do not create one track per asset or sound effect. For example, the sequential descending notes and stone rumble can share one sound-effects track.
- Add tracks only where simultaneous clips or independent layer/mix controls require them. Keep background footage and the aligned foreground person matte separate when needed for stickers behind John. Keep every clip independently editable; track consolidation must preserve timing, stacking, source trims, approved constant audio gains/native fades and visual animations.
## Image preparation and decoded-memory budget

- **Before adding an image to the edit, check its estimated decoded memory. If it exceeds 16 MiB, resize it proportionally to 8 MiB or less.** Apply this to paintings, photos, finished stickers, screenshots and other raster assets; audit existing referenced images when optimizing an episode.
- Estimate decoded memory using four bytes per pixel, based on pixel width and height, and use 1,048,576 bytes per MiB. This is a consistent budgeting estimate, not a measurement of actual browser/GPU memory. Use decoded pixel size rather than a compressed-file-size threshold: a smaller PNG/JPEG file can still decode into the same large bitmap.
- Preserve aspect ratio, transparency, sticker outlines and color appearance. Downsample with a high-quality resampler; round dimensions down to stay within the target. Do not crop or change an image's on-canvas position, display size, timing or animation merely to meet the budget. File compression may be applied additionally, but does not replace resizing.
- Keep untouched originals in a separate backup/source location outside the active asset set. Use optimized working copies in the project and keep a record of original/new dimensions and the backup location; do not repeatedly downsample an already optimized copy when regenerating it.
- This is a default asset-preparation rule that does not require knowing a sticker's eventual placement in advance. Allow a deliberate exception when a close crop or large zoom needs more detail; use the original to prepare that exception and inspect the actual frame.
- After replacement, verify the memory budget and transparency, run the project checks, and inspect representative rendered frames for sharpness, edges and crop fidelity. Check the largest/most zoomed use when applicable. Do not re-export the whole video unless requested.
- CHN9 observation: resizing the five oversized images to this budget reduced their combined estimated decoded memory from about 185 MiB to 40 MiB. John reported smoother playback afterward. This does not establish that images are the only source of timeline lag or impose a total-project memory cap.

## HyperFrames workspace boundary

- Work with project files and the browser editor. Do not launch or automate the HyperFrames desktop app / HF Studio, run `hyperframes open`, click “Open in desktop app,” or manage its registrations/symlinks/settings unless John explicitly requests it. John handles opening the app through the browser deeplink.

## Color preparation

- Before preparing HDR/iPhone footage, follow [color management](color-management.md). Probe the source, use the verified conversion for matching footage, compare stills before batch processing, and keep foreground matte colors matched to the base footage.

## Timestamp precision and scientific-notation export errors

### Prevent rounding drift

- Keep calculated edit boundaries in integer frames/ticks at the project frame rate, or use decimal arithmetic when preserving existing timings. Derive adjacent clips from the same boundary rather than independently rounding their start, end and duration. Preserve intentional sub-frame timing; do not snap the entire user-edited timeline to frames.
- Write time attributes as plain decimal strings, never scientific notation. For computed values intended to be zero, normalize residuals smaller than one microsecond to `0` before serialization. Do not clamp meaningful negative offsets or short durations.
- Check adjacent clip boundaries after a ripple edit. A nanosecond overlap can make HyperFrames display a clip on an extra row even when its `data-track-index` is unchanged. Fix the numerical boundary without moving the scene to another track or changing visible timing.

### Diagnose before changing media

- Verified with HyperFrames **0.8.223** during the CHN1 remake: internal arithmetic produced arguments such as `-3.33333360913457e-10` for FFmpeg `-ss` and FFprobe `-read_intervals`. Both rejected that notation. The renderer reported `VIDEO_SOURCE_UNRENDERABLE`, `invalid_media`, or `ffmpeg_failed` even though the source videos were valid.
- Inspect the underlying process stderr for `Invalid duration for option ss` or `Invalid interval start specification`. A successful browser preview or still snapshot does not prove the export path works. Changing codecs, re-encoding all footage, or switching FFmpeg builds alone does not fix this particular argument-formatting bug.

### Tested export workaround

- The bundled [FFmpeg wrapper](../scripts/ffmpeg-render-wrapper.py) and [FFprobe wrapper](../scripts/ffprobe-render-wrapper.py) format time arguments as fixed-point decimals and turn near-zero residuals into zero. They forward all other arguments to the full Homebrew binaries at `/opt/homebrew/opt/ffmpeg-full/bin/`. Check those binaries exist before use; update their paths for another machine. These wrappers change process arguments, not the approved edit or installed HyperFrames package.
- When this exact failure recurs, set **both** overrides for the authorized render invocation:

```sh
HYPERFRAMES_FFMPEG_PATH=/Users/johnamadeo/.codex/skills/chn-house-style/scripts/ffmpeg-render-wrapper.py \
HYPERFRAMES_FFPROBE_PATH=/Users/johnamadeo/.codex/skills/chn-house-style/scripts/ffprobe-render-wrapper.py \
node <project-pinned-hyperframes-cli> render <project> --quality delivery --output <requested-file.mp4>
```

- Overriding only FFprobe leaves the same error in FFmpeg. Passing plain decimals in authored HTML may still leave renderer-generated floating-point residuals, so check the actual subprocess arguments.
- Preserve the project-pinned HyperFrames version and user edits. After export, check duration, frame rate and audio, decode the complete output, and inspect representative encoded frames before reporting success. An export still requires John's explicit request.

