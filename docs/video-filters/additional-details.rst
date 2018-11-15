.. _video-filters/additional-details:

Additional Details
################################################################################

Fields and Field Processing
================================================================================

In an interlaced project, Premiere calls your video filter once per field. This allows video filters to have interlaced motion. (*theData)->total will be twice as large, each frame will be half- height, and rowbytes will double.

Respect the value of rowbytes when traversing data or the output will be incorrect.

----

Frame Caching
================================================================================

The rendered output of video filters is stored in the host media cache. For example, when the user scrubs over a frame with a filter on it, the filter will be called to render its effect on the frame and return the buffer to Premiere. Premiere caches the returned frame, so when the user scrubs over the same frame, Premiere will return the cached frame without having to call the filter again. If the user has modified the filter settings, the clip settings, the preview quality, etc, Premiere will call the filter to render with the new settings, but will keep the previously cache frame for a while. So if the changes are reversed, Premiere may still have the cached frame to return when appropri- ate.

If the filter should generate random, non-deterministic output, or if it changes over time without keyframes, the randomness bit must be set in the ANIM_FilterInfo section in the PiPL (.r file). If you set the bit to noRandomness, Premiere will only render one frame of a still image.

----

Creating Effect Presets
================================================================================

Effect presets appear in the Presets bin in the Effects panel, and can be applied just like Effects with specific parameter settings and keyframes. Effect presets can be created as follows:

1) Apply a filter to a clip
2) Set the parameters of the filter, adding keyframes if desired
3) Right-click on the filter name in the Effect Controls panel, and select "Save Preset..."
4) Create preset bins if desired by right-clicking in the Effects panel and choosing "New Presets Bin"
5) Organize the presets in the preset folders
6) Select the bins and/or presets you wish to export, right-click, and choose "Export Preset"

On Windows, newly created presets are saved in the hidden Application Data folder of the user's Documents and Settings (e.g. C:\Documents and Settings\[user]\Application Data\Adobe\\ Premiere Pro\[version]\Effect Presets and Custom Items.prfpset). On Mac OS, they are in the user folder, at ~/Library/Application Support/Adobe/Premiere Pro/[version]/Effect Presets and Custom Items.prfpset.

Effect Presets should be installed as described in the section, "Plug-in Installation". Once they are installed in that folder, they will be read-only, and the user will not be able to move them to a dif- ferent folder or change their names. User-created presets will be modifiable.

----

Effect Badging
================================================================================

Starting in CS5, video filters now appear with badges in the Effects panel to advertise if they support YUV, 32-bit, and/or accelerated rendering. The user can filter the list of effects to show only the effects that support those rendering modes. Video filters will automatically receive YUV and 32-bit badges if they advertise support using the existing *fsGetPixelFormatsSupported*. Custom badges can also be created.

To add your own effect badge, go to the following folder:

On Windows: ``[App installation path]\Settings\BadgeIcons\\``

On Mac OS: ``Adobe Premiere Pro CS5.app/Contents/Settings/BadgeIcons/``

In that folder are the PNG graphics that are loaded at runtime for various badges, and an additional set of 'Sample-*.png' and 'Sample.xml' files.

1) Make copies of the Sample-*.png files, replacing the "Sample" prefix with the prefix that matches whatever you want to call the new badge (like 'NewBadge-*.png'). Edit the PNG as you'd like, but don't change the image dimensions.
2) Copy the Sample.xml file to a new name that matches whatever you want to call the new badge (like 'NewBadge.xml'). Edit the list of match names that you want to be decorated with your badge. Change the <Name> tag to the name you chose in step 1 (like 'NewBadge'). You can also add your tooltip text as the <DescriptionItem> tags. These tags act as a localization map with the langid as the key. If a language isn't found, 'en_US' is used by default. Provide your own GUID in the <Guid> tag.
3) Relaunch the application. You'll get a badge filter icon next to the others and a badge icons next to each effect that was listed in the XML file.

.. note::

  'Sample' is a special case that is intentionally excluded. Any other set of *.xml/*.png files will be used.

----

Premiere Elements and Effect Thumbnail Previews
================================================================================

Premiere Elements (but not Premiere Pro) displays visual icons for each effect. You will need to provide icons for your effects, or else an empty black icon will be shown for your effects, or even worse behavior in Premiere Elements 8. The icons are 60x45 PNG files, and are placed here:

[Program Files]\Adobe\Adobe Premiere Elements [version]\Plug-ins\Common\EffectPreviews\\

The filename should be the match name of the effect, which you specify in the PiPL, prefixed with "PR." So if the match name was "MatchName", then the filename should be "PR.MatchName.png"
