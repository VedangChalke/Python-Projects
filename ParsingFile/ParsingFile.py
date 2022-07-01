#AIM: CREATE A PROGRAM TO PARSED AND STORED A PARTICULAR DATA FILE IN FOLDER, PARSING SHOULD BE DONE FOR EACH DATA AS SHOULD BE PRESENTED IN THE FORM OF LIST


import requests
import pickle

# HERE TAKEN A DATA FILE OF MACHINE LEARNING OF AUTOMOBILE INDUSTRY
data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data").text
#print(data)

list1 = data.split("\n")
#print(list1)

#LIST COMPREHENSION METHOD
list2 = [item.split(",") for item in list1 if len(item)!=0]
print(list2)

#STORING PARSED FILE AS PICKLE AS A BINARY FILE
with open("myauto.pkl" , "wb") as f:
     print(pickle.dump(list2 ,f))
     print("DONE, Created and Stored pickle file in Library\n\n")


#READING STORED FILE
print("Opening Binary file into Readable text..........\n")
with open ("myauto.pkl" , "rb") as f:
     print(pickle.load(f))
