from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/output/<name>')
def output(name):
    return 'Welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('output', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('output', name= user))


@app.route('/terminal')
def terminal():
    return 'terminal'

@app.route('/devices_connected')
def device_manager():
    return 'Thisi is my device manager'

if __name__ == '__main__':
    app.run(debug = True)
    
