import bcrypt
import psycopg2

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="healthcare_db",
    user="postgres",
    password="your_password"  # Replace with your actual password
)
cursor = connection.cursor()

# User registration
def register_user(username, password):
    # Hash the password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        # Insert the new user into the database
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (username, password_hash)
        )
        connection.commit()
        print("User registered successfully!")
    except psycopg2.IntegrityError:
        connection.rollback()
        print("Error: Username already exists.")

# Example: Register a user
register_user("test_user", "secure_password")

# Close the connection
cursor.close()
connection.close()
