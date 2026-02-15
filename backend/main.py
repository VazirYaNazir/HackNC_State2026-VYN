from pathlib import Path
import sys

# --- PATH SETUP ---
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import ai_engine
import feed_service
from src.googleapi import coords_to_geo
from src.xapi import get_posts_from_trends_as_real_tweets as get_trending_posts
from models import LocationData, PostData

app = FastAPI()

# --- 1. GLOBAL STATE ---
# We use this to store data between the POST and GET requests
newsData = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def root():
    return {"message": "Server is running"}

# --- FEED ENDPOINT ---
@app.get("/api/feed")
def get_feed():
    # This serves the Instagram-style feed (Mock + AI)
    return feed_service.generate_analyzed_feed()
    
# --- LOCATION ENDPOINT (The Fix) ---
@app.post("/api/submit-location")
async def receive_location(loc: LocationData):
    global newsData
    
    print(f"📍 RECEIVED COORDINATES: {loc.latitude}, {loc.longitude}")
    
    try:
        # 1. Convert Coords
        geo_location = coords_to_geo(loc.latitude, loc.longitude)
        print(f"🌎 Converted to Geo: {geo_location}")

        # 2. Call API (Store response first)
        response = get_trending_posts(geo_location, 10, 1)

        # 3. SAFETY CHECK (Critical Fix 2)
        # Check if response exists AND has the "posts" key
        if response and "posts" in response:
            newsData = response["posts"]
        else:
            newsData = [] # Clear old data if fails
            return {"status": "error", "message": "No data found for location"}

    except Exception as e:
        print(f"Error occurred while fetching trending posts: {e}")
        return {"status": "error", "detail": str(e)}

# --- NEWS GETTER ---
@app.get("/api/news")
def get_news():
    return newsData