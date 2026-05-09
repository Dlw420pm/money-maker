import os

HTML_FILE = "index.html"

card = """
    <div class="brain-rot-card" style="border: 2px solid #00ff00;">
        <div class="badge" style="background: #00ff00; color: #000;">💸 ACTIVE PAYOUT</div>
        <h2>User Interviews</h2>
        <p>Get paid real cash for testing apps, answering questions, and giving your opinion on new tech.</p>
        <a href="https://www.userinterviews.com/r/xyktllqkd" target="_blank" style="display: block; background: #00ff00; color: #000; padding: 12px; text-align: center; text-decoration: none; font-weight: bold; border-radius: 5px; margin-top: 15px; font-size: 1.2em;">👉 Claim Your Sign-Up Bonus</a>
    </div>
"""

with open(HTML_FILE, "r") as f:
    content = f.read()

# Injects the new money card right below the main header
updated_content = content.replace('<h1>AI ARSENAL</h1>', f'<h1>AI ARSENAL</h1>\n{card}')

with open(HTML_FILE, "w") as f:
    f.write(updated_content)

print("✅ Affiliate card injected!")
