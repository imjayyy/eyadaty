import pymongo
# from pymongo import ObjectId
import datetime, uuid
from  werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask_login import (
    UserMixin,
    LoginManager,
    login_required,
    login_user,
    logout_user,
)
from classes.connection import users, send_email

users.create_index( [("Email", pymongo.DESCENDING)], unique=True )


class User():
    def __init__(self, id):
        cursor = users.find_one({"googleId": ObjectId(id)})
        for i in cursor:
            if i != "_id":
                setattr(self, i, cursor[i])
            else:
                self.id = str(cursor["_id"])

    @staticmethod
    def checkCredentials(googleId):
        cursor = users.find_one({'googleId': googleId} )
        if len(cursor) == 1:
            for i in cursor:
                cli = User(i['_id'])
            return cli
        else:
            return False

    @staticmethod
    def signUpAndLoginUser(name, email, googleId):
        user_dict = users.find_one({'Email': email, 'googleId' : googleId})
        if (user_dict) == None:
            users.insert_one( { 'name': name, 'Email': email, 'googleId' : googleId, 'Date' : datetime.datetime.now() })
            user_dict = users.find_one({'Email': email, 'googleId' : googleId})
            send_email(email)
        return user_dict

    @staticmethod
    def updateInfo(email, googleId, phone):
        users.update_one({'Email': email, 'googleId' : googleId}, {'$set' : {"Phone":phone} } )
        return True