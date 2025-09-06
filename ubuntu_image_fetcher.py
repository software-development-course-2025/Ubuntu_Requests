import os
import requests
from urllib.parse import urlparse

def fetch_image(image_url):
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()

        # Check if Content-Type is image/*
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped: URL does not point to an image ({content_type})")
            return

        # Optional: Check for large files (>10MB for example)
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > 10_000_000:
            print(f"✗ Skipped: Image too large ({int(content_length)/1_000_000:.2f} MB)")
            return

        parsed = urlparse(image_url)
        filename = os.path.basename(parsed.path) or "image.jpg"
        file_path = os.path.join("Fetched_Images", filename)

        if os.path.exists(file_path):
            print(f"↪ Skipped (already exists): {filename}")
            return

        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {file_path}")
        print("\nConnection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to fetch image: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

de
