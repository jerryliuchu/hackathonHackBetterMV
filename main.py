from flask import Flask, render_template, request

from sentimentAnalyze import sentiment_scores

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods = ['POST', 'GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]

    journ = request.form.to_dict()
    journal = journ["journal"]
    s = sentiment_scores(journal);



    return render_template("index.html", name = name, journal = journal, s = s);


@app.route("/resources")
def resources():
    return render_template("resources.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

