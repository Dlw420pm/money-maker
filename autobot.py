import os
from datetime import datetime

def auto_update_arsenal(tool_name, description, link):
    new_entry = f"""
    <div class="brain-rot-card">
        <div class="badge">NEW DROP</div>
        <h2>{tool_name} <span class="slang">(CRACKED)</span></h2>
        <p>{description}</p>
        <a href="{link}" class="btn">GET THE LOOT</a>
    </div>
    """
    # This automatically injects the new tool into your HTML
    with open("index.html", "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(content.replace('', new_entry + '\n'))
    
    print(f"🚀 {tool_name} is now live in the Arsenal.")

# Example: Automating a high-ticket recurring SaaS
auto_update_arsenal("GETRESPONSE AI", "Automate your entire email empire. 40% recurring commissions.", "https://www.getresponse.com/?a=dlw420")