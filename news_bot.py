# replit: packages = ["feedparser", "requests"]
import feedparser
import requests

SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")  # Replace this with your actual URL

FEEDS = {
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "Google Developers": "https://developer.googleblog.com/atom.xml",
    "TechCrunch": "https://techcrunch.com/feed/"
}

KEYWORDS = ["software", "developer", "engineering", "programming", "open source", "api", "code", "devops", "framework"]

def find_relevant_articles():
    results = []
    print("🔍 Searching feeds for relevant stories...")
    for source_name, url in FEEDS.items():
        feed = feedparser.parse(url)
        print(f"Checking {source_name}...")
        for entry in feed.entries:
            title = entry.title.lower()
            summary = entry.get("summary", "").lower()
            if any(keyword in title or keyword in summary for keyword in KEYWORDS):
                formatted = f"*{source_name}*: <{entry.link}|{entry.title}>"
                results.append(formatted)
                print(f"✅ Found: {entry.title}")
                break  # Only one per source
        if len(results) == 3:
            break
    return results

def post_to_slack(messages):
    if not messages:
        print("❌ No relevant articles found. Sending fallback message...")
        fallback = "_No relevant software engineering news today. Check back tomorrow!_"
        response = requests.post(SLACK_WEBHOOK_URL, json={"text": fallback})
        print(f"Slack fallback status: {response.status_code}")
    else:
        message_text = "*Top Software Engineering News Today:*\n" + "\n".join(messages)
        print("📤 Posting to Slack...")
        response = requests.post(SLACK_WEBHOOK_URL, json={"text": message_text})
        print(f"Slack post status: {response.status_code}")

if __name__ == "__main__":
    articles = find_relevant_articles()
    post_to_slack(articles)
