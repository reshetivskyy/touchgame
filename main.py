from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


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
