import os

HTML_FILE = "index.html"

with open(HTML_FILE, "r") as f:
    content = f.read()

# Constrain the video height so the buttons stay on screen
if "max-height: 350px;" not in content:
    content = content.replace('.video-container {', '.video-container { max-height: 350px; ')

with open(HTML_FILE, "w") as f:
    f.write(content)

print("✅ Layout fixed: Videos constrained, buttons pulled up!")
