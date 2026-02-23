from flask import Flask
app = Flask(_name)
@app.route("/")
def home():
    return "hello from Flask + Jenkins"

if __name__ == "__main__":
    app.run(debug=True)