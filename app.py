from flask import Flask
<<<<<<< HEAD
app = Flask( __name__)
=======
app = Flask(__name__)
>>>>>>> dfbcf93 (Dockerfile added)
@app.route("/")
def home():
    return "hello from Flask + Jenkins"

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(host="0.0.0.0", port=5000)
>>>>>>> dfbcf93 (Dockerfile added)
