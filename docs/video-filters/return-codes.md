# Return Codes

| **Return Code**      | **Reason**                                                                            |
|----------------------|---------------------------------------------------------------------------------------|
| `fsNoErr`            | Operation has completed without error.                                                |
| `fsBadFormatIndex`   | Return from `fsGetPixelFormatsSupported` when all pixel formats have been enumerated. |
| `fsDoNotCacheOnLoad` | Return from `fsCacheOnLoad` to disable plugin caching for this filter.                |
| `fsHasNoSetupDialog` | Return from `fsHasSetupDialog` to disable setup button in Effect Controls panel       |
| `fsUnsupported`      | The selector is not recognized, or unsupported.                                       |
