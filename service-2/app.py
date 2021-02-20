from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/animal', methods=['GET'])
def animal():
    animals = ["lion", "Dog", "Cat", "Cow"]
    return Response(random.choices(animals), mimetype="text/plain")

@app.route('/noise', methods=['POST'])
def noise():
    animal = request.data.decode('utf-8')
    if animal == "lion":
        noise = "Roar"
    elif animal == "Dog":
        noise = "Woof"
    elif animal == "Cat":
        noise = "Meow"
    else:
        noise = "Moo"
    return Response(noise, mimetype="text/plain") 


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)