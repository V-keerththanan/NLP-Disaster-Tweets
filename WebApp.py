from flask import Flask,render_template,request
import pickle
import re
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class Ownprocessing:
    stopword = list(stopwords.words('english'))
    def Mypreprocessing_SingleText(self,sent):
        lem=WordNetLemmatizer()
        sen=sent.lower()
        sen=re.sub(r"http\S+","",sen)
        sen=re.sub(r"[^\w\s]","",sen)
        make=""
        for word in sen.split():
            if word not in self.stopword:
                word=lem.lemmatize(word)
                make=make+word+" "
        make=make.strip()
        return make
    
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def Home():
    return render_template("home.html")
@app.route("/predict",methods=['POST'])
def predict():
    dummy=[]
    if request.method=='POST':
        text=request.form.get('tweet').strip()
        print(text)
        text=Ownprocessing().Mypreprocessing_SingleText(text)
        idf=pickle.load(open("Model/TF_IDF.pkl","rb"))
        model=pickle.load(open("Model/LogisticModel.pkl","rb"))
        dummy.append(text)
        predictValue=model.predict(idf.transform(dummy).toarray())[0]
        result=''
        if predictValue==0:
            result="This tweet is not about real Disaster"
        else:
            result="This tweet is  about real Disaster"
        print(result)
        return render_template("predict.html",r=result)
if __name__=='__main__':
    app.run(debug=True)
