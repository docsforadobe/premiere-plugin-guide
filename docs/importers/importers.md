<a id="importers-importers"></a>

# Importers

Importers provide video, audio and/or closed captioning from the media source. This source can be a single file, a set of files, a communication link between another application, etc.

Standard importers appear as choices in the File > Import dialog, in the Files of type drop-down menu. Importers can support movies, still images, series of still images, and/or audio. If your importer provides enhanced support for a format already supported by another importer that ships with Premiere, set a high value in imImportInfoRec.priority to give your importer the first opportunity to handle the file.

Synthetic importers synthesize source material, rather than reading from disk. They appear in the File > New menu.

Custom importers are a special type of synthetic importer, implemented to better support titlers. Custom importers can create files on disk; synthetic importers don’t. Custom importers either create new media or import existing media handled by the importer. After the file is created, the media is treated like a standard file by the host application. Additionally, the media can be modified by the importer when the user double-clicks on it in the Project Panel.

| **Importer Type**   | **Reads from disk**   | **Creates clips**   | **Menu Location**        |
|---------------------|-----------------------|---------------------|--------------------------|
| Standard            | Yes                   | No                  | File > Import            |
| Synthetic           | No                    | Yes                 | File > New               |
| Custom              | Yes                   | Yes                 | File > New File > Import |

If you’ve never developed an importer before, you can skip [What’s New](whats-new.md#importers-whats-new), and go directly to [Getting Started](getting-started.md#importers-getting-started).
