from pymongo import MongoClient # this import allows to connect to our mongodb database
from bson.objectid import ObjectId #query using an ObjectID


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, db, collection, username, password, host, port):
        """Initialize the CRUDOperations object."""
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.db = self.client[db]
        self.collection = self.db[collection]

    # Method to implement CRUD (Create) 
    def create(self, data):
        """Insert a document into the MongoDB collection."""
        if data is not None:
            insert_dictionary = self.database.animals.insert_one(data)
            if insert_dictionary != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to insert")

    # Method to implement CRUD (Read)
    def read(self, search_crit=None):
        """Query documents from the MongoDB collection based on the provided query."""
        if search_crit:
            animal_query = self.collection.find(search_crit, {"_id": False})
        else:
            animal_query = self.collection.find({}, {"_id": False})
        return animal_query
    
    # Method to implement CRUD (Update)
    """Update document(s) in the MongoDB collection based on the provided query."""
    def update(self, save):
        if save is not None:
            if save:
                result = self.database.animals.insert_one(save)
            return result;
        else:
            raise Exception("Nothing to update")
            
    
    # Method to implement CRUD (Delete)
    def delete(self, remove):
        """Delete document(s) from the MongoDB collection based on the provided query."""
        if remove is not None:
            if remove:
                result = self.database.animals.delete_one(remove)
        else:
            raise Exception("Nothing to delete")