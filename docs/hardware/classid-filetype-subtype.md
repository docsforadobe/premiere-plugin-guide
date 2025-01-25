# ClassID, Filetype and Subtype

All plugin types that support media must identify unique classID, filetype, and subtype.

These are all four character codes, or 'fourCCs'.

| Identifier |                                                                                                                                                                Purpose                                                                                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filetype` | Identifies the plugin's associated file type(s). Plugins create lists of filetypes they support.                                                                                                                                                                                                                                      |
| `subtype`  | Differentiates between files of the same filetype. Identifies the codec or compression to be used.                                                                                                                                                                                                                                    |
| `classID`  | With the new editing mode system starting in CS4, the classID is far less important.<br/><br/>It is used as part of the identification for exporters in the Editing Mode XML.<br/><br/>And plugins may share information with most other plugins running in the same process using the [ClassData Functions](classdata-functions.md). |
