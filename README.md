# laptopprice_Prediction

# App link
https://laptopprice2022.herokuapp.com/

# Dataset Link
https://github.com/tarunsinghkanwar/laptopprice_Prediction/tree/main/dataset

# Aim

This project aims to predict the Price of Laptop by taking it's Brand, it's Type, RAM(in GB), and other parameters.

![image](https://user-images.githubusercontent.com/37711056/151305368-fb4e1d44-4566-45a8-aa7e-27dc7e01dd87.png)
![image](https://user-images.githubusercontent.com/37711056/151312856-059b208c-97fc-4ed3-8694-1e1a04738539.png)

# Description
This project takes the parameters of an Laptop such as : Company, TypeName , Ram , CPUBrand.
XGBOOST Regression model was built which had  0.85 R2_score on Test Data.
This project was given the form of an website built on Streamlit where we used the XGBOOST Regression model to perform predictions.

## laptop_Price_EDA.ipynb
Here all the cleaning has been done(Except the Encoding) and exported as X_train.pkl and Y_train.pkl.
## Preprocessing.py
Here we are doing the Encoding(RareLabel and Categorical ).
## Model_Tuner.py
It will find the best parameter for XGBOOST model
## Model_Building.py
It will fit the XGboost Model to the preprocessed data 
## Load_Data.py
It will load the X_train.pkl and Y_train.pkl files.
## Load_model.py 
It will dump the XGboost model after fitting on X_train


# How to use?

Clone the repository
Install the required packages in "requirements.txt" file.
Some packages are:

numpy
pandas
scikit-learn

Run the "main.py" file And you are good to go.

 




## Bug / Feature Request
If you find a bug , kindly open an issue [here](https://github.com/tarunsinghkanwar/laptopprice_Prediction/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/tarunsinghkanwar/laptopprice_Prediction/issues/new). Please include sample queries and their corresponding results.

## Libaray Used
#  Pandas , Numpy , XGBOOST, Feature-Engine, Streamlit



