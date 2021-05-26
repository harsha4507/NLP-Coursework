from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
import gensim
import gensim.corpora as corpora
import gensim.models as models
from gensim.test.utils import common_corpus, common_dictionary
from gensim.models import CoherenceModel

app = Flask(__name__)
Hist=[]


@app.route('/')
def home():
	return render_template('home.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
	Hist_session=[]
	x = pickle.load(open("model.pkl","rb"))
	#model1 = open('model.pkl','rb')
	df1= open('dataframe.pkl','rb')
	c1=request.form.get('c1')
	c2=request.form.get('c2')
	c3=request.form.get('c3')
	c4=request.form.get('c4')
	c5=request.form.get('c5')
	#x = pickle.load("model1.pkl","rb")
	P=pd.DataFrame()
	k=pd.read_pickle(df1)
	k10=k.to_html()
	a=0
	if request.method == 'POST':
		if c1:
			k1=k.loc[k['Company']=='O2']
			P=P.append(k1,ignore_index=True)
			a=1
			Hist_session.append(c1)
		if c2:
			k2=k.loc[k['Company']=='Safaricom_Care']
			P=P.append(k2,ignore_index=True)
			a=1
			Hist_session.append(c2)
		if c3:
			k3=k.loc[k['Company']=='VerizonSupport']
			P=P.append(k3,ignore_index=True)
			a=1
			Hist_session.append(c3)
		if c4:
			k4=k.loc[k['Company']=='idea_cares']
			P=P.append(k4,ignore_index=True)
			a=1
			Hist_session.append(c4)
		if c5:
			k5=k.loc[k['Company']=='sprintcare']
			P=P.append(k5,ignore_index=True)
			a=1
			Hist_session.append(c5)
		if a==0:
			P=P.append(k,ignore_index=True)
			Hist_session.append([c1,c2,c3,c4,c5])
	
		P=P.to_html()
		y= x.print_topics()
		z=pd.DataFrame(y)
		z=z.to_html()
		Hist.append(Hist_session)
	return render_template('result.html',predict=z,df=P)

@app.route('/History')
def History():
	return render_template("History.html",len=len(Hist),History=Hist)

if __name__ == '__main__':
	app.run(debug=True)
