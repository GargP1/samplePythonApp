from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about') 
def about():
    return "<h1>About Page</h1>"

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone'] 
        print(name, email, phone)
        return render_template('success.html', name = name)
    return render_template('contact.html')

if __name__ == '__main__':
   app.run(debug = True)
