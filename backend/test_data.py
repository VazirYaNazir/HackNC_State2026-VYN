import sys
import json
import time

# Tweak path to ensure we can import from the current directory
sys.path.append('.')

print("🔍 INITIALIZING SIMULATION FEED TEST...")
print("-" * 50)

try:
    # 1. IMPORT YOUR MAIN APP
    # This verifies that all imports (like ai_engine) are working
    from main import get_feed
    print("✅ Successfully imported backend.main")
    
except ImportError as e:
    print(f"❌ CRITICAL ERROR: Could not import main.py: {e}")
    print("💡 Make sure you are running this from the 'backend/' folder.")
    sys.exit(1)

# 2. RUN THE FEED GENERATION
print("🔄 Generating Feed & Running AI Analysis...")
start_time = time.time()

try:
    # This calls the exact same function your React Native app will hit
    feed_data = get_feed()
    
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    
    print(f"✅ Feed Generated in {duration} seconds.")
    print("-" * 50)

    # 3. INSPECT THE OUTPUT
    for post in feed_data:
        # Check if AI actually worked
        score = post.get('risk_score', 'N/A')
        flag = post.get('flag', 'N/A')
        
        print(f"📄 POST ID: {post['id']}")
        print(f"   User:    {post['username']}")
        print(f"   Caption: {post['caption'][:60]}...")
        print(f"   ❤️  Likes: {post['likes']}")
        
        # VISUAL CHECK FOR AI
        if score > 75:
            print(f"   🚨 RISK SCORE: {score} (HIGH RISK)")
        elif score > 0:
            print(f"   ⚠️ RISK SCORE: {score} (Moderate)")
        else:
            print(f"   ✅ RISK SCORE: {score} (Safe)")
            
        print(f"   🚩 FLAG: {flag}")
        print("-" * 30)

    # 4. JSON EXPORT (Optional)
    # Allows you to see the exact structure
    print("\n⬇️ RAW JSON SAMPLE (First Post):")
    print(json.dumps(feed_data[0], indent=4))

except Exception as e:
    print(f"❌ TEST FAILED: {e}")
    import traceback
    traceback.print_exc()