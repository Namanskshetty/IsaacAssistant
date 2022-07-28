import pickle
clfo=pickle.load(open("clf_save","rb"))
cvo=pickle.load(open("cv_save","rb"))
user=str(input("Enter the word to analysed  "))
data=cvo.transform([user]).toarray()
output = clfo.predict(data)
print(output)
