from app import app

@app.route('/')
@app.route('/index')
def greet():
    return "Hello World!"
