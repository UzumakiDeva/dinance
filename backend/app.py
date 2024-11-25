from flask import Flask, render_template, request, jsonify
from peewee import MySQLDatabase, Model, CharField, DecimalField

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
    name = CharField()
    symbol = CharField(unique=True)

    class Meta:
        database = db  # Connect the model to the MySQL database
        table_name = "coins"

class TradePair(Model):
    symbol = CharField(unique=True)
    price = DecimalField(max_digits=16,decimal_places=8)

    class Meta:
        database = db  # Connect the model to the MySQL database
        table_name = "tradepairs"

# Flask application setup
app = Flask("__main__")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_coin",methods=["POST"])
def create_coin():
    data = request.json
    try:
        if not Coin.select().where(Coin.symbol == data['symbol']).exists():
            Coin.create(name=data['name'], symbol=data['symbol'])

        coins = Coin.select()
        coin_list = [{"name":coin.name, "symbol":coin.symbol} for coin in coins]


    except Exception as e:
        print(f"Database error: {e}")
    finally:
        db.close()
    return jsonify(coin_list)

@app.route("/get_coins",methods=["GET"])
def get_coins():
    try:
        coins = Coin.select()
        coins = [{"name": coin.name, "symbol": coin.symbol} for coin in coins]
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        db.close()
    return jsonify(coins)

@app.route("/add_trade_pair",methods=["POST"])
def create_tradepair():
    data = request.json
    try:
        if not TradePair.select().where(TradePair.symbol == data['symbol']).exists():
            TradePair.create(symbol=data['symbol'], price=data['price'])

        tradepairs = TradePair.select()
        pair_list = [{"symbol":pair.symbol, "price":pair.price} for pair in tradepairs]

    except Exception as e:
        print(f"Database error: {e}")
    finally:
        db.close()
    return jsonify(pair_list)



if __name__ == "__main__":
    # Database operations
    try:
        db.connect()
        db.create_tables([User,Coin], safe=True)  # Create the table if it doesn't already exist

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
