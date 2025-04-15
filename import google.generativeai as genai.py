import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="AIzaSyDNERNqiOfd4r0ZauWFavomvHmi2USF8vA")

# List all models accessible to your account
models = genai.list_models()

print("Available models:")
for model in models:
    print(f"- {model.name}")
