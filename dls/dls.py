import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "DLSBOT")
    return r


def run_bot(r):
    subreddit = r.subreddit('cricket')
    for submission in subreddit.submissions():
        if "Match Thread" in submission.title:
            print(submission.title)
            k = submission.title.split(" ")
            team1 = k[2]
            print(team1)
        #    i = 3
        #    while k[i] != "vs" or i > len(k):
        #        team1+=k[i]
            #    i+=1
            #print(team1)


r = bot_login()
run_bot(r)
