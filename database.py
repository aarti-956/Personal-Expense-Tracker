import sqlite3

def create_connection():

    connection = sqlite3.connect("expenses.db")

    return connection



def add_expense(amount, category, date, description):

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO expenses
        (amount, category, date, description)

        VALUES (?, ?, ?, ?)
        """,

        (amount, category, date, description)

    )


    connection.commit()

    connection.close()



def view_expenses():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        "SELECT * FROM expenses"
    )


    data = cursor.fetchall()


    connection.close()

    return data


def delete_expense(expense_id):

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        DELETE FROM expenses
        WHERE id=?
        """,
        (expense_id,)
    )


    connection.commit()

    connection.close()
    
    
def update_expense(expense_id, amount, category, date, description):

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE expenses
        SET amount=?,
            category=?,
            date=?,
            description=?
        WHERE id=?
        """,
        (
            amount,
            category,
            date,
            description,
            expense_id
        )
    )


    connection.commit()

    connection.close()
def get_total_expense():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        "SELECT SUM(amount) FROM expenses"
    )


    result = cursor.fetchone()


    connection.close()


    if result[0] is None:

        return 0


    return result[0]

def get_expense_count():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM expenses"
    )


    result = cursor.fetchone()


    connection.close()


    return result[0]
def get_top_category():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
        LIMIT 1
        """
    )


    result = cursor.fetchone()


    connection.close()


    if result:

        return result[0]

    else:

        return "None"
def create_users_table():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE,

            password TEXT
        )
        """
    )


    connection.commit()

    connection.close()
def register_user(username, password):

    connection = create_connection()

    cursor = connection.cursor()


    try:

        cursor.execute(
            """
            INSERT INTO users(username,password)

            VALUES(?,?)
            """,
            (
                username,
                password
            )
        )


        connection.commit()


        return True


    except:

        return False


    finally:

        connection.close()
def login_user(username,password):

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=? AND password=?
        """,
        (
            username,
            password
        )
    )


    result = cursor.fetchone()


    connection.close()


    return result
def get_dashboard_data():

    connection = create_connection()

    cursor = connection.cursor()


    # Total expense

    cursor.execute(
        "SELECT SUM(amount) FROM expenses"
    )

    total = cursor.fetchone()[0]


    if total is None:
        total = 0



    # Transaction count

    cursor.execute(
        "SELECT COUNT(*) FROM expenses"
    )

    count = cursor.fetchone()[0]


    connection.close()


    return total, count                