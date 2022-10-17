# Write a Slack bot that
# Send a cat image every 5 minus
# Search cat image with inline command

import slack
import requests
import time


slack_Token = 'xoxb-4208909272770-4209010571954-XqwxkwLZIdzQw6l3MOBRkmsH'
try:
    while True:
        client = slack.WebClient(slack_Token)
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        data = response.json()
        client.chat_postMessage(channel='test', text = data[0]['url']) # get URL of cat image
        time.sleep(5) # Sleep 5 seconds and then do again
except:
    print("Disconnect!")
