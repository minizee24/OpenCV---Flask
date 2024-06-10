from flask import Flask, redirect,url_for, render_template, request
## creates WSGI application - flask app object
## http verb post and get

##Jinja2 template engine
'''
{%%...%} for statements, conditions, for loops
{{   }} expression to print
{#....#} this is for comments
'''
app = Flask(__name__)

@app.route('/')  #decorator along with func to trigger
def welcome():
    return render_template('index.html')

@app.route('/members') # link/members
def members():
    return "welcome to my page here members"

# building url dynamically
@app.route('/success/<int:score>') # success is the url and i want to append a value
# def success(score): # url/success/55. 
#     res =''
#     if score>=50:
#         res='pass'
#     else:
#         res='fail'
        
#     return render_template('result.html',result = res)
def success(score): # url/success/55
    res=''
    if score>=50:
        res='pass'
    else:
        res='fail'
    exp = {'score':score,'res':res} # displaying key avlues pairs
    return render_template('result.html',result = exp)

# @app.route('/fail/<int:score>') # fail is the url and i want to append a value
# def fail(score): # url/fail/55
#     return "the student has failed with" + str(score)

# @app.route('/results/<int:marks>') # success is the url and i want to append a value
# def results(marks): # url/success/55
#     result =''
#     if marks<50:
#         result = 'fail'
#     else:
#         result = 'pass'
#     return redirect(url_for(result,score=marks)) # redirects to the above success or fail functionality pages

@app.route('/submit',methods=['POST','GET'])  ## result checker html page
def submit():
    total_score =0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        DS = float(request.form['DS'])
        total_score = (science + maths+c+DS)/4

    return redirect(url_for('success',score = total_score))
# one url will be able to handle it 'success' as we have defined just that above with condition

if __name__=='__main__': #can be interview quest. why?
    app.run(debug=True) # helps automatically save & run when made changes

