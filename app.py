from flask import Flask, render_template
from InstaForm import LoginForm
app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = "Panczi"

@app.route('/hello')
def home():
    return render_template('Home.html')

@app.route('/')
@app.route('/instagram')
def instagram():
    form = LoginForm()
    return render_template("Template.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
###    app.run(host='0.0.0.0', port=5000)