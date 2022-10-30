
from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
process=pickle.load(open("Model/processing.pkl","rb"))
idf=pickle.load(open("Model/TF_IDF.pkl","rb"))
model=pickle.load(open("Model/LogisticModel.pkl","rb"))
@app.route("/")
@app.route("/home")
def Home():
    return render_template("home.html")
@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        text=request.form.get('tweet').strip()
        
        #processedText=process(text)
        print(text)
        return render_template("predict.html")
if __name__=='__main__':
    app.run(debug=True)