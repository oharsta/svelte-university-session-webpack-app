from uuid import uuid4

from flask import current_app


class ToDo:

    @staticmethod
    def find_all():
        return current_app.mongo.db.todos.find({})

    @staticmethod
    def delete(doc_id):
        return current_app.mongo.db.todos.delete_one({"_id": doc_id})

    @staticmethod
    def save_or_update(model, return_data=True):
        todos = current_app.mongo.db.todos
        if "_id" in model:
            todos.update_one({"_id": model["_id"]}, {"$set": model})
        else:
            model["_id"] = str(uuid4())
            todos.insert_one(model)
        return todos.find_one({"_id": model["_id"]}) if return_data else None
