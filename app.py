from flask import Flask, request, jsonify, render_template, redirect, url_for, flash,make_response
# render_template: to render the HTML templates
# redirect: to redirect the user to another endpoint
# url_for: to generate URLs
# flash: to display messages to the user
# request: to access incoming request data

app = Flask(__name__)
app.secret_key = "12345"  # required for sessions (session is time interval when user is on the your app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 