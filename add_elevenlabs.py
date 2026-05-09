import os

HTML_FILE = "index.html"

card = """
    <div class="brain-rot-card" style="border: 2px solid #00d1ff;">
        <div class="badge" style="background: #00d1ff; color: #000;">🎙️ PRO VOICE ENGINE</div>
        <h2>ElevenLabs AI</h2>
        <p>The world's most advanced AI audio platform. Perfect for faceless YouTube channels, storytelling, and uncanny voice clones.</p>
        <a href="https://try.elevenlabs.io/ke0nrfzwanm4" target="_blank" style="display: block; background: #00d1ff; color: #000; padding: 12px; text-align: center; text-decoration: none; font-weight: bold; border-radius: 5px; margin-top: 15px; font-size: 1.2em;">👉 Get Started for Free</a>
    </div>
"""

with open(HTML_FILE, "r") as f:
    content = f.read()

# Injects the new ElevenLabs card
updated_content = content.replace('<h1>AI ARSENAL</h1>', f'<h1>AI ARSENAL</h1>\n{card}')

with open(HTML_FILE, "w") as f:
    f.write(updated_content)

print("✅ ElevenLabs card injected!")
