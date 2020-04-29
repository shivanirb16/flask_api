from models.store import StoreModel
from flask_restful import Resource

class Store(Resource):
    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':"Store not found"},404


    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message':"Store already exists"},400
        store=StoreModel(name)
        try:
            store.save_to_db()
            return store.json(),201
        except:
            return {"message":"Error occured during inserting"},500

    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message':"store deleted"}

class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}