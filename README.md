# Fantasy Football Scraper

This is a basic in-development python application that scrapes posts from http://www.reddit.com/r/fantasyfootball and a current list of players from http://www.footballdb.com.
All of this player data will then be stored into a SQLite database, where it can be compared against posts and comments.

What Works

reddit_scraper.py
 • Connects to Reddit through PRAW
 • For basic security, Reddit API login credentials-- client_id, client_secret, and user_agent-- are accessed through a text file

footballdb_scraper.py
 • Connects to letter 'A' of the current player list on https://github.com/scalyreptillian/FantasyFootballScraperwww.footballdb.com
 • Takes the player data table into a text file and cleans it up (leaves square brackets)

database_controller.py
 • Connects to SQLite and creates a table in the database

Last updated 8/13/20
