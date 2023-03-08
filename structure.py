import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Select all records from the "questions" table
c.execute("SELECT * FROM questions")
rows = c.fetchall()

# Print each row to the screen
for row in rows:
    print(row)

# Close the connection
conn.close()
