# Python - Server Side Rendering

## 📋 Description

This project explores server-side rendering (SSR) concepts in Python, focusing on dynamic content generation using templates. You'll learn how to render HTML pages dynamically by processing data from various sources including JSON files, CSV files, and SQLite databases.

## 🎯 Learning Objectives

At the end of this project, you should be able to explain:

- What server-side rendering is and how it differs from client-side rendering
- How to use Python to generate dynamic HTML content
- How to work with template engines (Jinja2)
- How to read and process data from different file formats
- How to integrate database queries with template rendering
- Best practices for separating logic from presentation

## 🛠️ Requirements

- Python 3.x
- Jinja2 library (`pip install jinja2`)
- Basic understanding of HTML
- Familiarity with SQL (for database tasks)

## 📁 Project Structure

```
python-server_side_rendering/
│
├── README.md                 # Project documentation
├── task_00_intro.py         # Introduction to SSR concepts
├── task_01_jinja.py         # Basic Jinja2 templating
├── task_02_logic.py         # Control structures and logic in templates
├── task_03_files.py         # Reading and rendering file data
├── task_04_db.py            # Database integration
│
├── templates/               # HTML template directory
│
├── items.json               # Sample JSON data for testing
├── products.json            # Products dataset (JSON format)
├── products.csv             # Products dataset (CSV format)
├── products.db              # SQLite database with products
└── template.txt             # Simple text template example
```

## 📝 Tasks

### Task 0: Introduction to Server-Side Rendering
**File:** `task_00_intro.py`

Learn the fundamentals of server-side rendering and create your first dynamically generated content.

### Task 1: Jinja2 Templates
**File:** `task_01_jinja.py`

Implement basic templating using Jinja2, Python's most popular template engine.

**Key Concepts:**
- Template syntax
- Variable substitution
- Template inheritance

### Task 2: Template Logic
**File:** `task_02_logic.py`

Master control structures in templates including loops and conditionals.

**Key Concepts:**
- For loops in templates
- If/else statements
- Filters and functions

### Task 3: File Data Rendering
**File:** `task_03_files.py`

Read data from JSON and CSV files, then render it dynamically in templates.

**Key Concepts:**
- JSON parsing
- CSV processing
- Data transformation

### Task 4: Database Integration
**File:** `task_04_db.py`

Query SQLite database and display results using templates.

**Key Concepts:**
- Database connections
- SQL queries
- Result rendering

## 🚀 Usage

### Install Dependencies

```bash
pip install jinja2
```

### Run Tasks

```bash
# Task 0
python task_00_intro.py

# Task 1
python task_01_jinja.py

# Task 2
python task_02_logic.py

# Task 3
python task_03_files.py

# Task 4
python task_04_db.py
```

## 📊 Data Files

### items.json
Contains sample item data for testing basic JSON rendering.

### products.json
Product catalog in JSON format with fields: id, name, category, price.

### products.csv
Product catalog in CSV format - same data as JSON for format comparison.

### products.db
SQLite database containing a `products` table with sample e-commerce data.

### template.txt
Simple text template demonstrating basic variable substitution.

## 💡 Tips

- Always validate your data before rendering
- Use Jinja2's auto-escaping to prevent XSS attacks
- Keep templates simple and logic minimal
- Separate concerns: data processing in Python, presentation in templates
- Use template inheritance to avoid repetition

## 🔗 Resources

- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Python Template Strings](https://docs.python.org/3/library/string.html#template-strings)
- [Server-Side Rendering Explained](https://www.patterns.dev/posts/server-side-rendering/)
