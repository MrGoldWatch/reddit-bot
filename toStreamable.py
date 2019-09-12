import praw
import re
import time

reddit = praw.Reddit(client_id='0x5WMM6iNQFunw',
                    client_secret='DbI0Rx5DviCgT2zdnrBEoHMnMa0',
                    user_agent='<console:to_streamable:0.0.1 (by /u/MrGoldWatch)',
                    username='ToStreamable',
                    password='testmain88')

print(reddit.read_only)

subreddit = reddit.subreddit('soccer') # Subreddit to get links from

# For testing
# print(subreddit.display_name)  # Output: redditdev
print(subreddit.title)         # Output: reddit Development
# print(subreddit.description)   # Output: A subreddit for discussion of ...