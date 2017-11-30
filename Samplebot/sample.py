import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "Sample Check- jontargaeryan ")
    return r


def run_bot(r):
    i=0
    for comment in r.subreddit('test').comments(limit=25):
        if "Dragon" in comment.body:
            i=i+1
            comment.reply("Valar Morghulis. [Here](https://imgur.com/r/gameofthrones/z8h1Pcn)")
    return i

r = bot_login()
print("There are ",run_bot(r)," instances of dragon")
