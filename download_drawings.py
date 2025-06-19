import os
import urllib.request

categories = [
    "apple", "bicycle", "cat", "tree", "clock",
    "star", "face", "flower", "pizza", "house"
]

os.makedirs("drawings", exist_ok=True)

base_url = "https://storage.googleapis.com/quickdraw_dataset/full/simplified/"

for category in categories:
    url = f"{base_url}{category}.ndjson"
    path = f"drawings/{category}.ndjson"
    try:
        print(f"Downloading {category}...")
        urllib.request.urlretrieve(url, path)
        print(f"✅ Saved to {path}")
    except Exception as e:
        print(f"❌ Failed to download {category}: {e}")
