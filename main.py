import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Fixed schema fields
FIELDS = ["intent", "source", "destination", "mode", "date", "time"]
def search_transport(source, destination, mode):
    """
    Simulates a backend API call.
    
    """
    print("\n[Backend API Simulation]")
    print(f"Searching {mode} options from {source} → {destination}...")


def parse_travel_intent(user_input):
    """
    Converts a natural language travel request into structured JSON.
    """

    prompt = f"""
You are a travel intent parser.

Extract travel details from the user sentence.

Return ONLY valid JSON in this exact format:

{{
  "intent": "travel_request",
  "source": null,
  "destination": null,
  "mode": null,
  "date": null,
  "time": null
}}

Rules:
- Return ONLY JSON
- No extra text
- Use null if missing

User sentence:
"{user_input}"
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    raw_output = response.choices[0].message.content.strip()

    # ✅ Validate JSON
    try:
        parsed = json.loads(raw_output)

        # Ensure all fields exist
        for field in FIELDS:
            if field not in parsed:
                parsed[field] = None

        return parsed

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by model",
            "raw_output": raw_output
        }


if __name__ == "__main__":
    examples = [
        "I want to go from Pune to Delhi by train tomorrow evening",
        "Book a bus from Mumbai to Goa Friday morning",
        "I need a flight to Bangalore",
        "Travel from Chennai to Hyderabad"
    ]

    for sentence in examples:
        print("\nUser Input:", sentence)

        result = parse_travel_intent(sentence)

        print("Parsed Output:")
        print(json.dumps(result, indent=2))
        
            # ✅ Backend tool simulation (Step 4)
        if result.get("source") and result.get("destination") and result.get("mode"):
             search_transport(
                    result["source"],
                    result["destination"],
                    result["mode"]
        )
