import json
import urllib.request

# Aapki API Key
API_KEY = "AQ.Ab8RN6Jr0Vyoso0_2T9fwZ8ZFrBhBxT5DX5yJ0xhuYJEQI3ROQ"

def generate_website_agent():
    print("="*50)
    print("🤖 Welcome to AI Website Developer Agent 🤖")
    print("="*50)

    b_name = input("\n1. Business ka naam likho: ")
    b_type = input("2. Business kis cheez ka hai (e.g. Restaurant, Salon, Gym): ")
    b_services = input("3. Kaun konsi services ya products hain: ")
    b_color = input("4. Website ka color theme kaisa chahiye: ")

    prompt = f"""
    You are an expert AI Web Developer Agent.
    Create a complete, single-page professional website for:
    - Business Name: {b_name}
    - Business Type: {b_type}
    - Key Services/Features: {b_services}
    - Color Theme Preference: {b_color}

    Requirements:
    1. Write clean, valid HTML5 code with modern Tailwind CSS CDN added in the <head>.
    2. Design sections: Header/Navbar, Hero Banner with Call to Action, About Us, Services/Features Grid, Testimonials, and Contact Form/Footer.
    3. Use high-quality Unsplash image URLs for placeholder images.
    4. Make the design fully mobile responsive.
    5. Output ONLY raw HTML code inside <html></html> tags without markdown formatting.
    """

    print("\n⏳ Agent website code generate kar raha hai...")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode('utf-8')

    try:
        req = urllib.request.Request(url, data=data, headers=headers)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            code_text = result['candidates'][0]['content']['parts'][0]['text']

            clean_html = code_text.replace("```html", "").replace("```", "").strip()

            with open("index.html", "w", encoding="utf-8") as f:
                f.write(clean_html)

            print("\n✅ Mubarak ho! Website successfully generate hokar 'index.html' me save ho gayi hai!")

    except Exception as e:
        print(f"\n❌ Error aagaya: {e}")

if __name__ == "__main__":
    generate_website_agent()
