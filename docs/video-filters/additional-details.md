# Additional Details

## Fields and Field Processing

In an interlaced project, Premiere calls your video filter once per field.

This allows video filters to have interlaced motion. `(*theData)->total` will be twice as large, each frame will be half-height, and rowbytes will double.

Respect the value of rowbytes when traversing data or the output will be incorrect.

---

## Frame Caching

The rendered output of video filters is stored in the host media cache. For example, when the user scrubs over a frame with a filter on it, the filter will be called to render its effect on the frame and return the buffer to Premiere. Premiere caches the returned frame, so when the user scrubs over the same frame, Premiere will return the cached frame without having to call the filter again. If the user has modified the filter settings, the clip settings, the preview quality, etc, Premiere will call the filter to render with the new settings, but will keep the previously cache frame for a while. So if the changes are reversed, Premiere may still have the cached frame to return when appropriate.

If the filter should generate random, non-deterministic output, or if it changes over time without keyframes, the randomness bit must be set in the `ANIM_FilterInfo` section in the PiPL (.r file).

If you set the bit to noRandomness, Premiere will only render one frame of a still image.

---

## Creating Effect Presets

Effect presets appear in the Presets bin in the Effects panel, and can be applied just like Effects with specific parameter settings and keyframes. Effect presets can be created as follows:

1. Apply a filter to a clip
2. Set the parameters of the filter, adding keyframes if desired
3. Right-click on the filter name in the Effect Controls panel, and select "Save Preset…"
4. Create preset bins if desired by right-clicking in the Effects panel and choosing "New Presets Bin"
5. Organize the presets in the preset folders
6. Select the bins and/or presets you wish to export, right-click, and choose "Export Preset"

On Windows, newly created presets are saved in the hidden Application Data folder of the user's Documents and Settings (e.g. `C:/Documents and Settings/[user]/Application Data/Adobe Premiere Pro/[version]/Effect Presets and Custom Items.prfpset`). On MacOS, they are in the user folder, at `~/Library/Application Support/Adobe/Premiere Pro/[version]/Effect Presets and Custom Items.prfpset.`

Effect Presets should be installed as described in the section, "Plugin Installation". Once they are installed in that folder, they will be read-only, and the user will not be able to move them to a different folder or change their names. User-created presets will be modifiable.

---

## Premiere Elements and Effect Thumbnail Previews

Premiere Elements (but not Premiere Pro) displays visual icons for each effect. You will need to provide icons for your effects, or else an empty black icon will be shown for your effects, or even worse behavior in Premiere Elements 8. The icons are 60x45 PNG files, and are placed here:

`/[Program Files]/Adobe/Adobe Premiere Elements [version]/Plugins/Common/Effect/Previews/`

The filename should be the match name of the effect, which you specify in the PiPL, prefixed with "PR." So if the match name was "MatchName", then the filename should be "PR.MatchName.png"
