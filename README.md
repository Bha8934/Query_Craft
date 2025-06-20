# QueryCraft: Natural Language to SQL Converter

## Overview
QueryCraft transforms natural language descriptions into precise SQL queries using Google's Gemini Pro AI. Designed for database professionals and developers, it eliminates manual SQL syntax requirements while supporting PostgreSQL, MySQL, SQL Server, and SQLite.

### Key Features
- **Natural Language Processing**: Convert plain English to accurate SQL
- **Multi-Database Support**: Generate compatible queries for major RDBMS
- **Secure API Integration**: Protected Google Gemini API key management
- **Visual Workflow**: Intuitive interface with guided conversion
- **Complex Query Handling**: Supports JOINs, subqueries, aggregations

![QueryCraft Interface](images/app_screenshot.png)

## 🔑 API Key Configuration

### Step 1: Create Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with Google account
3. Click "Create Project" > Name it (e.g., "QueryCraft-SQL") > Create

### Step 2: Enable Gemini API
1. Navigate to "APIs & Services" > "Library"
2. Search for "Generative Language API"
3. Click "Enable"

### Step 3: Generate API Key
1. Go to "Credentials" > "+ Create Credentials" > "API Key"
2. Copy the generated key (displayed only once)
3. Click "Restrict Key":
   - Application restriction: HTTP referrers
   - API restriction: Select "Generative Language API"

### Step 4: Configure Local Environment
```bash
# Create .env file
touch .env  # Mac/Linux
New-Item .env -ItemType File  # Windows (PowerShell)

# Add API key
echo "GOOGLE_API_KEY=your_key_here" >> .env  # Mac/Linux
Add-Content .env "GOOGLE_API_KEY=your_key_here"  # Windows
```

### Step 5: Security Hardening
1. Add to .gitignore:
```bash
echo ".env" >> .gitignore
```
2. Set usage quotas in Google Cloud Console

## 📁 Project Structure
```bash
QueryCraft/
├── images/                   # Application visuals
│   ├── header_icon.png       # Branding image
│   └── workflow_diagram.png  # Conversion visual
├── .env                      # API credentials
├── .gitignore                # Excludes sensitive files
├── app.py                    # Main application logic
├── requirements.txt          # Dependency list
└── README.md                 # This documentation
```

## ⚙️ Installation Guide

### Prerequisites
- Python 3.9+
- Google Gemini API Key

### Setup Process
1. **Clone repository**:
```bash
git clone https://github.com/your-username/QueryCraft.git
cd QueryCraft
```

2. **Install dependencies**:
```bash
# Mac/Linux
pip install -r requirements.txt

# Windows
py -m pip install -r requirements.txt
```

3. **Configure environment** (complete API Key steps above)

## 🚀 Usage Instructions

1. **Launch application**:
```bash
# Mac/Linux:
streamlit run app.py

# Windows:
py -m streamlit run app.py
```

2. **Operational workflow**:
   1. Describe query in natural language:
      > "Show customers from California with orders over $500"
   
   2. Click "Submit" to generate SQL
   
   3. Review formatted output:
```sql
SELECT customers.name, orders.total 
FROM customers
JOIN orders ON customers.id = orders.customer_id
WHERE customers.state = 'CA' AND orders.total > 500;
```

## 💻 Technical Implementation

### API Integration
```python
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

# Validate API key
if 'GOOGLE_API_KEY' not in os.environ:
    st.error("❌ API key missing! Create .env file")
    st.stop()

# Configure Gemini
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')
```

### Query Processing
```python
def get_gemini_response(user_query):
    prompt = f"""
    Convert to SQL: "{user_query}"
    Guidelines:
    1. Identify tables and columns
    2. Apply conditions and joins
    3. Format SQL properly
    4. Include only SQL code
    """
    return model.generate_content(prompt).text
```

## 🔒 Security Best Practices

### API Key Management
1. **Rotation Policy**:
   - Regenerate keys quarterly
   - Update `.env` immediately after rotation
2. **Access Restrictions**:
   - Bind keys to specific IP ranges
   - Set usage quotas in Google Cloud Console
3. **Storage Protocols**:
   - Never store keys in code repositories
   - Use secret managers in production

### Application Security
- Input sanitization for SQL injection prevention
- HTTPS enforcement for all requests
- Session timeout (15 minutes)
- Rate limiting (60 requests/minute)

## 🛠 Troubleshooting

| Error | Solution |
|-------|----------|
| `API_KEY_INVALID` | Verify key in .env matches Cloud Console |
| `PERMISSION_DENIED` | Enable "Generative Language API" |
| `QUOTA_EXCEEDED` | Increase quotas in Cloud Console |
| `LOCATION_NOT_SUPPORTED` | Use global API endpoint |

### Key Rotation Protocol
1. Generate new key in Cloud Console
2. Update `.env` with new key
3. Immediately disable old key
4. Test application functionality

## 📚 Support & Resources
- [Issue Tracker](https://github.com/your-username/QueryCraft/issues)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Google Cloud Console](https://console.cloud.google.com/)
- [Streamlit Deployment Guide](https://docs.streamlit.io/deploy)
- [Pricing Details](https://ai.google.dev/pricing)

**Note**: Free tier includes 60 requests/minute. Production usage costs $0.50/1k characters.
