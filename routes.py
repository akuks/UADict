from flask import Flask, render_template, request
from models import db, User
from forms import SignupForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:admin@127.0.0.1:5432/uadict'
# to intilize db in flask app
db.init_app(app)

app.secret_key = "development-key"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()

	if request.method == "POST":
		if form.validate() == False:
			return render_template("signup.html", form=form)
		else:
			newUser = User(form.first_name.data, form.middle_name.data, form.last_name.data,
				           form.email.data, form.password.data)
			db.session.add(newUser)
			db.session.commit()
			return "Sucess"
	
	elif request.method == "GET":
		return render_template("signup.html", form=form)

if __name__ == "__main__":
	app.run(debug="True")	