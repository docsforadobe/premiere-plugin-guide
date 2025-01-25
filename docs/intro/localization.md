<a id="intro-localization"></a>

# Localization

The language used by Premiere Pro is decided by the user during installation.

Plug-ins can determine this setting from the following locations:

On Windows, in the registry at `HKEY_CURRENT_USER\Software\Adobe\Premiere Pro\[version]`, in a key named `"Language"`.

On macOS, at `~/Library/Preferences/com.Adobe.Premiere Pro.[version].plist`, at `Root > Language`.

The string will be set to one of the values below by Premiere Pro at startup.

| **Language**                         | **String**   |
|--------------------------------------|--------------|
| English                              | `en_US`      |
| French                               | `fr_FR`      |
| German                               | `de_DE`      |
| Italian                              | `it_IT`      |
| Japanese                             | `ja_JP`      |
| Spanish                              | `es_ES`      |
| Korean                               | `ko_KR`      |
| Chinese (new in CC)                  | `zh_CN`      |
| Russian (new in CC 2014)             | `ru_RU`      |
| Brazilian Portugese (new in CC 2014) | `pt_BR`      |

Changing the string will not change the language Premiere Pro runs in, unless you override the application language by placing a file in the following location:

Windows: `[App installation folder]\lang-override.txt`

macOS: `[App Installation folder]/[Premiere Pro application package]/Contents/lang-override.txt`
