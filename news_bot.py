import os
import requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

def post_test_message():
    message = "✅ *Test Successful:* Your Software Engineering News Bot is connected and ready to go!"
    response = requests.post(SLACK_WEBHOOK_URL, json={"text": message})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    if not SLACK_WEBHOOK_URL:
        print("❌ Missing Slack webhook.")
    else:
        post_test_message()
