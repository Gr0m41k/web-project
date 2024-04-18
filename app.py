from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        name_sig = request.form['name_sig']
        email_sig = request.form['email_sig']
        password_sig = request.form['password_sig']

        user = User(username=name_sig, email=email_sig, password=password_sig)

        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')

        except:
            return '<h1>Упс.. Ошибка 407</h1>'
    else:
        return render_template('reg.html')


if __name__ == '__main__':
    app.run(debug=True)
