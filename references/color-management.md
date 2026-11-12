## HDR footage and SDR color handling

CHN10’s first HDR-to-SDR preparation made John’s skin and white shirt look washed out. Correct the conversion from the original footage before trying to compensate with an exposure/contrast grade. Do not treat a technically valid file or correct color tags as proof that the picture looks right.

1. **Probe the original before converting.** Inspect pixel format, color primaries, transfer, matrix, range, Dolby Vision side data and rotation. CHN10’s original iPhone footage was HEVC `yuv420p10le`, BT.2020 primaries, `bt2020nc` matrix, HLG (`arib-std-b67`), limited range, with Dolby Vision profile 8 / compatibility ID 4 (HLG-compatible base layer), and a −90° display rotation. Do not assume every iPhone recording has these properties. Already-SDR Rec.709 assets, including reused intros, must not be tone-mapped again.
2. **Convert pixels, not just metadata.** For the inspected CHN10 HLG footage, the successful starting pipeline was linearization → floating-point RGB → Rec.709 primaries → Hable tone mapping → Rec.709 transfer/matrix and limited range → delivery pixel format. Merely assigning Rec.709 tags to HDR pixels is not a conversion. This base-layer workflow is not a claim to reproduce Dolby Vision’s dynamic-metadata rendering, and is not a universal preset for PQ or other HDR inputs.
3. **Use the working FFmpeg build.** On this machine `/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg` supports `zscale`; the plain PATH `ffmpeg` did not during this edit. Check filter availability rather than silently omitting color conversion. Keep source rotation/native framing, trims, frame count and approved speed intact.

CHN10’s tested filter chain:

```text
zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p
```

The corresponding encode used H.264 (`libx264`, CRF 18, `yuv420p`) and explicit `-color_primaries bt709 -color_trc bt709 -colorspace bt709` tags. `npl=100` belongs to this tested conversion, not an instruction to force all footage to a universal brightness. Retiming was a separate `setpts=PTS/1.1,fps=30` step with pitch-preserving audio handled separately.

4. **Compare representative stills before batch preparation.** Inspect the same moment from the source in a color-managed viewer, the SDR conversion, and the approved CHN references/contact sheets. Include skin, white shirt highlights, dark hair/blacks and bright windows; check both window-lit and interior setups. Look for lost shirt detail, lifted blacks, pale skin, clipped highlights or excessive darkening. Metadata and waveform checks support visual inspection; they do not replace it. Resolve the conversion first, then prepare the rest of the clips.
5. **Grade after conversion, once.** CHN10’s corrected conversion was followed by modest shot-specific exposure/contrast/black/highlight adjustments through HyperFrames’ native `media-treatment` controls. Preserve these as editable grades. Do not bake them into media and then apply them a second time, or copy one shot’s numeric grade to every lighting setup. Preserve originals and record the conversion and per-shot settings.
6. **Keep foreground mattes color-matched.** Generate the foreground from corrected footage, or reuse the existing alpha with corrected RGB only when frame count, timing, resolution and framing match exactly. CHN10’s repair decoded VP9 alpha with `-c:v libvpx-vp9`, extracted alpha, and merged it with corrected RGB. Apply the identical native grade and geometric transforms to the base footage and matching foreground; otherwise the presenter becomes a differently colored patch over the room. Inspect moving hair/hands and overlap frames.
7. **Verify the actual editor image.** Confirm the active scenes use the corrected assets; check the decoded SDR tags and inspect browser snapshots after grades and mattes are applied. Compare exported frames only when John explicitly requests an export. Do not export a preview or final video just to perform this check.

CHN10 implementation evidence: `outputs/chn10-hyperframes/work/correct-color.py`, `prepare-new-hook.py`, `color-correction.json` and `color-before-after.jpg` in the episode’s Codex workspace. These record the successful conversion and comparison; the previous washed-out assets were preserved separately.
