import numpy as np
import pandas as pd
import pickle
import json
import config


class LoanPrediction():
    def __init__(self,Gender,Married,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Dependents):

        self.Gender = Gender
        self.Married = Married
        self.Education = Education
        self.Self_Employed = Self_Employed
        self.ApplicantIncome = ApplicantIncome
        self.CoapplicantIncome = CoapplicantIncome
        self.LoanAmount = LoanAmount
        self.Loan_Amount_Term = Loan_Amount_Term
        self.Credit_History = Credit_History
        self.Property_Area = Property_Area
       

        self.Dependents = "Dependents_" + str(Dependents)

    def load_models(self):
        with open ("rf_scaled_model.pkl","rb")as f:
            self.model = pickle.load(f)

        with open ("json_file.json","r")as f:
            self.json_data = json.load(f) 

        with open ("scaled_model.pkl","rb")as f:
            self.scaled_data = pickle.load(f)


    def loan_status_prediction(self):

        self.load_models()  # creating instance of model and json_data

        Dependents_index = list(self.json_data["columns"]).index(self.Dependents) 

        array = np.zeros(len(self.json_data["columns"])) 

        array[0] = self.json_data["Gender"][self.Gender]
        array[1] = self.json_data["Married"][self.Married]
        array[2] = self.json_data["Education"][self.Education]
        array[3] = self.json_data["Self_Employed"][self.Self_Employed]


        array[4] = self.ApplicantIncome
        array[5] = self.CoapplicantIncome
        array[6] = self.LoanAmount
        array[7] = self.Loan_Amount_Term 
        array[8] = self.Credit_History
        array[9] = self.json_data["Property_Area"][Property_Area]
        array[Dependents_index] = 1

        print("test_array:-->",array)

        scaled_array = self.scaled_data.transform([array])

        loan_status = self.model.predict(scaled_array)[0]

        return loan_status

if __name__=="__main__":
   
    Gender = "Male"
    Married = "Yes"
    Education = "Graduate"
    Self_Employed = "No"
    ApplicantIncome = 4583
    CoapplicantIncome = 1508.0
    LoanAmount = 128.0
    Loan_Amount_Term = 360.0
    Credit_History = 1.0
    Property_Area = "Rural"
    Dependents = 1
       

    loan_pred = LoanPrediction(Gender,Married,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Dependents)
    loan_status  = loan_pred.loan_status_prediction()
    print("Loan_Status:",loan_status)