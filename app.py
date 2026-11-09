import pickle

from flask import Flask,render_template,request
import numpy as np
#import pandas as pd


#create an application
app = Flask(__name__)

# load the model that u trained
with open('House_Model.pkl','rb') as f:
    model=pickle.load(f)


#  class - different parameters
class HousePrice():

    def __init__(self,bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,sqft_above,sqft_basement,yr_built,yr_renovated,city,statezip,country):  #this function executes automatically when an obj is called.

        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.sqft_living = sqft_living
        self.sqft_lot = sqft_lot
        self.floors = floors
        self.waterfront = waterfront
        self.view = view
        self.condition = condition
        self.sqft_above = sqft_above
        self.sqft_basement = sqft_basement
        self.yr_built = yr_built
        self.yr_renovated = yr_renovated
        self.city=city
        self.statezip=statezip
        self.country=country

    def predict(self):


        if self.bedrooms <=0 or self.bathrooms <=0:   # if user dont specify these requoirements  then this shows an error of invalid  inputsss.
            return 'Invalid Inputs  --  Enter Correct values... '

        else:
            data=np.array([[
                self.bedrooms,
                self.bathrooms,
                self.sqft_living,
                self.sqft_lot,
                self.floors,
                self.waterfront,
                self.view,
                self.condition,
                self.sqft_above,
                self.sqft_basement,
                self.yr_built,
                self.yr_renovated,
                self.city,
                self.statezip,
                self.country
            ]])


            result=model.predict(data)


            return result[0]



# home route - redirects to home page.
@app.route('/')   # this is decorator  it connects the url to py function.

def home():    # this function  handles the homepage request.

    return render_template('index.html')

@app.route('/predict',methods=['POST'])   # accept the user data by post method

def predict():
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    sqft_living = float(request.form['sqft_living'])
    sqft_lot = float(request.form['sqft_lot'])
    floors = int(request.form['floors'])
    waterfront = int(request.form['waterfront'])
    view = int(request.form['view'])
    condition = int(request.form['condition'])
    sqft_above = int(request.form['sqft_above'])
    sqft_basement = int(request.form['sqft_basement'])
    yr_built = int(request.form['yr_built'])
    yr_renovated = int(request.form['yr_renovated'])
    city = int(request.form['city'])
    statezip = int(request.form['statezip'])
    country = int(request.form['country'])

    #create an obj

    house_obj=HousePrice(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,sqft_above,sqft_basement,yr_built,yr_renovated,city,statezip,country)


    result=house_obj.predict()   #this predict method is in our class HousePrice



    if isinstance(result,str):
        return render_template('index.html',prediction=result)

    else:
        return render_template('index.html',prediction=f'Prediction House Price: ${result:,.2f}')


if __name__ == '__main__':
    app.run(debug = True)