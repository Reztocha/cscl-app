import json

#open json file - our test database
def load_db():
    with open("cscl_test_db.json") as f:
        return json.load(f)

#save to the database
def save_db():
    with open("cscl_test_db.json","w") as f:
        return json.dump(db,f)
        
#use this variable to access database
db = load_db()