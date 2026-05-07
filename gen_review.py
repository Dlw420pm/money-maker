import os

def create_review(tool_name, slang_rating, link):
    content = f"""
    <div class="brain-rot-card">
        <h2>{tool_name} <span class="slang">({slang_rating})</span></h2>
        <p>This tool is actually cracked. No cap, it saves 10+ hours a week.</p> 
        <a href="{link}" class="btn">GET THE LOOT</a>
    </div>
    """
    # Using 'a' to append to the end of your index.html
    with open("index.html", "a") as f:
        f.write(content)
    print(f"✅ {tool_name} added to the Arsenal.")

# Example usage
if __name__ == "__main__":
    create_review("KREA AI", "ABSOLUTE GOATED", "https://krea.ai?via=dlw420")
