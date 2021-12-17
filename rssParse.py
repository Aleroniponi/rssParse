import sqlite3
import feedparser

# Connection to the db
connection = sqlite3.connect('rss.db')

# Parses the given rss feed
gitFeed = feedparser.parse('https://github.com/CapsAdmin/pac3/commits/master.atom') #Change to filepath

latestUpdate = gitFeed.feed.updated
latestChangeLog = gitFeed.entries[0].title
latestCommitId = gitFeed.entries[0].id

print("Time: " + latestUpdate)
print("Change: " + latestChangeLog)
print(latestCommitId)