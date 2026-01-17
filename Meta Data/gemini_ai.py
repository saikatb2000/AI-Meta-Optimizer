import google.generativeai as genai

genai.configure(api_key="AIzaSyBDQNf4tivzRAkqtA8tiNSIiSCWeKh3Ofk")

model = genai.GenerativeModel("gemini-2.5-flash")

def optimize_meta(title, description, url):
    prompt = f"""
You are an SEO expert.

Website URL: {url}
Current Meta Title: {title}
Current Meta Description: {description}

Suggest:
1) SEO optimized meta title (max 60 characters)
2) SEO optimized meta description (max 155 characters)

Follow Google SEO best practices.
Return clean output.
"""

    response = model.generate_content(prompt)
    return response.text
