# In-Memory Database Engine Simulator

This project is a Python-based simulation of a Relational Database Management System (RDBMS). It was developed as part of the **BBM103: Introduction to Programming Laboratory** course. The system processes SQL-like commands to manage data stored in memory without requiring an external database server.

## 📌 Project Features

The simulator supports a variety of core database operations:
- **Table Creation:** Define new tables with custom column structures.
- **Data Manipulation (DML):** `INSERT`, `UPDATE`, and `DELETE` operations with condition filtering.
- **Data Querying:** `SELECT` specific columns and `COUNT` operations with support for multi-condition `WHERE` clauses (JSON-formatted).
- **Relational Operations:** `JOIN` functionality to combine data from two different tables based on a common key.
- **Formatted Output:** Beautifully rendered ASCII tables for data visualization in the console.

## 🛠️ Technical Details

- **Language:** Python 3.x
- **Storage:** Data is handled using Python dictionaries and lists to mimic table structures and rows.
- **Command Parsing:** Custom logic to parse and execute commands from text-based input files.
- **Robustness:** Handles error cases such as "Table not found", "Column not found", and duplicate primary key scenarios.

## 📁 File Structure

- `database.py`: The core engine containing the logic for all SQL-like operations and table rendering.
- `i1.txt`, `i2.txt`, `i3.txt`: Sample input files containing sequences of database commands.
- `01.txt`, `02.txt`, `03.txt`: Expected output files showing the results of the operations.
- `BBM_103_F_24_PA3-2.pdf`: Detailed project specifications.

## 🚀 How to Use

The script takes an input file as a command-line argument and processes the commands within.

1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/python-in-memory-database.git](https://github.com/yourusername/python-in-memory-database.git)
   ```

2. Run the engine with a sample input file:
   ```bash
   python database.py i1.txt
   ```

3. The system will process each line and display the results (tables, success messages, or errors) directly in your terminal.
   
## 📊 Example Commands Supported
   ```bash
   CREATE_TABLE students id,name,age,major
   INSERT students 1,John Doe,20,CS
   SELECT students id,name WHERE {"major": "CS"}
   UPDATE students {"major": "SE"} WHERE {"name": "John Doe"}
   JOIN students,courses ON major
   ```

---
*Developed as a Computer Engineering student at Hacettepe University.
   