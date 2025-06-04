from yt_dlp import YoutubeDL
import os
import subprocess

def download_video(url):
    output_dir = "downloads"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # creating folder by os
    
    # Create Options
    ydl_opts = {
        'quiet': False,
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'no_check_certificate': True,
        'format': 'best'
    }
    
    # Create instance
    with YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"🔄 Downloading video from {url}...")
            ydl.download([url])
            print(f"✅ Download completed: saved in '{output_dir}'")
        except Exception as e:
            print(f"❌ Download failed: {e}")
            
    # Automatically call download.sh for moving files into their respective folders
    try:
        subprocess.run(["./scripts/./download.sh"], check=True)
        print("✅  Downloaded videos sorted successfully by extension and date.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to sort downloaded videos: {e}")
            
if __name__ == "__main__":
    video_url = input("Enter the video URL to download: ")
    download_video(video_url)