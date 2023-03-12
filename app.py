from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # used to encrypt session data

# Define a dictionary to store the users' data
users = {}

# Home page
@app.route('/index')
def home_page():
    return render_template('index.html')

# Define a route to display the registration form
@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')

# Define a route to handle the registration form submission
@app.route('/register', methods=['POST'])
def register_submit():
    # Get the values from the form
    username = request.form['username']
    password = request.form['password']
    
    # Check if the username is already taken
    if username in users:
        return 'Username already taken'
    
    # Add the user to the dictionary
    users[username] = password
    
    return redirect('/login')

# Define a route to display the login form
@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

# Define a route to handle the login form submission
@app.route('/login', methods=['POST'])
def login_submit():
    # Get the values from the form
    username = request.form['username']
    password = request.form['password']
    
    # Check if the username and password match
    if username not in users or users[username] != password:
        return 'Invalid username or password'
    
    # Set the user's session data
    session['username'] = username
    
    return redirect('/')

# Define a route to display the user's profile
@app.route('/')
def profile():
    # Check if the user is logged in
    if 'username' not in session:
        return redirect('/login')
    
    # Get the user's data from the dictionary
    username = session['username']
    password = users[username]
    
    return render_template('profile.html', username=username, password=password)

# Define a route to handle logging out
@app.route('/logout')
def logout():
    # Clear the user's session data
    session.clear()
    
    return redirect('/login')

# About page
@app.route('/about')
def about_page():
     return render_template('about.html')           

# End
if __name__ == '__main__':
    app.run(debug=True)  # run the application in debug mode
