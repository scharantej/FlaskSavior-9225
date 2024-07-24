
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    data = request.form
    # Perform calculations or operations based on the data
    # Store the result in a variable called 'output'
    return render_template('result.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
