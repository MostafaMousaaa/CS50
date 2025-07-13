from flask import Flask, session, render_template, redirect, url_for
app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_to_cart/<item>")
def add_to_cart(item):
    cart = session.get("cart", [])
    cart.append(item)
    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    cart = session.get("cart", [])
    return render_template("cart.html", cart=cart)

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", error_code=404, error_message="Page not found."), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("error.html", error_code=500, error_message="Internal server error."), 500

if __name__ == "__main__":
    app.run() 