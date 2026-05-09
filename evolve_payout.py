import os

HTML_FILE = "index.html"

# Custom CSS for the Payout Card
custom_css = """
<style>
    .payout-card {
        border: 2px solid #00ff00 !important;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.3);
        animation: pulse-green 2s infinite;
    }
    @keyframes pulse-green {
        0% { box-shadow: 0 0 5px rgba(0, 255, 0, 0.3); }
        50% { box-shadow: 0 0 20px rgba(0, 255, 0, 0.6); }
        100% { box-shadow: 0 0 5px rgba(0, 255, 0, 0.3); }
    }
    .payout-badge {
        background: #00ff00 !important;
        color: #000 !important;
        font-weight: 900;
        text-transform: uppercase;
        padding: 4px 10px;
        border-radius: 3px;
        font-size: 0.8em;
    }
</style>
"""

with open(HTML_FILE, "r") as f:
    content = f.read()

# Add the CSS to the head if it's not there
if "</head>" in content and "payout-card" not in content:
    content = content.replace("</head>", f"{custom_css}\n</head>")

# Apply the custom class to the User Interviews card
content = content.replace('class="brain-rot-card"', 'class="brain-rot-card payout-card"', 1)
content = content.replace('ACTIVE PAYOUT', '<span class="payout-badge">💸 ACTIVE PAYOUT</span>', 1)

with open(HTML_FILE, "w") as f:
    f.write(content)

print("✅ Money Green evolution applied.")
