import base64

with open("ChatGPT_Obsidian.png", "rb") as f:
    encoded = base64.b64encode(f.read()).decode("utf-8")
    print(encoded)