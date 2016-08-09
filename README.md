My script is small compared to the limitless thing you could do with 
nflgame api you can find more infomation on the page below.
https://github.com/BurntSushi/nflgame


nflgame is an API to retrieve and read NFL Game Center JSON data. It can work with real-time data, which can be used for fantasy football.

nflgame works by parsing the same JSON data that powers NFL.com's live GameCenter. Therefore, nflgame can be used to report game statistics while a game is being played.

The package comes pre-loaded with game data from every pre- and regular season game from 2009 up until the present (I try to update it every week). Therefore, querying such data does not actually ping NFL.com.

However, if you try to search for data in a game that is being currently played, the JSON data will be downloaded from NFL.com at each request (so be careful not to inspect for data too many times while a game is being played). If you ask for data for a particular game that hasn't been cached to disk but is no longer being played, it will be automatically cached to disk so that no further downloads are required.


