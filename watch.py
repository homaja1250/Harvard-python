import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression to match the src attribute of an iframe
    match = re.search(r'src="(http[s]?://(?:www\.)?youtube\.com/embed/[^"]+)"', s)
    if match:
        # Extract the YouTube video ID from the embed URL
        embed_url = match.group(1)
        video_id = embed_url.split('/')[-1]
        # Return the shorter, shareable URL
        return f"https://youtu.be/{video_id}"
    return None

if __name__ == "__main__":
    main()
