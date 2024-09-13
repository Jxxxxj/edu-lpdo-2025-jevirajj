from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')


    return f"Merci {first_name} {last_name}, nous avons reçu votre email à {email}."

if __name__ == '__main__':
    app.run(debug=True)
