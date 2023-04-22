from flask import Flask, render_template, request

from sentimentAnalyze import sentiment_vader

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
    negative, neutral, positive, compound, overall_sentiment = sentiment_vader(journal);



    return render_template("index.html", name = name, journal = journal, overall_sentiment = overall_sentiment);

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)