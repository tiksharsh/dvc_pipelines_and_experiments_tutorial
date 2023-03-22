# https://towardsdatascience.com/the-ultimate-guide-to-building-maintainable-machine-learning-pipelines-using-dvc-a976907b2a1b

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_curve, auc

categories = ["comp.graphics","sci.space"]

newsgroups_train = fetch_20newsgroups(subset='train', categories=categories)
newsgroups_test = fetch_20newsgroups(subset='test', categories=categories)
newsgroups_all = fetch_20newsgroups(subset='all', categories=categories)

vectorizer = TfidfVectorizer()
vectorizer.fit(newsgroups_all.data)

X = vectorizer.transform(newsgroups_train.data)
clf = MultinomialNB(alpha=0.1)
clf.fit(X,newsgroups_train.target)

X_predict = vectorizer.transform(newsgroups_test.data)
y_pred_scores = clf.predict_proba(X_predict)
y_true = newsgroups_test.target

precision, recall, _ = precision_recall_curve(y_true, y_pred_scores[:, -1])
auc = auc(recall, precision)

print(auc)
