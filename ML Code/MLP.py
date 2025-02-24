from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble
from sklearn.model_selection import cross_validate
import pandas, xgboost, numpy, textblob, string
from keras.preprocessing import text, sequence
from keras import layers, models, optimizers
import pickle 
import os

root_path = os.getcwd()
# load the dataset
try:
    data = open(root_path + "\\Corpus\\normalizedData.txt", encoding='utf-8').read()
except FileNotFoundError:
    root_path = root_path + "\\Cabueta-TrainedModelsDetection"
    data = open(root_path + "\\Corpus\\normalizedData.txt", encoding='utf-8').read()
    
labels, texts = [], []
for i, line in enumerate(data.split("\n")):
    content = line.split("\t")
    labels.append(content[0])
    texts.append(" ".join(content[1:]))
#stemming
data1 = []
import nltk

nltk.download('punkt')

st = nltk.ISRIStemmer()
for tx in texts:
    tweet = ""
    for a in nltk.word_tokenize(tx):
        tweet = tweet + st.stem(a)+ " "
    data1.append(tweet.strip())

#print(data1[:10])

# create a dataframe using texts and lables
trainDF = pandas.DataFrame()
trainDF['tweet'] = data1
trainDF['class'] = labels

# split the dataset into training and validation datasets 
train_x, valid_x, train_y, valid_y = model_selection.train_test_split(trainDF['tweet'], trainDF['class'],test_size = 0.2)

# create a count vectorizer object 
count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
count_vect.fit(trainDF['tweet'])

# transform the training and validation data using count vectorizer object
xtrain_count =  count_vect.transform(train_x)
xvalid_count =  count_vect.transform(valid_x)

# word level tf-idf
tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=20000)
tfidf_vect.fit(trainDF['tweet'])
xtrain_tfidf =  tfidf_vect.transform(train_x)
xvalid_tfidf =  tfidf_vect.transform(valid_x)

# ngram level tf-idf 
tfidf_vect_ngram = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', ngram_range=(2,3), max_features=20000)
tfidf_vect_ngram.fit(trainDF['tweet'])
xtrain_tfidf_ngram =  tfidf_vect_ngram.transform(train_x)
xvalid_tfidf_ngram =  tfidf_vect_ngram.transform(valid_x)

# characters level tf-idf
tfidf_vect_ngram_chars = TfidfVectorizer(analyzer='char', token_pattern=r'\w{1,}', ngram_range=(2,3), max_features=20000)
tfidf_vect_ngram_chars.fit(trainDF['tweet'])
xtrain_tfidf_ngram_chars =  tfidf_vect_ngram_chars.transform(train_x) 
xvalid_tfidf_ngram_chars =  tfidf_vect_ngram_chars.transform(valid_x) 

def train_model(classifier, feature_vector_train, label, feature_vector_valid, modelName, is_neural_net=False):
    # fit the training dataset on the classifier
    clf = classifier.fit(feature_vector_train, label)
    with open(modelName, 'wb') as picklefile:
        pickle.dump(clf,picklefile)
    # predict the labels on validation dataset
    predictions = clf.predict(feature_vector_valid)
    #scores = cross_validate(clf, feature_vector_train, label, cv=10, scoring='f1_weighted')
    #print(scores)
    if is_neural_net:
        predictions = predictions.argmax(axis=-1)
    
    #return metrics.accuracy_score(predictions, valid_y)
    print(metrics.precision_score(predictions, valid_y, average='weighted'))
    print(metrics.recall_score(predictions, valid_y, average='weighted'))
    return metrics.f1_score(predictions, valid_y, average='weighted')
from sklearn.neural_network import MLPClassifier

# MLPClassifier on Count Vectors
MLPmodelname = root_path + "//TrainedModels//50CountVectors_MLP_Model.pkl"
MLP = MLPClassifier(hidden_layer_sizes=(8,8,8), activation='relu', solver='adam', max_iter=500)
accuracy = train_model(MLP, xtrain_count, train_y, xvalid_count,MLPmodelname)
print ("MLP, Count Vectors: ", accuracy)

# MLPClassifier on Word Level TF IDF Vectors
MLPmodelname = root_path + "//TrainedModels//51WordLevel_MLP_Model.pkl"
accuracy = train_model(MLP, xtrain_tfidf, train_y, xvalid_tfidf,MLPmodelname)
print ("MLP, WordLevel TF-IDF: ", accuracy)

# MLPClassifier on Ngram Level TF IDF Vectors
MLPmodelname = root_path + "//TrainedModels//52N-GramVectors_MLP_Model.pkl"
accuracy = train_model(MLP, xtrain_tfidf_ngram, train_y, xvalid_tfidf_ngram,MLPmodelname)
print ("MLP, N-Gram Vectors: ", accuracy)

# MLPClassifier on Character Level TF IDF Vectors
MLPmodelname = root_path + "//TrainedModels//53CharLevelVectors_MLP_Model.pkl"
accuracy = train_model(MLP, xtrain_tfidf_ngram_chars, train_y, xvalid_tfidf_ngram_chars,MLPmodelname)
print ("MLP, CharLevel Vectors: ", accuracy)


