import os

HTML_FILE = "index.html"

master_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Arsenal - Money Maker</title>
    <style>
        body { background: #0a0a0a; color: #00ff00; font-family: 'Courier New', monospace; text-align: center; }
        h1 { text-shadow: 2px 2px #ff00ff, -2px -2px #00ffff; animation: glitch 1s infinite; font-size: 3em; margin-top: 20px;}
        .affiliate-container { display: flex; gap: 20px; flex-wrap: wrap; justify-content: center; padding: 20px; }
        .brain-rot-card {
            background: rgba(0, 0, 0, 0.8);
            border: 2px solid #333;
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.2);
            transition: 0.3s;
            flex: 1;
            min-width: 320px;
            max-width: 400px;
            padding: 20px;
            border-radius: 10px;
        }
        .brain-rot-card:hover {
            transform: scale(1.02) rotate(1deg);
            box-shadow: 0 0 30px rgba(255, 0, 255, 0.4);
        }
        .badge { font-weight: bold; padding: 5px 10px; display: inline-block; border-radius: 3px; margin-bottom: 15px; color: #000; }
        .video-container {
            width: 100%;
            aspect-ratio: 9/16;
            margin-bottom: 15px;
            background: #111;
            border: 1px solid #444;
            overflow: hidden;
            border-radius: 5px;
        }
        .video-container video, .video-container iframe {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        a.cta-button { display: block; padding: 12px; text-align: center; text-decoration: none; font-weight: bold; border-radius: 5px; margin-top: 15px; font-size: 1.2em; color: #000; }
        @keyframes glitch {
            0% { transform: translate(0); }
            20% { transform: translate(-2px, 2px); }
            40% { transform: translate(-2px, -2px); }
            60% { transform: translate(2px, 2px); }
            80% { transform: translate(2px, -2px); }
            100% { transform: translate(0); }
        }
    </style>
</head>
<body>
    <h1>AI ARSENAL</h1>
    <div class="affiliate-container">
        <!-- Card 1: UserInterviews -->
        <div class="brain-rot-card" style="border-color: #00ff00;">
            <div class="badge" style="background: #00ff00;">💸 ACTIVE PAYOUT</div>
            <h2>User Interviews</h2>
            <div class="video-container">
                <video controls autoplay muted loop playsinline>
                    <source src="arsenal_short.mp4" type="video/mp4">
                </video>
            </div>
            <p>Get paid real cash for testing apps and giving opinions. Real money, real fast.</p>
            <a href="https://www.userinterviews.com/r/xyktllqkd" target="_blank" class="cta-button" style="background: #00ff00;">👉 Claim Sign-Up Bonus</a>
        </div>

        <!-- Card 2: ElevenLabs -->
        <div class="brain-rot-card" style="border-color: #00d1ff;">
            <div class="badge" style="background: #00d1ff;">🎙️ PRO VOICE ENGINE</div>
            <h2>ElevenLabs AI</h2>
            <div class="video-container">
                <iframe src="https://www.youtube.com/embed/2Ah_Zn8qaA8?autoplay=1&mute=1&loop=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
            <p>The world's best AI audio. Perfect for faceless channels and uncanny storytelling.</p>
            <a href="https://try.elevenlabs.io/ke0nrfzwanm4" target="_blank" class="cta-button" style="background: #00d1ff;">👉 Try for Free</a>
        </div>
    </div>
</body>
</html>"""

with open(HTML_FILE, "w") as f:
    f.write(master_html)

print("✅ Master HTML with Video Embeds & Trippy UI generated!")
