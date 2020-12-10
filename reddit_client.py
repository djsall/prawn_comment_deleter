# author: DjSall
# purpose: Script to delete comments under a certain karma threshold
# to use: create a creds.py, add a script app to your profile, where you will get the client ID, and client secret
# more info can be found in the prawn documentation

# this is how your creds.py should look like
# credentials = {
#   "client_id": "",
#   "client_secret": "",
#   "password": "",
#   "user_agent": "comment deleter by djsall",
#   "username": ""
# }

import praw
from creds import credentials as crd

reddit = praw.Reddit(client_id=crd["client_id"], client_secret=crd["client_secret"],
                     password=crd["password"], user_agent=crd["user_agent"], username=crd["username"])
me = reddit.user.me()
# if the username isn't outputted, your application is in read-only mode, so you won't be able to delete comments
print("Username:" + me)
counter = 0
for comment in me.comments.top("all"):
  if comment.score < 100:
    print(str(comment.score) + ": " + comment.body)
    counter += 1
    comment.delete()
    print("____deleted____")
print("deleted: " + str(counter) + " comments")
