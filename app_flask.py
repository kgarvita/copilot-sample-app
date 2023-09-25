from flask import Flask, render_template, request, jsonify


#app = Flask(__name__)
app = Flask(__name__, template_folder='template')

@app.route("/")
def ind():
    ct=0
    return render_template("index.html")




@app.route("/get", methods=["GET","POST"])
def chatbot_response():
    msg = request.form['msg']
    result = msg

#if __ == "__main__":
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)

