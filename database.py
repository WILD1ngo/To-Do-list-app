import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect("data.db")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")


def create_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Task (
        task_text TEXT NOT NULL
    )
''')
    
def load_Tasks():
    conn = create_connection()
    cursor = conn.cursor()
    create_table(cursor)


    cursor.execute('SELECT Task_Text FROM Task')
    Tasks = cursor.fetchall()
    print (Tasks)
    return Tasks
    conn.close()
def add_Task(task_Text):
    conn = create_connection()
    cursor = conn.cursor()
    create_table(cursor)  # Assuming create_table function is defined elsewhere
    cursor.execute('INSERT INTO Task (task_text) VALUES (?)', (task_Text,))
    conn.commit()

def remove_Task(task_Text):
    conn = create_connection()
    cursor = conn.cursor()
    create_table(cursor)  # Assuming create_table function is defined elsewhere
    cursor.execute('DELETE FROM Task WHERE task_text = ?', (task_Text))
    conn.commit()


