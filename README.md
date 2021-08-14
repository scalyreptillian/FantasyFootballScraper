# Fantasy Football Scraper

This is a basic in-development python application that scrapes posts from http://www.reddit.com/r/fantasyfootball and a current list of players from http://www.footballdb.com.
All of this player data will then be stored into a SQLite database, where it can be compared against posts and comments.

What Works

reddit_scraper.py
 • Connects to Reddit through PRAW
 • For basic security, Reddit API login credentials-- client_id, client_secret, and user_agent-- are accessed through a text file

footballdb_scraper.py
 • Connects to any letter of the current player list on www.footballdb.com
 • Takes the player data table into a text file and cleans it up

database_controller.py
 • Connects to SQLite and creates a table in the database
 • Reads the data from organizedfootball.txt into the SQLite database

main.py
 • Imports controller/scrapers. Creates new database.
 • Loops through alphabet & collects current player information for each player
 • Sends the data to the database

Last updated 8/14/20
