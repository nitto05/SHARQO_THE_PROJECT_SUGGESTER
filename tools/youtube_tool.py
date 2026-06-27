import requests
from dotenv import load_dotenv
import os

load_dotenv()   # Loads variables from .env

# youtube_key = os.getenv("YOUTUBE_API_KEY")
api_key = os.getenv("YOUTUBE")

# api_key = get_api_key("YOUTUBE")

base_url = "https://www.googleapis.com/youtube/v3/search"

def get_youtube_videos(query):

    params = {
        "part" : "snippet",
        "q" : query,
        "maxResults" : 10,
        "type" : "video",
        "key" : api_key
    }

    print(base_url)
    print(params)

    try:

        response = requests.get(base_url, params = params)
        
        response.raise_for_status()
        data = response.json()
    except Exception as e:

        return f"Unable to fetch any Youtube videos...\n {e}"
    if "items" not in data or len(data["items"]) == 0:
        return "No videos found..."

    seen = set()
    
    video_data = ""

    for video in data["items"]:
        video_id = video.get("id", {}).get("videoId")

        if video_id in seen:
            continue
        seen.add(video_id)

        snippet = video.get("snippet", {})

        title = snippet.get(
            "title", 
            "Unknown"
        )

        channelTitle = snippet.get("channel", "Unknown")

        published = snippet.get("publishedAt", "Unknown")

        description = snippet.get("description", "No description available.")

        if len(description) > 300:
            description = description[:300] + "..."

        thumbnails = snippet.get("thumbnails", {})

        # high = thumbnails.get("high", {})

        # thumbnail = high.get("url", "N/A")

        thumbnail = (
            thumbnails.get("high")
            or thumbnails.get("medium")
            or thumbnails.get("default")
            or {}
        ).get("url", "N/A")

        video_link = (f"https://www.youtube.com/watch?v={video_id}")

        video_data += f"""

Title : {title}
Channel : {channelTitle}
Published : {published}

Description : 
{description}

Thumbnail : 
{thumbnail}

Watch : 
{video_link}

"""
        video_data += "\n"
        video_data += "=" * 50
        video_data += "\n\n"
    
    return video_data

