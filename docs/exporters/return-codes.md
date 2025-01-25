<a id="exporters-return-codes"></a>

# Return Codes

| **Return Code**                             | **Reason**                                                                                                                              |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `exportReturn_ErrNone`                      | Operation has completed without error.                                                                                                  |
| `exportReturn_Abort`                        | User aborted the export.                                                                                                                |
| `exportReturn_Done`                         | Export finished normally.                                                                                                               |
| `exportReturn_InternalError`                | Return this if none of the other errors apply.                                                                                          |
| `exportReturn_OutOfDiskSpace`               | Out of disk space error.                                                                                                                |
| `exportReturn_BufferFull`                   | The offset into the buffer would overflow it.                                                                                           |
| `exportReturn_ErrOther`                     | The vaguer the better, right?                                                                                                           |
| `exportReturn_ErrMemory`                    | Out of memory.                                                                                                                          |
| `exportReturn_ErrFileNotFound`              | File not found.                                                                                                                         |
| `exportReturn_ErrTooManyOpenFiles`          | Too many open files.                                                                                                                    |
| `exportReturn_ErrPermErr`                   | Permission violation.                                                                                                                   |
| `exportReturn_ErrOpenErr`                   | Unable to open the file.                                                                                                                |
| `exportReturn_ErrInvalidDrive`              | Invalid drive.                                                                                                                          |
| `exportReturn_ErrDupFile`                   | Duplicate filename.                                                                                                                     |
| `exportReturn_ErrIo`                        | File I/O error.                                                                                                                         |
| `exportReturn_ErrInUse`                     | File is in use.                                                                                                                         |
| `exportReturn_IterateExporter`              | Return value from `exSelStartup` to request exporter iteration.                                                                         |
| `exportReturn_IterateExporterDone`          | Return value from `exSelStartup` to indicate there are no more exporters.                                                               |
| `exportReturn_InternalErrorSilent`          | Return error code from `exSelExport` to put a custom error message on screen just before returning control to the host.                 |
| `exportReturn_ErrCodecBadInput`             | A video codec refused the input format.                                                                                                 |
| `exportReturn_ErrLastErrorSet`              | The exporter is returning an error using the [Error Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-error-suite).    |
| `exportReturn_ErrLastWarningSet`            | The exporter is returning a warning using the [Error Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-error-suite).   |
| `exportReturn_ErrLastInfoSet`               | The exporter is returning information using the [Error Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-error-suite). |
| `exportReturn_ErrExceedsMaxFormatDuration`  | The exporter (or the host) has deemed the duration of the export to be too large.                                                       |
| `exportReturn_VideoCodecNeedsActivation`    | The current video codec is not activated and cannot be used.                                                                            |
| `exportReturn_AudioCodecNeedsActivation`    | The current audio codec is not activated and cannot be used.                                                                            |
| `exportReturn_IncompatibleAudioChannelType` | The requested audio channels are not compatible with the source audio.                                                                  |
| `exportReturn_IncompatibleVideoCodec`       | New in CS5. User tried to load a preset with an invalid video codec                                                                     |
| `exportReturn_IncompatibleAudioCodec`       | New in CS5. User tried to load a preset with an invalid audio codec                                                                     |
| `exportReturn_ParamButtonCancel`            | New in CS5.5. Return this from `exSelParamButton` if the user cancelled settings dialog by pressing cancel button.                      |
| `exportReturn_ErrMediaFormat`               | Error encountered writing to media format.                                                                                              |
| `exportReturn_ErrVideoEncoderCreation`      | Error encountered while creating video encoder.                                                                                         |
| `exportReturn_ErrAudioEncoderConfiguration` | Error encountered configuring audio encoder.                                                                                            |
| `exportReturn_ErrVideoEncoderConfiguration` | Error encountered configuring video encoder.                                                                                            |
| `exportReturn_ErrInvalidPixelFormat`        | Pixel format not compatible with output format.                                                                                         |
| `exportReturn_ErrOutputBuffer`              | Error creating output buffer.                                                                                                           |
| `exportReturn_ErrInputBuffer`               | Error accessing input buffer.                                                                                                           |
| `exportReturn_ErrAudioEncoder`              | Error encountered during audio encoding.                                                                                                |
| `exportReturn_ErrVideoEncoder`              | Error encountered during video encoding.                                                                                                |
| `exportReturn_ErrMuxer`                     | Error encountered during muxing.                                                                                                        |
| `exportReturn_ErrVersion`                   | Error encountered because of versions.                                                                                                  |
| `exportReturn_ErrColorSpace`                | Specified color space is not compatible with output format.                                                                             |
| `exportReturn_ErrVideoEncoderAdaptor`       | Error encountered using video encoding adaptor.                                                                                         |
| `exportReturn_ErrPixelBufferCreation`       | Error creating pixel buffer.                                                                                                            |
| `exportReturn_ErrPixelBufferLock`           | Error encountered locking buffer.                                                                                                       |
| `exportReturn_ErrPixelBufferPlanarFormat`   | Error encountered with pixel buffer planar format.                                                                                      |
| `exportReturn_ErrPixelBufferBytesMatch`     | Error encountered with byte matching, within pixel buffer.                                                                              |
| `exportReturn_ErrPixelBufferUnlock`         | Error encountered unlocking buffer.                                                                                                     |
| `exportReturn_ErrPixelBufferException`      | Error encountered; exception accessing buffer.                                                                                          |
| `exportReturn_ErrPixelBufferAppend`         | Error appending to pixel buffer.                                                                                                        |
| `exportReturn_Unsupported`                  | Unsupported selector.                                                                                                                   |
