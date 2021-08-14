import database_controller
import footballdb_scraper
# import reddit_scraper
import string

database = database_controller
player_scraper = footballdb_scraper
# reddit_scraper = reddit_scraper

database.create_db()

for letter in string.ascii_uppercase:
    player_scraper.capture_from_url_ending_in(letter)
    database.write_player_data_to_db()

# player_scraper.capture_from_url_ending_in('C')
# database.write_player_data_to_db()