from flask import Flask, render_template, request
from sugar import passing_data
# AGE,SEX,BMI,BP
app = Flask(__name__)
@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
     result=request.form
     return render_template("index.html",result = passing_data(result))
   else:
      return render_template("index.html",result="")
if __name__ == '__main__':
   app.run(debug = True)
