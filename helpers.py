from difflib import SequenceMatcher
import db

def trim_link(link):
    if "=" in link:
        return link.rsplit("=")[1].rsplit("?")[0].rsplit("&")[0].rsplit("#")[0]
    else:
        return ""
    
def search_by_title(search_term):
    results = db.select_videos_by_keywords(search_term.split())
    results.sort(reverse = True, key = lambda video: SequenceMatcher(None, search_term, video.title).ratio())
    return results