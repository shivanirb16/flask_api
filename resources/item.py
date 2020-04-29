from flask_restful import reqparse,Resource
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This ele is mandatory")
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="This ele is mandatory")

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {"message":"Item not found"},400


    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':'item with name {} already exists'.format(name)},400
        data = Item.parser.parse_args()
        item = ItemModel(name,data["price"],data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message":"Error occured during inserting"},500

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message':'Item deleted'}

    def put(self,name):

        data=Item.parser.parse_args()
        item =ItemModel.find_by_name(name)
        if item is None:
            item=ItemModel(name,data['price'],data['store_id'])
        else:
            item.price=data['price']
        item.save_to_db()

        return item.json()

class ItemList(Resource):
    def get(self):
        return {'items:':[x.json() for x in ItemModel.query.all()]}