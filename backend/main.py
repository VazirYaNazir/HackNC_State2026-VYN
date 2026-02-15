from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import time
import random
import ai_engine

app = FastAPI()

USE_MOCK_ONLY = True 

# --- 2. DATA MODELS ---
class PostData(BaseModel):
    id: str
    username: str
    image_url: str
    caption: str
    likes: int
    risk_score: int = 0
    flag: str = "Analyzing"

# --- 3. THE "GOLDEN" DATASET ---
# These posts cover all your edge cases: Safe, Scam, and Borderline.
def get_mock_feed():
    return [
        # SCAM 1: The obvious crypto scam
        {
            "id": "demo_scam_1",
            "username": "elon_giveaway_official",
            # Use a placeholder or a real hosted image you control
            "image_url": "https://placehold.co/600x600/red/white?text=BTC+GIVEAWAY", 
            "caption": "URGENT: Doubling all BTC sent to my wallet! Link in bio! 🚀🔴 #crypto #giveaway #tesla",
            "likes": 5200,
            "risk_score": 0, # AI will calculate this
            "flag": "Pending"
        },
        # SAFE 1: Standard Tech News
        {
            "id": "demo_safe_1",
            "username": "tech_crunch",
            "image_url": "https://images.unsplash.com/photo-1519389950473-47ba0277781c",
            "caption": "Breaking: OpenAI releases GPT-5 preview. The new model is 10x faster and safer. #ai #tech #future",
            "likes": 15400,
            "risk_score": 0,
            "flag": "Pending"
        },
        # SCAM 2: Phishing/Support Scam
        {
            "id": "demo_scam_2",
            "username": "instagram_support_team",
            "image_url": "https://placehold.co/600x600/orange/white?text=Acct+Locked", 
            "caption": "Your account has been locked due to suspicious activity. Click the link in our bio to verify your identity or your account will be deleted in 24 hours. 🔒",
            "likes": 45,
            "risk_score": 0,
            "flag": "Pending"
        },
        # SAFE 2: Lifestyle/Travel
        {
            "id": "demo_safe_2",
            "username": "travel_weekly",
            "image_url": "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1",
            "caption": "Top 10 destinations to visit in Switzerland this winter. 🏔️🇨🇭 #travel #wanderlust",
            "likes": 8900,
            "risk_score": 0,
            "flag": "Pending"
        }
    ]

# --- 4. MAIN ENDPOINT ---
@app.get("/feed")
def get_feed():
    print("⚡ Request received. Serving Simulation Feed...")
    
    # 1. Get the Raw Data
    feed = get_mock_feed()
    
    # 2. Run Real-Time Analysis
    analyzed_feed = []
    
    for post in feed:
        # Check if AI is available
        if ai_engine:
            try:
                print(f"   Running AI on post: {post['id']}...")
                risk_score = ai_engine.scan_post_caption(post["caption"])
                
                post['risk_score'] = risk_score
                
                # Logic to set the flag based on the score
                if risk_score > 75:
                    post['flag'] = "SCAM DETECTED"
                elif risk_score > 40:
                    post['flag'] = "Suspicious"
                else:
                    post['flag'] = "Safe"
                    
            except Exception as e:
                print(f"   ❌ AI Error: {e}")
                post['risk_score'] = -1
                post['flag'] = "AI Error"
        else:
            # Fallback if AI engine is missing
            post['risk_score'] = 0
            post['flag'] = "AI Offline"
            
        analyzed_feed.append(post)

    print("✅ Response sent to frontend.")
    return analyzed_feed