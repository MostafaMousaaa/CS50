from flask import Flask, session, render_template, redirect, url_for
app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/set")
def set_session():
    session["user"] = "Alice"
    return redirect(url_for("get_session"))

@app.route("/get")
def get_session():
    user = session.get("user", "Not set")
    return render_template("session.html", user=user)

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", error_code=404, error_message="Page not found."), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("error.html", error_code=500, error_message="Internal server error."), 500

if __name__ == "__main__":
    app.run() 