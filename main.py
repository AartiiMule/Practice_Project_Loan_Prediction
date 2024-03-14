from flask import Flask, jsonify, render_template, request

from project_app.utils import LoanPrediction

# Creating instance here
app = Flask(__name__)


@app.route("/") 
def hello_flask():
    print("Welcome to Loan Prediction System")   
    return render_template("index.html")


@app.route("/predict_Loan_Status", methods = ["POST", "GET"])
def loan_status_prediction():
    if request.method == "GET":
        print("We are in a GET Method")


        Gender = request.args.get("Gender")
        Married = request.args.get("Married")
        Education = request.args.get("Education")
        Self_Employed = request.args.get("Self_Employed")
        ApplicantIncome = eval(request.args.get("ApplicantIncome"))
        CoapplicantIncome = eval(request.args.get("CoapplicantIncome"))
        LoanAmount = eval(request.args.get("LoanAmount"))
        Loan_Amount_Term = eval(request.args.get("Loan_Amount_Term"))
        Credit_History = eval(request.args.get("Credit_History"))
        Property_Area = request.args.get("Property_Area")
        Dependents = eval(request.args.get("Dependents"))
    

        print("*********************** Gender,Married,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Dependents **********************\n",Gender,Married,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Dependents)

        loan_pred = LoanPrediction(Gender,Married,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Dependents)
        loan_status  = loan_pred.loan_status_prediction()
    
        return render_template("index.html", prediction = loan_status)
    
print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 1004, debug = False)  # By default Prameters