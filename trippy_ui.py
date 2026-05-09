import os

HTML_FILE = "index.html"

trippy_styles = """
<style>
    body { background: #0a0a0a; color: #00ff00; font-family: 'Courier New', monospace; }
    h1 { text-shadow: 2px 2px #ff00ff, -2px -2px #00ffff; animation: glitch 1s infinite; }
    .brain-rot-card { 
        background: rgba(0, 0, 0, 0.8);
        border: 1px solid #333;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.2);
        transition: 0.3s;
    }
    .brain-rot-card:hover { 
        transform: scale(1.02) rotate(1deg); 
        box-shadow: 0 0 30px rgba(255, 0, 255, 0.4);
    }
    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, 2px); }
        80% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }
</style>
"""

with open(HTML_FILE, "r") as f:
    content = f.read()

if "<style>" not in content:
    updated_content = content.replace("</head>", f"{trippy_styles}\n</head>")
    with open(HTML_FILE, "w") as f:
        f.write(updated_content)
    print("✅ Trippy UI injected!")
else:
    print("⚠️ Style block already exists. Manual tweak recommended.")
