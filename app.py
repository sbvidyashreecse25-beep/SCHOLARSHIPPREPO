from flask import flask,requesst
app=flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')
def submit():
    if request.method == 'POST':
