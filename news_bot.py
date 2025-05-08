import os
import requests

SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

def post_test_message():
    message = {
        "text": "✅ *Direct test:* Slack webhook is working via GitHub Actions."
    }

    if not SLACK_WEBHOOK_URL:
        print("❌ SLACK_WEBHOOK_URL is missing.")
        return

    print("✅ Webhook variable loaded.")
    response = requests.post(SLACK_WEBHOOK_URL, json=message)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

if __name__ == "__main__":
    post_test_message()
