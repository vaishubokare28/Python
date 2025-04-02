import pickle
data=["john","blake","martin","tiger"]
byte=pickle.dumps(data)  #to convert python object into byte stream ---pickling 
print(byte)


data=pickle.loads(byte)  #convert byte stream to python objects- unpickling 
print(data)




