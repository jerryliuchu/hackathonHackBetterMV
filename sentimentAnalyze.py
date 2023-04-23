# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    n = (sentiment_dict['neg']) * 100
    ne = sentiment_dict['neu'] * 100
    p = sentiment_dict['pos'] * 100

    x = "Your journal is " + str(round(n, 1)) + "% negative, " + str(round(ne, 1)) + "% neutral, and " + str(round(p,1)) + "% positive, and overall, your journal is "

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        x += "Positive";

    elif sentiment_dict['compound'] <= - 0.05:
        x += "Negative";

    else:
        x += "Neutral";

    return x

