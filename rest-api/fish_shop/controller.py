from main import app

@app.route('/')
def index():
    return 'Hooray'

@app.route('/prize/<id>')
def get_fish(id):
    return "<h1>HANDS UP</h1><br>Give me your money!!!!"


@app.route("/fish")
def find_fish():
    return "The fish had gotten lost<br><h2>CRYING!!!</h2>"

@app.route("/fish", methods=["POST"])
def create_fish():
    print("fish_killed")
    return ""