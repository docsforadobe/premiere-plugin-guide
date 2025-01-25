# Exporters

Exporters are used to export video, audio, and markers in any format. Exporters get individual video frames in a requested pixel format (generally, uncompressed video) and uncompressed audio. The exporter is responsible for any compression of the video and audio data, and wrapping the output in a file format. To reuse an existing exporter, you may provide an export controller.

Exporters can be used from within Premiere Pro, or from Adobe Media Encoder. From within Premiere Pro, go to the File > Export > Media dialog. From there, the Export Settings dialog appears. The format chosen in the Format drop-down determines the exporter used, and the exporter provides the parameter settings and summary displayed in the Export Settings dialog.

Exporters can optionally provide hardware acceleration by coordinating with a renderer plugin to render timeline segments. Legacy editing modes are formed by the combination of an exporter and a player; the exporter generates preview files and the player manages the cutlist.

If you’ve never developed an exporter before, you can skip [Whats New](whats-new.md#exporters-whats-new), and go directly to [Getting Started](getting-started.md#exporters-getting-started).
