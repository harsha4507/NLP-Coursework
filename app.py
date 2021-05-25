from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import gensim
import gensim.corpora as corpora
import gensim.models as models
from gensim.test.utils import common_corpus, common_dictionary
from gensim.models import CoherenceModel
import pyLDAvis.gensim_models
import pickle
import pyLDAvis
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
	model1 = open('model.pkl','rb')
	c1=request.form.get('c1')
	c2=request.form.get('c2')
	c3=request.form.get('c3')
	x = joblib.load(model1)
	a=0
	if request.method == 'POST':
		if c1:
			a="1"
		y= x.print_topics()
		z=pd.DataFrame(y)
		z=z.to_html()
	return render_template('result.html',predict=z, pre=a)

if __name__ == '__main__':
	app.run(debug=True)