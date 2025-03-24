from flask import Flask, render_template, request, redirect, url_for
import feedparser
import os
import math

app = Flask(__name__)

# Default RSS Feeds
RSS_FEEDS = {
    "CNN": "https://rss.cnn.com/rss/edition.rss",
    "NY Times": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
}

FEEDS_FILE = "feeds.txt"

def load_feeds():
    """Load user-added feeds from a dictionary format stored in a file."""
    if os.path.exists(FEEDS_FILE):
        try:
            with open(FEEDS_FILE, "r") as file:
                content = file.read()
                if content.strip():  
                    local_vars = {}
                    exec(content, {}, local_vars)  # Execute the file safely to load dictionary
                    return local_vars.get("RSS_FEEDS", {})  # Extract RSS_FEEDS dictionary
        except Exception as e:
            print(f"Error loading feeds: {e}")
    return {}  # Return empty if file doesn't exist or has issues


def save_feeds():
    """Save the user-added feeds in dictionary format to the file."""
    with open(FEEDS_FILE, "w") as file:
        file.write("RSS_FEEDS = {\n")  # Start dictionary format
        for name, url in user_feeds.items():
            file.write(f'    "{name}": "{url}",\n')  # Write each feed as key-value pair
        file.write("}\n")  # Close dictionary


user_feeds = load_feeds()

def fetch_news():
    news = []
    
    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        articles = [{"title": entry.title, "link": entry.link, "source": source} for entry in feed.entries[:5]]
        news.extend(articles)

    for source, url in user_feeds.items():  # Now using named user feeds
        feed = feedparser.parse(url)
        articles = [{"title": entry.title, "link": entry.link, "source": source} for entry in feed.entries[:5]]
        news.extend(articles)

    return news


@app.route("/", methods=["GET", "POST"])
def home():
    global user_feeds  

    if request.method == "POST":
        feed_name = request.form.get("feed_name").strip()
        feed_url = request.form.get("rss_url").strip()

        if feed_name and feed_url and feed_name not in user_feeds:
            user_feeds[feed_name] = feed_url  # Store with name as key
            save_feeds()  

    # Get the page number from the request
    page = request.args.get("page", 1, type=int)
    articles_per_page = request.args.get("articles_per_page", 6, type=int)

    news = fetch_news()
    total_articles = len(news)
    total_pages = math.ceil(total_articles / articles_per_page)
    
    # Paginate results
    start = (page - 1) * articles_per_page
    end = start + articles_per_page
    paginated_news = news[start:end]

    return render_template(
        "index.html",
        news=paginated_news,
        user_feeds=user_feeds,
        page=page,
        total_pages=total_pages,
        articles_per_page=articles_per_page
    )


if __name__ == "__main__":
    app.run(debug=True)