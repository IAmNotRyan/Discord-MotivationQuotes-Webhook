import praw
import random
import requests
import json


wh_url = "WebhookURL here"

#setup PRAW API
reddit = praw.Reddit(client_id = "API id",
                     client_secret = "API key",
                     username = "reddit username",
                     password = "reddit passwd",
                     user_agent = "user agent")


#find photos from redit and select random 
all_photos = []
subreddit = "GetMotivated"
subreddit = reddit.subreddit(subreddit)
topphotos = subreddit.top(limit = 150)
for submision in topphotos:
    all_photos.append(submision)
    quotes_image = random.choice(all_photos)
    quotesname = quotes_image.title

#discord embedment
webhook_data = {
  "username": "DailyMotivation",
  "avatar_url": "https://imgur.com/o5KUgVE",
  "embeds": [
    {
      "title": f"{quotesname}",
      "color": f"{random.randint(0, 0xFFFFFF)}",
      "image": {
        "url": f"{quotes_image.url}"
      }
    }
  ]
}

#post request to webhook url with embed data 
requests.post(wh_url, data=json.dumps(webhook_data), headers={'Content-Type':'application/json'})
