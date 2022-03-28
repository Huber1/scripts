## BingSearchOff
Just run the `bing_search_off.reg` file, then log off and on again to turn off Bing search in the start menu of Windows 10/11.
This should also stop Windows from sending every search to Microsoft, thus your searches stay private

There is a Warning that you shouldn't trust unknown registry files. You can safely ignore that, but if you're feeling unsafe, there's an explanation below.

### Explanation

#### [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search]
For Windows 10, doesn't work on Windows 11 anymore, but no problem if exists anyway
- `BingSearchEnabled` -> false
- `CortanaConsent` -> false

#### [HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Explorer]
For Windows 11, might also be needed in future Win-10 Updates
- `DisableSearchBoxSuggestions` -> true
