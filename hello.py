from flask import Flask , render_template


'''
safe - apply html
title - capitalize first letter of every word
lower 
upper 
capitalize - capitalize first letter
trim - remove extra spaces from the end
striptags - ignore html tags
'''


#create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route("/")
def index():
	first_name = "Eshaan"
	fruits = ["apple","banana" , "kiwi",12 , 34]
	return render_template("index.html" ,fruits = fruits ,first_name = first_name)

@app.route("/user/<name>")
def user(name):
	return render_template("user.html", name = name)


#create custom error pages

#invalid URL
@app.errorhandler(404)

def page_not_found(e):
	return render_template("404.html"),404


#internal server error. 
@app.errorhandler(500)

def internal_server_error(e):
	return render_template("500.html"),500



if __name__ == "__main__":
	app.run(debug = True)