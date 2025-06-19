import json
import random

def load_sketch(category):
    with open(f"drawings/{category}.ndjson", "r") as f:

        lines = f.readlines()
    sample = json.loads(random.choice(lines))
    return sample['drawing']
