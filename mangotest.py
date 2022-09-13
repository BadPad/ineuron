import pymongo


client = pymongo.MongoClient("mongodb+srv://bprasadv:Bday*300584@cluster0.bdy5eum.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name':'Badri',
    'emailid':'bprasadv@gmail.com',
    'surname':'Athreyas'
    }

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
