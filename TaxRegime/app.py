from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'secret'

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['taxregime']
users_collection = db['users']

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        aadhar = request.form['aadhar']
        password = request.form['password']
        user = users_collection.find_one({'aadhar': aadhar})

        if user and user['password'] == password:
            session['aadhar'] = aadhar
            session['name'] = user['name']
            return redirect(url_for('request_view'))
        else:
            error = "Invalid credentials"
    return render_template('index.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        aadhar = request.form['aadhar']
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']

        if password != confirmPassword:
            return render_template('register.html', error="Passwords do not match.")

        if users_collection.find_one({'aadhar': aadhar}):
            return render_template('register.html', error="Aadhar already exists.")

        users_collection.insert_one({
            'aadhar': aadhar,
            'name': name,
            'email': email,
            'contact': contact,
            'password': password
        })
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        aadhar = request.form['aadhar']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        if password != confirm_password:
            return render_template('forgot.html', error="Passwords do not match.")

        user = users_collection.find_one({'aadhar': aadhar})
        if user:
            users_collection.update_one({'aadhar': aadhar}, {'$set': {'password': password}})
            return render_template('forgot.html', success="Password updated successfully.")
        else:
            return render_template('forgot.html', error="Aadhar not registered.")

    return render_template('forgot.html')

@app.route('/requestview', methods=['GET', 'POST'])
def request_view():
    if 'aadhar' not in session:
        return redirect(url_for('login'))

    aadhar = session['aadhar']
    name = session['name']

    if request.method == 'POST':
        if request.form.get('dropdown') == 'Yes':
            return redirect(url_for('sidebar'))

    return render_template('requestview.html', aadhar=aadhar, name=name)

@app.route('/sidebar')
def sidebar():
    if 'aadhar' not in session:
        return redirect(url_for('login'))

    aadhar = session['aadhar']
    name = session['name']
    return render_template('sidebar.html', aadhar=aadhar, name=name)

@app.route('/mytaxregime')
def my_tax_regime():
    if 'aadhar' not in session:
        return redirect(url_for('login'))

    aadhar = session['aadhar']
    name = session['name']
    return render_template('my_tax_regime.html', aadhar=aadhar, name=name)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
