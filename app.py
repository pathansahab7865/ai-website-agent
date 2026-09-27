import os
import google.generativeai as genai

# Google AI Studio ki API Key yahan paste karein
API_KEY = "AQ.Ab8RN6IxVxLbA58FVmmgxLHuafjoVV1WwY5HIhuq-9Uv5OXZDQ"

# Gemini setup
genai.configure(api_key=API_KEY)

def generate_website_agent():
    print("="*50)
    print("🤖 Welcome to AI Website Developer Agent 🤖")
    print("="*50)

    # User inputs
    b_name = input("\n1. Business ka naam likho: ")
    b_type = input("2. Business kis cheez ka hai (e.g. Restaurant, Salon, Gym): ")
    b_services = input("3. Kaun konsi services ya products hain: ")
    b_color = input("4. Website ka color theme kaisa chahiye (e.g. Red and Black, Blue and White): ")

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
    5. Output ONLY the raw HTML code without markdown code blocks or additional text.
    """

    print("\n⏳ Agent website code design aur generate kar raha hai...")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    # Code clean karna
    clean_html = response.text.replace("```html", "").replace("```", "").strip()

    # File save karna
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(clean_html)

    print("\n✅ Mubarak ho! Aapki website successfully generate hokar 'index.html' file me save ho gayi hai!")

if __name__ == "__main__":
    generate_website_agent()
