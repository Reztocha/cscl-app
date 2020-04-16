import json

#open json file - our test database
def load_db():
    with open("cscl_test_db.json") as f:
        return json.load(f)
        
#use this variable to access database
db = load_db()