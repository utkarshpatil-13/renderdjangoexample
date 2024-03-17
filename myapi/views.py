from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from myapi.models import flower
from myapi.serializers import flowerSerializers
import pickle
import numpy as np
import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')

class FlowerView(viewsets.ModelViewSet):
	queryset = flower.objects.all()
	serializer_class = flowerSerializers


def normalize_document(stop_words):
		# lower case and remove special characters\whitespaces
	doc = re.sub(r'[^a-zA-Z\s]', '', doc, re.I|re.A)
	doc = doc.lower()
	doc = doc.strip()
	# tokenize document
	tokens = nltk.word_tokenize(doc)
	# filter stopwords out of document
	filtered_tokens = [token for token in tokens if token not in stop_words]
	# re-create document from filtered tokens
	doc = ' '.join(filtered_tokens)
	return doc

@api_view(["GET"])
def remarkSummarizer(request):
    try:
        DOCUMENT = request.data['text']
        DOCUMENT = re.sub(r'\n|\r', ' ', DOCUMENT)
        DOCUMENT = re.sub(r' +', ' ', DOCUMENT)
        DOCUMENT = DOCUMENT.strip()

        sentences = nltk.sent_tokenize(DOCUMENT)
        num_sentences = len(sentences)

        stop_words = nltk.corpus.stopwords.words('english')

        # Assuming normalize_document is a function that takes in stop words
        normalize_corpus = np.vectorize(normalize_document(stop_words))

        norm_sentences = normalize_corpus(sentences)
        # Do something with norm_sentences
        return Response("Success", status=status.HTTP_200_OK)

    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def vitaminPredict(request):
    try:
        model_loaded = pickle.load(open('static/vitamin_detector', 'rb'))
        mydata = request.data['data']

        unit = np.array(mydata).reshape(1, -1)
        y_pred = model_loaded.predict(unit)
        return JsonResponse({"prediction": y_pred.tolist()}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
	
# @api_view(["POST"])
# def breastCancerPredict(request):
# 	try:
# 		model_loaded = pickle.load(open('static/BreastCancer', 'rb'))
# 		mydata=request.data

# 		unit=np.array(list(mydata.values()))
# 		unit=unit.reshape(1,-1)
# 		y_pred=model_loaded.predict(unit)
# 		return JsonResponse('{}'.format(y_pred), safe=False)
# 	except ValueError as e:
# 		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
      

@api_view(["GET"])
def breastCancerPredict(request):
	try:
		model_loaded = pickle.load(open('static/BreastCancer', 'rb'))
		mydata=request.data
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		y_pred=model_loaded.predict(unit)
		return JsonResponse('{}'.format(y_pred), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
		
@api_view(["GET"])
def flowerPredict(request):
	try:
		model_loaded = pickle.load(open('static/model_saved', 'rb'))
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		mydata=request.data
		# mydata={
        #     'Sepal.Length': 6.2, 
		# 	'Sepal.Width' : 3.1, 
		# 	'Petal.Length' : 5.6,
        #     'Petal.Width' : 3.1
        # }
		# mydata={
        #     "Dependants": 3,
        #     "ApplicantIncome": 4500,
        #     "CoapplicantIncome": 1500,
        #     "LoanAmount": 128500,
        #     "Loan_Amount_Term": 360,
        #     "CreditHistory": 1,
        #     "Gender_Female": 0,
        #     "Gender_Male": 1,
        #     "Married_No": 0,
		# 	"Married_Yes": 1,
        #     "Education_Graduate": 0,
		# 	"Education_Not Graduate": 1,
        #     "Self_Employed_No": 1,
        #     "Self_Employed_Yes": 0,
        #     "Property_Area_Rural": 1,
        #     "Property_Area_Semiurban": 0,
        #     "Property_Area_Urban":0
        # }
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		# scalers=joblib.load("static\scalers.pkl")
		# X=scalers.transform(unit)
		y_pred=model_loaded.predict(unit)
		# y_pred=(y_pred>0.58)
		# newdf=pd.DataFrame(y_pred, columns=['Status'])
		# newdf=newdf.replace({True:'Approved', False:'Rejected'})
		return JsonResponse('Your Flower is {}'.format(y_pred), safe=False)
		# prediction = model_loaded.predict([[6.2, 3.1, 5.6, 3.1]])
		# return Response(f'{prediction}')
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)