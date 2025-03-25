Github URL: https://github.com/anushiyairru/morning_dashboard.git

Architecture:


Flask (Python) backend handles data processing, RSS feed parsing, and routing.

HTML, CSS, JavaScript frontend provides the UI for users to view and interact with news feeds.

Feedparser is used to fetch RSS feed data from external sources.

Local storage (a text file) is used to persist user-added RSS feeds.

Features:



RSS Feed Management: 
Preloaded Feeds: CNN and NYTimes feeds are available by default.  
User-Added Feeds: Users can add custom RSS feeds, which persist between sessions.

News Display & Pagination:
News Grid Layout: Articles are displayed in a visually appealing grid.
Pagination: Users can navigate between multiple pages of articles.
Adjustable Articles Per Page: Users can select how many articles they want to view at once.

Dark Mode Toggle
Local Storage Persistence: Dark mode preference is saved in localStorage so it remains active after refreshing the page.

Responsive Design
Desktop View: 3 columns (3x2 layout).
Tablet View: 2 columns (2x4 layout).
Mobile View: 1 column (1x5 layout).

Flask Backend Functionality
Fetches and Parses RSS Feeds using feedparser.
Stores User-Added Feeds in a Local File (feeds.txt).
Handles GET and POST Requests:
GET retrieves news and renders the page.
POST adds a new RSS feed.
