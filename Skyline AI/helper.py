import google.generativeai as genai

# Directly pass the API key (for testing)
api_key = "AIzaSyDm_GzS_-zlFU1LXAaYOEL6OpB-sNZum8w"

# Configure the API key
genai.configure(api_key=api_key)

# Initialize the model and make a request
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("Explain how AI works")

# Print the response
print(response.text)
