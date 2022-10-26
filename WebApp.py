from flask import Flask,render_template,request
app=Flask(__name__)


@app.route("/")
@app.route("/home")
def Home():
    return render_template("home.html")
@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        return render_template("predict.html")
if __name__=='__main__':
    app.run(debug=True)