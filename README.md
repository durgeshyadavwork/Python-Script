
# WhatsApp Number Formatter

This is a Python + Flask-based tool to auto-detect and format raw phone numbers into E.164 international format with country codes (like +91, +86 etc.).

## Features
- Supports 16 enabled countries (e.g., IN, US, CN, GB, etc.)
- Detects country based on mobile prefixes
- Formats raw numbers to WhatsApp-compatible format
- Upload CSV file via simple web interface
- Outputs cleaned CSV file with valid formatted numbers

## How to Use

1. Install dependencies:

   pip install flask phonenumbers


2. Run the Flask app:

   
   python3 app.py
   

3. Open browser at `http://localhost:5000`

4. Upload a CSV file with raw phone numbers (one per line)

5. Download the cleaned result CSV with formatted numbers.

## Folder Structure

```
├── app.py
├── phone_formatter.py
├── templates/
│   └── index.html
├── uploads/
├── cleaned/
```

---


