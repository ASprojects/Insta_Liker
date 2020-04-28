from flask import Flask, render_template, request
from InstaForm import LoginForm
from InstagramMain import InstaBot
app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = "SECRET"

@app.route('/hello')
def home():
    return render_template('Home.html')

@app.route('/')
@app.route('/instagram', methods=['GET','POST'])
def instagram():
    form = LoginForm()
    return render_template("Template.html", form=form)

@app.route('/processing', methods=['POST'])
def processing():
    username = request.form["username"]
    password = request.form["password"]
    hashtag = request.form["hashtag"]
    ASprojects = InstaBot(username, password)
    ASprojects.login()
    ASprojects.like_pic(hashtag)

if __name__ == '__main__':
    app.run(debug=True)
###    app.run(host='0.0.0.0', port=5000)