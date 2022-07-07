from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f27d76de11771ec8a992862795014b55'

posts = [
    {
    'author':'Corey Schafer',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 20, 2018'
    },{
    'author':' Schafer',
    'title': 'Blog Post 1',
    'content': 'Second post content',
    'date_posted': 'April 20, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register',methods=['get','post'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['get','post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='123':
            flash('You have been logged in','success')
            return redirect(url_for('home'))
        else:
            flash('Loginin unsuccessfully','danger')
    return render_template('login.html',title='Login',form=form)


if __name__=='__main__':
    app.run(debug=True)