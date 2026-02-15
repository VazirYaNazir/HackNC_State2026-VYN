from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import time
import random
import ai_engine

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USE_MOCK_ONLY = True 

# --- 2. DATA MODELS ---
class PostData(BaseModel):
    id: str
    username: str
    image_url: str
    caption: str
    likes: int
    risk_score: int = 0
    ai_image_probability: float = 0.0
    flag: str = "Analyzing"

class LocationData(BaseModel):
    latitude: float
    longitude: float
    # Optional: Add timestamp or user_id if needed
    # timestamp: Optional[float] = None 

# --- 3. THE MOCK DATASET ---
def get_mock_feed():
    return [
        # SCAM 1
        {
            "id": "demo_scam_1",
            "username": "elon_giveaway_official",
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlSP-QgB_POFLe9i3pdDlCabp4BYp0kfnIxA&s", 
            "caption": "URGENT: Doubling all BTC sent to my wallet! Link in bio! Spots sell out fast! 🚀🔴 #crypto #giveaway #tesla",
            "likes": 5200,
            "risk_score": 0,
            "ai_image_probability": 0.0,
            "flag": "Pending"
        },
        # SAFE 1
        {
            "id": "demo_safe_1",
            "username": "tech_crunch",
            "image_url": "https://images.unsplash.com/photo-1519389950473-47ba0277781c",
            "caption": "Breaking: OpenAI releases GPT-5 preview. The new model is 10x faster and safer. #ai #tech #future",
            "likes": 15400,
            "risk_score": 0,
            "ai_image_probability": 0.0,
            "flag": "Pending"
        },
        # SCAM 2
        {
            "id": "demo_scam_2",
            "username": "instagram_support_team",
            "image_url": "https://placehold.co/600x600/orange/white?text=Acct+Locked", 
            "caption": "Your account has been locked due to suspicious activity. Click the link in our bio to verify your identity or your account will be deleted in 24 hours. 🔒",
            "likes": 45,
            "risk_score": 0,
            "ai_image_probability": 0.0,
            "flag": "Pending"
        },
        # SAFE 2
        {
            "id": "demo_safe_2",
            "username": "travel_weekly",
            "image_url": "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1",
            "caption": "Top 10 destinations to visit in Switzerland this winter. 🏔️🇨🇭 #travel #wanderlust",
            "likes": 8900,
            "risk_score": 0,
            "ai_image_probability": 0.0,
            "flag": "Pending"
        }
    ]

# --- 4. MAIN ENDPOINT ---
@app.get("/api")
async def root():
    return {"message": "Hello World"}

@app.get("/api/feed")
def get_feed():
    feed = get_mock_feed()
    analyzed_feed = []
    
    for post in feed:
        if ai_engine:
            try:
                print(f"Running AI on post: {post['id']}...")
                risk_score = ai_engine.scan_post_caption(post["caption"])
                ai_image_probability = ai_engine.get_ai_image_probability(post["image_url"])
                post['risk_score'] = risk_score
                post['ai_image_probability'] = ai_image_probability

                if risk_score > 75:
                    post['flag'] = "SCAM DETECTED"
                elif risk_score > 40:
                    post['flag'] = "Suspicious"
                else:
                    post['flag'] = "Safe"
                    
            except Exception as e:
                print(f"AI Error: {e}")
                post['risk_score'] = -1
                post['flag'] = "AI Error"
        else:
            post['risk_score'] = 0
            post['flag'] = "AI Offline"
            
        analyzed_feed.append(post)

    return analyzed_feed

@app.post("/api/submit-location")
async def receive_location(loc: LocationData):
    print(f"RECEIVED COORDINATES: {loc.latitude}, {loc.longitude}")
    # Here you can add logic to store the location or use it elsewhere.
    return {
        "message": "Location received",
        "latitude": loc.latitude,
        "longitude": loc.longitude
    }

@app.get("/api/get-image")
def getImage():
    """
    This is the endpoint for 
    sending the twitter images to the frontend.
    """
    return

@app.get("/api/get-news")
def getNews():
    """
    This is the endpoint for 
    sending the twitter news to the frontend.
    """
    return