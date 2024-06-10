from flask import Flask, redirect,url_for
## creates WSGI application - flask app object
app = Flask(__name__)

@app.route('/')  #decorator along with func to trigger
def welcome():
    return "welcome to my page here"

@app.route('/members') # link/members
def members():
    return "welcome to my page here members"

# building url dynamically
@app.route('/success/<int:score>') # success is the url and i want to append a value
def success(score): # url/success/55
    return "the student has passed with" + str(score)

@app.route('/fail/<int:score>') # fail is the url and i want to append a value
def fail(score): # url/fail/55
    return "the student has failed with" + str(score)

@app.route('/results/<int:marks>') # success is the url and i want to append a value
def results(marks): # url/success/55
    result =''
    if marks<50:
        result = 'fail'
    else:
        result = 'pass'
    return redirect(url_for(result,score=marks)) # redirects to the above success or fail functionality pages

if __name__=='__main__': #can be interview quest. why?
    app.run(debug=True) # helps automatically save & run when made changes
    