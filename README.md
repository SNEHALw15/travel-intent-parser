# travel-intent-parser
LLM-powered travel intent parsing tool
# Travel Intent Parser 

This project converts natural language travel queries into structured JSON.

It demonstrates:

- Intent Parsing
- Slot Filling
- Backend-friendly JSON output

---

## Example Input

Book me a train from Pune to Delhi tomorrow evening

## Example Output

```json
{
  "intent": "travel_request",
  "source": "Pune",
  "destination": "Delhi",
  "mode": "train",
  "date": "tomorrow",
  "time": "evening"
}

## Example Output

```json
{
  "intent": "travel_request",
  "source": "Pune",
  "destination": "Delhi",
  "mode": "train",
  "date": "tomorrow",
  "time": "evening"
}
Tech Stack

Python

Groq LLM API

JSON Prompting



Setup Instructions
1. Install dependencies -pip install groq python-dotenv
2. Add API key - Create a .env file: 
GROQ_API_KEY=your_api_key_here
3. Run the script-python main.py
