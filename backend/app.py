from flask import Flask, render_template, request
from peewee import MySQLDatabase, Model, CharField

# Configure MySQLDatabase using Peewee
db = MySQLDatabase(
    'dinance', 
    user='root', 
    password='Admin@123',  # Correct spelling
    host='localhost', 
    port=3306, 
)

# Define a model (table structure)
class User(Model):
    username = CharField(unique=True)
    email = CharField()

    class Meta:
        database = db  # Connect the model to the MySQL database
        table_name = "users"

class Coin(Model):
    name = CharField
    symbol = CharField(unique=True)

    class Meta:
        database = db  # Connect the model to the MySQL database
        table_name = "coins"

# Flask application setup
app = Flask("__main__")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_coin",methods=["POST"])
def create_coin():
    name = request.json.get("name")
    symbol = request.json.get("symbol")
    image = request.json.get("image")

    Coin.create(name=name,symbol=symbol,image=image)
    return {
        "message" : f"Coin {symbol} was created successfully"
    }, 200





if __name__ == "__main__":
    # Database operations
    try:
        db.connect()
        db.create_tables([User], safe=True)  # Create the table if it doesn't already exist

        # Insert a new user if no users exist
        if User.select().count() == 0:
            User.create(username='john_doe', email='john@example.com')

        # Query and print all users
        for user in User.select():
            print(f"Username: {user.username}, Email: {user.email}")
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        db.close()

    # Run the Flask app
    app.run(debug=True)
