# NLQ-Driven-Smart-Table-Selector

## 📌 Overview
The **NL-to-SQL Table Selector** is an AI-powered system that dynamically selects the most relevant tables from a database schema based on a user's **natural language query** (NLQ). It then integrates with an NL-to-SQL model (like OpenAI's GPT) to generate SQL queries.

## 🚀 Features
- **Natural Language Processing (NLP)**: Extracts keywords from user queries.
- **Table Ranking**: Uses fuzzy matching to rank relevant database tables.
- **Dynamic Table Selection**: Filters and selects only the most relevant tables.
- **AI-Powered SQL Generation**: Generates SQL queries using an NL-to-SQL model.
- **User Interface**: Includes a simple UI for entering queries.

## 🛠️ Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/nl-to-sql-selector.git
cd nl-to-sql-selector
```
### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
Ensure you have `python3` installed.

## 📌 Usage
### **Run the Application**
```bash
python app.py
```
This starts the application where you can input natural language queries.

### **Example Query**
```python
query = "Get all customer emails and names"
```
**Output:**
```json
{
  "customers": {
    "columns": ["id", "name", "email", "created_at", "total_spent"]
  }
}
SQL Query: SELECT name, email FROM customers;
```

## 📂 Project Structure
```
📦 nl-to-sql-selector
 ┣ 📜 app.py           # Main application script
 ┣ 📜 ui.py            # User interface for querying
 ┣ 📜 schema.json      # Database schema file
 ┗ 📜 README.md        # Documentation
```

## 🔧 Configuration
- **Schema File:** The database schema (`schema.json`) should be in **JSON format**.
- **Threshold Score:** Adjust the `threshold` in `select_relevant_tables()` to control table selection sensitivity.
- **OpenAI API Key:** Ensure `openai` is properly configured to generate SQL queries.

## 📌 Dependencies
- `fuzzywuzzy`
- `nltk`
- `openai`

## 📝 License
MIT License

## 🤝 Contributing
Feel free to fork, improve, and submit a PR!

## 📞 Support
For any issues, contact **your.email@example.com**.

