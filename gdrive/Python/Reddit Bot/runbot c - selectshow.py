import praw
import sys

#details
BotA = {'ClientID': 'FmFQgtKl41ehaQ',
        'ClientSecret': 'l9PvV_Pr10la_YsCWQN6PPXH_C0',
        'UserAgent': 'python3.6.1:darthplagueisbot:v1 (by /u/Sgp15)',
        'Username': 'darthplagueisbot',
        'Password': 'CoreHairSee62'}

Account = BotA

#initialise reddit object with details
reddit = praw.Reddit(client_id = Account['ClientID'],
                     client_secret = Account['ClientSecret'],
                     password = Account['Password'],
                     user_agent = Account['UserAgent'],
                     username = Account['Username'])

#active zone
##print('Select subreddit')
subreddit = reddit.subreddit('PrequelMemes')

#run bot
while True:
    for comment in subreddit.stream.comments():
        try:
            print(comment.body)
        except:
            print('ERROR')
            e = sys.exc_info()
            print(e)
            
