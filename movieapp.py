from flask import Flask, render_template, url_for,  flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5ef125114dc5f9b1ba25242cfac67cc0'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Game of Thrones',
        'content': 'First post content',
        'release_date': '2011-04-17',
        'poster': 'https://cdn.watchmode.com/posters/0345534_poster_w185.jpg',
        'Trailer': ' https://www.youtube.com/watch?v=BpJYNVhGf1s',
        'streaming_links': 'https://tv.apple.com/us/episode/winter-is-coming/umc.cmc.11q7jp45c84lp6d16zdhum6ul?playableId=tvs.sbd.9001%3A494877461&showId=umc.cmc.7htjb4sh74ynzxavta5boxuzq'
    }]


# Homepage 
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# Movie Page
@app.route('/movie')
def movie():
    return render_template('movie.html', posts=posts, title="Movie")



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
