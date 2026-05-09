import os
import subprocess
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.http import MediaFileUpload

# --- CONFIGURATION ---
VIDEO_FILE = "arsenal_short.mp4"
HTML_FILE = "index.html"
CLIENT_SECRETS = "client_secrets.json"
# ---------------------

def upload_and_integrate():
    # 1. YouTube Upload Logic
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    request_body = {
        "snippet": {
            "title": "AI ARSENAL DROP", 
            "description": "Cracked tools only. #shorts #brainrot", 
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public", 
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(VIDEO_FILE, chunksize=-1, resumable=True)
    print("🚀 Blasting video to YouTube...")
    response = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media).execute()
    video_id = response.get('id')
    print(f"✅ YouTube Live: https://youtu.be/{video_id}")

    # 2. Site Injection Logic
    new_card = f"""
    <div class="brain-rot-card">
        <div class="badge">LATEST DROP</div>
        <div style="position:relative; padding-bottom:177.77%; height:0; overflow:hidden; border-radius:10px;">
            <iframe style="position:absolute; top:0; left:0; width:100%; height:100%; border:0;" 
                src="https://www.youtube.com/embed/{video_id}?modestbranding=1&rel=0&controls=0" 
                allowfullscreen></iframe>
        </div>
        <p>This tool is <span class="slang">cracked</span>. Watch the demo above.</p>
    </div>
    """

    with open(HTML_FILE, "r") as f:
        content = f.read()
    
    # Injects the video right below the header
    updated_content = content.replace('<h1>AI ARSENAL</h1>', f'<h1>AI ARSENAL</h1>\n{new_card}')
    
    with open(HTML_FILE, "w") as f:
        f.write(updated_content)
    
    print("✅ Site updated with invisible host.")

    # 3. Auto-Deploy to GitHub
    print("📤 Pushing to GitHub Pages...")
    subprocess.run(["git", "add", "index.html"])
    subprocess.run(["git", "commit", "-m", f"Automated Drop: Video {video_id}"])
    subprocess.run(["git", "push", "origin", "main"])
    print("🔥 EVERYTHING IS LIVE.")

if __name__ == "__main__":
    upload_and_integrate()
