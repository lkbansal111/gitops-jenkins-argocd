from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("text", "")
        return user_input + " This is Gitop class."
    
    return "Send a POST request with 'text' field"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)