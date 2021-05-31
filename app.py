# Import the necessary packages
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

# Configuring the Flask environment and loading the pickle file
app = Flask(__name__)
model = pickle.load(open('Titanic_Survival_Predicion_RFC.pkl', 'rb'))
@app.route('/', methods = ['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods = ['POST'])
def predict():
    # Getting the form information
    if (request.method == "POST"):
        # Name
        Name = request.form['Name']
        
        # Age
        Age = int(request.form['Age'])
        
        # Gender
        Gender = request.form['Sex']
        Salutation = ""
        if (Gender == "Female"):
            Gender = 0
            Salutation = "Mrs."
        else:
            Gender = 1
            Salutation = "Mr."
        
        # SibSp
        SibSp = int(request.form['SibSp'])
        
        # Parch
        Parch = int(request.form['Parch'])
        
        # Class
        Class = int(request.form['Class'])
                
        # Fare
        Fare = float(request.form['Fare'])
        
        # Embarked
        Embarked = request.form['Embarked']
        if (Embarked == "Southampton"):
            Embarked = 2
        elif (Embarked == "Queenstown"):
            Embarked = 1
        else:
            Embarked = 0
            
        # Creating the input array
        inputs = [[Class, Gender, Age, SibSp, Parch, Fare, Embarked]]
        
        # Predicting the price of the car with the given inputs
        Prediction = model.predict(inputs)
        output = Prediction[0]
        
        # Displaying the output dependino upon the predictions
        if (output == 0):
            return render_template('output.html', prediction_text = f"Sorry {Salutation} {Name}. If you were on Titanic you couldn't have survived.")
        else:
            return render_template('output.html', prediction_text = f"Hurray! Hey {Salutation} {Name}, if you were on Titanic you could have survived.")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)
            
                                        