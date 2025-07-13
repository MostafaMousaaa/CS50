from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello, {name}!"
    return render_template("greet.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", error_code=404, error_message="Page not found."), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("error.html", error_code=500, error_message="Internal server error."), 500

if __name__ == "__main__":
    app.run() 