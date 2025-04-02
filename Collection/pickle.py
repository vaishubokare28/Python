import pickle
data=["john","blake","martin","tiger"]
f=open("student.txt","wb")
pickle.dump(data,f)