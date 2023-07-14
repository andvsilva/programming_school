import sqlite3

# Connect to an existing database or create a new one
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY, name TEXT, salary REAL)''')

# Insert data into the table
cursor.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", ('John Doe', 5000))
cursor.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", ('Jane Smith', 6000))

# Commit the changes
conn.commit()

# Retrieve data from the table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()