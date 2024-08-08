from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Define a route for another example page
@app.route('/example')
def example():
    return "This is an example page."

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)