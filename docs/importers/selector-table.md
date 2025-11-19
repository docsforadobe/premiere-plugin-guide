# Selector Table

Before implementing a handler for a certain selector, make sure that it is really necessary for your importer. Many selectors are optional, and only useful for certain special needs.

The Synth column indicates whether or not the selector is applicable to synthetic importers. Custom importers can respond to any of the selectors.

|                                      Selector                                       |                                        param1                                        |                                      param2                                      | Synth |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | ----- |
| [imInit](selector-descriptions.md#iminit)                                           | [imImportInfoRec\*](structure-descriptions.md#imimportinforec)                       | unused                                                                           | Yes   |
| [imShutdown](selector-descriptions.md#imshutdown)                                   | unused                                                                               | unused                                                                           | Yes   |
| [imGetIndFormat](selector-descriptions.md#imgetindformat)                           | `(int) index`                                                                        | [imIndFormatRec\*](structure-descriptions.md#imindformatrec)                     | Yes   |
| [imGetSupports8](selector-descriptions.md#imgetsupports8)                           | unused                                                                               | unused                                                                           | Yes   |
| [imGetSupports7](selector-descriptions.md#imgetsupports7)                           | unused                                                                               | unused                                                                           | Yes   |
| [imGetInfo8](selector-descriptions.md#imgetinfo8)                                   | [imFileAccessRec8\*](structure-descriptions.md#imfileaccessrec8)                     | [imFileInfoRec8\*](structure-descriptions.md#imfileinforec8)                     | Yes   |
| [imCloseFile](selector-descriptions.md#imclosefile)                                 | [imFileRef\*](structure-descriptions.md#imfileref)                                   | `(void*) PrivateData**`                                                          | No    |
| [imGetIndPixelFormat](selector-descriptions.md#imgetindpixelformat)                 | `(int) index`                                                                        | [imIndPixelFormatRec\*](structure-descriptions.md#imindpixelformatrec)           | Yes   |
| [imGetPreferredFrameSize](selector-descriptions.md#imgetpreferredframesize)         | [imPreferredFrameSizeRec\*](structure-descriptions.md#impreferredframesizerec)       | unused                                                                           | Yes   |
| [imSelectClipFrameDescriptor](selector-descriptions.md#imselectclipframedescriptor) | [imFileRef](structure-descriptions.md#imfileref)                                     | [imClipFrameDescriptorRec\*](structure-descriptions.md#imclipframedescriptorrec) | Yes   |
| [imGetSourceVideo](selector-descriptions.md#imgetsourcevideo)                       | [imFileRef](structure-descriptions.md#imfileref)                                     | [imSourceVideoRec\*](structure-descriptions.md#imsourcevideorec)                 | Yes   |
| [imCreateAsyncImporter](selector-descriptions.md#imcreateasyncimporter)             | [imAsyncImporterCreationRec\*](structure-descriptions.md#imasyncimportercreationrec) | unused                                                                           | Yes   |
| [imImportImage](selector-descriptions.md#imimportimage)                             | [imFileRef](structure-descriptions.md#imfileref)                                     | [imImportImageRec\*](structure-descriptions.md#imimportimagerec)                 | Yes   |
| [imImportAudio7](selector-descriptions.md#imimportaudio7)                           | [imFileRef](structure-descriptions.md#imfileref)                                     | [imImportAudioRec7\*](structure-descriptions.md#imimportaudiorec7)               | Yes   |
| `imResetSequentialAudio`                                                            | [imFileRef](structure-descriptions.md#imfileref)                                     | [imImportAudioRec7\*](structure-descriptions.md#imimportaudiorec7)               | Yes   |
| `imGetSequentialAudio`                                                              | [imFileRef](structure-descriptions.md#imfileref)                                     | [imImportAudioRec7\*](structure-descriptions.md#imimportaudiorec7)               | Yes   |
| [imGetPrefs8](selector-descriptions.md#imgetprefs8)                                 | [imFileAccessRec8\*](structure-descriptions.md#imfileaccessrec8)                     | [imGetPrefsRec\*](structure-descriptions.md#imgetprefsrec)                       | Yes   |
| [imGetEmbeddedLUT](selector-descriptions.md#imgetembeddedlut)                       | `(int) index`                                                                        | [imIndEmbeddedLUTRec\*](structure-descriptions.md#embeddedlutrec)                | Yes   |

The following selectors are optional, to provide custom file handling:

|                       Selector                        |                             param1                             |                            param2                            | Synth |
| ----------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------ | ----- |
| [imOpenFile8](selector-descriptions.md#imopenfile8)   | [imFileRef\*](structure-descriptions.md#imfileref)             | [imFileOpenRec8\*](structure-descriptions.md#imfileopenrec8) | No    |
| [imQuietFile](selector-descriptions.md#imquietfile)   | [imFileRef\*](structure-descriptions.md#imfileref)             | `(void*) PrivateData**`                                      | No    |
| [imSaveFile8](selector-descriptions.md#imsavefile8)   | [imSaveFileRec8\*](structure-descriptions.md#imsavefilerec8)   | unused                                                       | No    |
| [imDeleteFile](selector-descriptions.md#imdeletefile) | [imDeleteFileRec\*](structure-descriptions.md#imdeletefilerec) | unused                                                       | No    |

The following selectors are optional, for better support copying and trimming files using the Project Manager:

|                                 Selector                                  |                                       param1                                       |                              param2                              | Synth |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ----- |
| [imCalcSize8](selector-descriptions.md#imcalcsize8)                       | [imCalcSizeRec\*](structure-descriptions.md#imcalcsizerec)                         | [imFileAccessRec8\*](structure-descriptions.md#imfileaccessrec8) | No    |
| [imCheckTrim8](selector-descriptions.md#imchecktrim8)                     | [imCheckTrimRec\*](structure-descriptions.md#imchecktrimrec)                       | [imFileAccessRec8\*](structure-descriptions.md#imfileaccessrec8) | No    |
| [imTrimFile8](selector-descriptions.md#imtrimfile8)                       | [imFileAccessRec8\*](structure-descriptions.md#imfileaccessrec8)                   | [imTrimFileRec8\*](structure-descriptions.md#imtrimfilerec8)     | No    |
| [imCopyFile](selector-descriptions.md#imcopyfile)                         | [imCopyFileRec\*](structure-descriptions.md#imcopyfilerec)                         | unused                                                           | No    |
| [imRetargetAccelerator](selector-descriptions.md#imretargetaccelerator)   | [imAcceleratorRec\*](structure-descriptions.md#imacceleratorrec)                   | unused                                                           | No    |
| [imQueryDestinationPath](selector-descriptions.md#imquerydestinationpath) | [imQueryDestinationPathRec\*](structure-descriptions.md#imquerydestinationpathrec) | unused                                                           | No    |

The following selectors are used for embedded Closed Captioning support:

|                                           Selector                                            |                      param1                      |                                                 param2                                                 | Synth |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ----- |
| [imInitiateAsyncClosedCaptionScan](selector-descriptions.md#iminitiateasyncclosedcaptionscan) | [imFileRef](structure-descriptions.md#imfileref) | [imInitiateAsyncClosedCaptionScanRec\*](structure-descriptions.md#iminitiateasyncclosedcaptionscanrec) | No    |
| [imGetNextClosedCaption](selector-descriptions.md#imgetnextclosedcaption)                     | [imFileRef](structure-descriptions.md#imfileref) | [imGetNextClosedCaptionRec\*](structure-descriptions.md#imgetnextclosedcaptionrec)                     | No    |
| [imCompleteAsyncClosedCaptionScan](selector-descriptions.md#imcompleteasyncclosedcaptionscan) | [imFileRef](structure-descriptions.md#imfileref) | [imCompleteAsyncClosedCaptionScanRec\*](structure-descriptions.md#imcompleteasyncclosedcaptionscanrec) | No    |

The following selectors are optional, useful for a subset of importers:

|                                  Selector                                   |                                     param1                                     |                                        param2                                        | Synth |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ----- |
| [imAnalysis](selector-descriptions.md#imanalysis)                           | [imFileRef](structure-descriptions.md#imfileref)                               | [imAnalysisRec\*](structure-descriptions.md#imanalysisrec)                           | Yes   |
| [imDataRateAnalysis](selector-descriptions.md#imdatarateanalysis)           | [imFileRef](structure-descriptions.md#imfileref)                               | [imDataRateAnalysisRec\*](structure-descriptions.md#imdatarateanalysisrec)           | No    |
| [imGetTimeInfo8](selector-descriptions.md#imgettimeinfo8)                   | [imFileRef](structure-descriptions.md#imfileref)                               | [imTimeInfoRec8\*](structure-descriptions.md#imtimeinforec8)                         | No    |
| [imSetTimeInfo8](selector-descriptions.md#imsettimeinfo8)                   | [imFileRef](structure-descriptions.md#imfileref)                               | [imTimeInfoRec8\*](structure-descriptions.md#imtimeinforec8)                         | No    |
| [imGetFileAttributes](selector-descriptions.md#imgetfileattributes)         | [imFileAttributesRec\*](structure-descriptions.md#imfileattributesrec)         | unused                                                                               |       |
| [imGetMetaData](selector-descriptions.md#imgetmetadata)                     | [imFileRef](structure-descriptions.md#imfileref)                               | [imMetaDataRec\*](structure-descriptions.md#immetadatarec)                           | No    |
| [imSetMetaData](selector-descriptions.md#imsetmetadata)                     | [imFileRef](structure-descriptions.md#imfileref)                               | [imMetaDataRec\*](structure-descriptions.md#immetadatarec)                           | No    |
| `imGetRollCrawlInfo`                                                        | `imRollCrawlInfoRec*`                                                          | unused                                                                               | Yes   |
| `imRollCrawlRenderPage`                                                     | `rollCrawlRenderRec*`                                                          | unused                                                                               | Yes   |
| [imDeferredProcessing](selector-descriptions.md#imdeferredprocessing)       | [imDeferredProcessingRec\*](structure-descriptions.md#imdeferredprocessingrec) | unused                                                                               | No    |
| [imGetAudioChannelLayout](selector-descriptions.md#imgetaudiochannellayout) | [imFileRef](structure-descriptions.md#imfileref)                               | [imGetAudioChannelLayoutRec\*](structure-descriptions.md#imgetaudiochannellayoutrec) | Yes   |
| [imGetPeakAudio](selector-descriptions.md#imgetpeakaudio)                   | [imFileRef](structure-descriptions.md#imfileref)                               | [imPeakAudioRec\*](structure-descriptions.md#impeakaudiorec)                         | Yes   |
| [imQueryContentState](selector-descriptions.md#imquerycontentstate)         | [imQueryContentStateRec\*](structure-descriptions.md#imquerycontentstaterec)   | unused                                                                               | No    |
| [imQueryStreamLabel](selector-descriptions.md#imquerystreamlabel)           | [imQueryStreamLabelRec\*](structure-descriptions.md#imquerystreamlabelrec)     | unused                                                                               | Yes   |
| [imGetIndColorSpace](selector-descriptions.md#imgetindcolorspace)           | `(int) index`                                                                  | [imIndColorSpaceRec\*](structure-descriptions.md#imindcolorspacerec)                 | Yes   |

Used only in After Effects:

|                               Selector                                |                                     param1                                     |                                     param2                                     | Synth |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ----- |
| [imGetSubTypeNames](selector-descriptions.md#imgetsubtypenames)       | `(csSDK_int32) fileType`                                                       | [imSubTypeDescriptionRec\*](structure-descriptions.md#imsubtypedescriptionrec) | No    |
| [imGetIndColorProfile](selector-descriptions.md#imgetindcolorprofile) | `(int) index`                                                                  | [imIndColorProfileRec\*](structure-descriptions.md#imindcolorprofilerec)       | No    |
| [imQueryInputFileList](selector-descriptions.md#imqueryinputfilelist) | [imQueryInputFileListRec\*](structure-descriptions.md#imqueryinputfilelistrec) | unused                                                                         | No    |
