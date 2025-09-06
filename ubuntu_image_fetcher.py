import os
import requests
from urllib.parse import urlparse

def fetch_image(image_url):
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()

        parsed = urlparse(image_url)
        filename = os.path.basename(parsed.path) or "image.jpg"
        file_path = os.path.join("Fetched_Images", filename)

        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {file_path}")
        print("\nConnection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to fetch image: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls_input = input("Please enter image URLs separated by commas: ")
    image_urls = [url.strip() for url in urls_input.split(",")]

    os.makedirs("Fetched_Images", exist_ok=True)

    for url in image_urls:
        fetch_image(url)

if __name__ == "__main__":
    main()
