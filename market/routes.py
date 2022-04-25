from market import app
from flask import render_template, request


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        # Get form input
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        role = request.form.get('role')

        
        return render_template('register.html')
    else:
        return render_template('register.html')