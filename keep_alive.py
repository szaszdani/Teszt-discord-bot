from flask import Flask
from threading import Thread

# Létrehozzuk a Flask alkalmazást
app = Flask('')

@app.route('/')
def home():
    # Ezt a szöveget látja az Uptime Robot
    return "A Discord bot fut és ébren van!"

def run():
  # A web szerver futtatása a Render/Replit környezethez
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    """
    Ez a függvény indítja el a Flask szervert egy külön szálon, 
    így a fő program (Discord bot) is futhat mellette.
    """
    t = Thread(target=run)
    t.start()