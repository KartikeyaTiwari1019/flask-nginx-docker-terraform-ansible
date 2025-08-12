from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Dummy check for demonstration
        if username == "admin" and password == "password":
            return f"<h2>Welcome, {username}!</h2>"
        else:
            return "<h2 style='color:red;'>Invalid Credentials</h2>"
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
