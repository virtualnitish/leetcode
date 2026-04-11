import subprocess
import shutil
import os
import re
import urllib.request
import urllib.error
from datetime import datetime

# Optional: For robust Cloudflare bypass if standard urllib fails
# To use: uv pip install curl_cffi beautifulsoup4
try:
    from curl_cffi import requests as requests_cffi
except ImportError:
    requests_cffi = None

def check_copyq():
    return shutil.which("copyq") is not None

def get_user_agent():
    return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def fetch_leetcode_title(url):
    """Fetches the problem title from LeetCode URL."""
    print(f"Fetching metadata from {url}...")
    try:
        # Standard urllib attempt first
        headers = {"User-Agent": get_user_agent()}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response:
            html = response.read().decode('utf-8')
            
            # Extract title from <title> tag
            match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
            if match:
                title_text = match.group(1).replace(" - LeetCode", "").strip()
                return title_text
    except Exception as e:
        print(f"Standard fetch failed: {e}")
        
        # Fallback to curl_cffi if available
        if requests_cffi:
            try:
                print("Attempting with curl_cffi...")
                resp = requests_cffi.get(url, impersonate="chrome110", timeout=10)
                match = re.search(r"<title>(.*?)</title>", resp.text, re.IGNORECASE)
                if match:
                    return match.group(1).replace(" - LeetCode", "").strip()
            except Exception as e2:
                print(f"curl_cffi fetch failed: {e2}")

    return None

def convert_to_filename(number, title):
    clean_title = title.lower().replace(" ", "_")
    # Remove special characters
    clean_title = re.sub(r'[^a-z0-9_]', '', clean_title)
    padded_number = str(number).zfill(4)
    return f"{padded_number}.{clean_title}.md"

def create_template(number, title):
    return f"""# {number}. {title}

```python
# Solution for {title}
```

1. **Core Trick**: 

2. **Time & Space Complexity**:
   - **Time Complexity**: O()
   - **Space Complexity**: O()


- Python Tips:
"""

def copy_to_clipboard(text):
    if not check_copyq():
        return
    try:
        subprocess.run(["copyq", "copy", text], check=True)
        print(f"Filename '{text}' copied to clipboard.")
    except subprocess.CalledProcessError:
        print("Failed to copy to clipboard. Make sure CopyQ is running.")

def main():
    if not os.path.exists("python"):
        os.makedirs("python")

    print("--- LeetCode Solution Bootstrapper ---")
    print("Enter 'exit' to quit.")
    print("Inputs supported:")
    print("1. '1. Two Sum'")
    print("2. 'https://leetcode.com/problems/two-sum/'")
    
    while True:
        user_input = input("\nTitle or URL: ").strip()
        if user_input.lower() == 'exit':
            break
        if not user_input:
            continue

        problem_number = None
        problem_title = None

        # Check if URL
        if user_input.startswith("http"):
            problem_title = fetch_leetcode_title(user_input)
            if not problem_title:
                print("Could not fetch title automatically.")
                problem_title = input("Please enter the title manually: ").strip()
            
            # Try to see if title has number or ask
            num_match = re.match(r"^(\d+)\.\s*(.*)", problem_title)
            if num_match:
                problem_number = num_match.group(1)
                problem_title = num_match.group(2)
            else:
                problem_number = input("Enter problem number: ").strip()
        else:
            # Handle "Number. Title"
            match = re.match(r"^(\d+)\.\s*(.*)", user_input)
            if match:
                problem_number = match.group(1)
                problem_title = match.group(2)
            else:
                print("Invalid format. Use 'Number. Title' or a URL.")
                continue

        filename = convert_to_filename(problem_number, problem_title)
        filepath = os.path.join("python", filename)

        if os.path.exists(filepath):
            print(f"Warning: File {filepath} already exists.")
            overwrite = input("Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                continue

        with open(filepath, "w") as f:
            f.write(create_template(problem_number, problem_title))
        
        print(f"Successfully created: {filepath}")
        copy_to_clipboard(filename)

if __name__ == "__main__":
    main()
