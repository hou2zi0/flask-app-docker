from app import app

@app.route('/')
def index():
    return "Hello from Flask! 🐵"
    
@app.route('/affe')
def affe():
    return "Hello from Flask! Affe sagt Hallo! 🐵"
