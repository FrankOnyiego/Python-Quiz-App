import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# Retrieve the contents of the "questions" table
cursor.execute("SELECT * FROM questions")
rows = cursor.fetchall()

# Display the contents of the table
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
conn.close()
