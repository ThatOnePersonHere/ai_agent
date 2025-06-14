import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv)>1:
    response = client.models.generate_content(model='gemini-2.0-flash-001',contents=sys.argv[1])
    if response != None and len(sys.argv)>2 and sys.argv[2] == "--verbose":
        print(
                f'User prompt: {sys.argv[1]}\nPrompt tokens:{response.usage_metadata.prompt_token_count}\nResponse tokens:{response.usage_metadata.candidates_token_count}'
                )
else:
    print("Error: No Prompt provided.")
    exit(1)