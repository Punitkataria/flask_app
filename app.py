from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify

## creating a simple flask application
app = Flask(__name__)  # entry point of program

@app.route("/", methods = ["GET"]) # This is a decorator that defines a route for the root URL ('/'), 
                                   # methods parameter allows to specify the HTTP methods accepted by decorated route.
def welcome():
    return "<h1>Welcome to new project</h1>"


@app.route("/index", methods = ["GET"])
def index() :
    return "this is index page"

# variable rule - putting a variable in url
@app.route("/success/<int:score>")
def success(score):
    return "the person has passed and score is: " + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "the person have failed and score is: " + str(score)

@app.route("/form", methods = ["GET","POST"])
def form():
     if request.method == "GET":
         return render_template("calculate.html")
     else: 
         maths = float(request.form["maths"]) 
         science = float(request.form["science"])   
         history = float(request.form["history"])  
          
         average_marks = (maths+science+history)/3
         
         # return render_template("calculate.html", score = average_marks) # here web template system(jinja2) is used to enter the data from backend.
         
         res = ""
         if average_marks >= 50:
             res = "success"
         else:
             res = "fail"
             
         return redirect(url_for(res,score = average_marks))
             



         
if __name__ == "__main__":
    app.run(debug=True)

'''
This conditional statement checks whether the script is the main entry point.
If it is, it runs the Flask application with app.run(debug=True).
The debug=True argument enables debugging mode, which can be helpful during development.
'''
