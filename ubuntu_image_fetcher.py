import os
import requests
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    image_url = input("Please enter the image URL: ").strip()

    # Create the directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    try:
        # Attempt to fetch the image
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()

        # Try to get a filename from the URL
        parsed = urlparse(image_url)
        filename = os.path.basename(parsed.path)

        # Fallback filename if URL doesn't end with a file
        if not filename:
            filename = "image.jpg"

        file_path = os.path.join("Fetched_Images", filename)

        # Save the image in binary mode
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {file_path}")
        print("\nConnection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to fetch image: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

if __name__ == "__main__":
    main()
