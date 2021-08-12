# This is a Python script that scrapes player names from the fantasy football subreddit,
# and it lists them from most to least mentioned.

import praw

# Client ID, secret, & user agent created on https://www.reddit.com/prefs/apps
# Reads necessary Reddit API access details from text document
userpass = open(r'userpass.txt', 'r')

with open('userpass.txt') as f:
    credential_list = f.read().splitlines()
        
# Creates a valid read-only Reddit instance
reddit = praw.Reddit(
    client_id=credential_list[0],
    client_secret=credential_list[1],
    user_agent=credential_list[2],
)

# Obtains a Subreddit instance
subreddit = reddit.subreddit('fantasyfootball')

for submission in subreddit.top(limit=10):
    print(submission.title)
    print(submission.score)
    print(submission.id)
    print(submission.url)
