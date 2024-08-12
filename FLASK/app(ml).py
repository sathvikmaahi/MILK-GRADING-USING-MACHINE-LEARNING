#render template : It retrieves the templates whichwe created using css...
#request: It requests the values to the model:




from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd

model = pickle.load(open(r"F:/MY PROJECTS/KJCMT COLLEGE PROJECTS/milk grading system files/Flask/milk.pkl",'rb'))

app = Flask(__name__) #function:


@app.route("/")
def about():
    return render_template('home.html')



@app.route("/predict")      
def home1():
    return render_template('predict.html')





@app.route("/pred", methods=['POST','GET'])
def predict():
   x = [[x for x in request.form.values()]] #x is our input variables
   print(x)
  
   x = np.array(x)
   print(x.shape)
     
     
   print(x)
   pred = model.predict(x)
   print(pred[0])
   return render_template('submit.html', prediction_text=str(pred))

if __name__ == "__main__":
 app.run(debug=False)
