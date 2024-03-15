from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/top')
def top():
    return render_template('top.html')

@app.route('/easy')
def easy():
    return render_template('easy.html')

@app.route('/medium')
def medium():
    return render_template('medium.html')

@app.route('/hard')
def hard():
    return render_template('hard.html')

@app.route('/again')
def again():
    score = request.args.get('score')
    return render_template('again.html', score=score)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', ssl_context="adhoc")
