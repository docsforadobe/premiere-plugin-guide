# Hardware Integration Components

## Importers

Importers are used whenever frames of video or audio from a clip are needed. To give Premiere Pro the ability to read media that uses a new format or codec, develop an importer. See [Importers](../importers/importers.md) for more information.

---

## Recorders

Users may choose a recorder in Project > Project Settings > General > Capture Format. Recorders are used to grab frames from a hardware source and write them to a file, to be imported for editing.

---

## Exporters

Exporters are used whenever Premiere Pro renders preview files, or performs an export on a clip or sequence. To give Premiere Pro the ability to write media that uses a new format or codec, develop an exporter. The exporter used to render preview files in the timeline is set in Sequence > Sequence Settings > Preview File Format. The exporter used for exports is chosen when the user selects File > Export > Media > File Type. See [Exporters](../exporters/exporters.md) for more information.

---

## Transmitters

A transmitter handles the display of video on any external A/V hardware and secondary output. To give Premiere Pro the ability to play video out to hardware for preview and final playout, write a transmitter. See [Transmitters](../transmitters/transmitters.md) for more information.
