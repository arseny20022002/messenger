import datetime
from peewee import *

db = PostgresqlDatabase('messenger', user='postgres', password='ars19293949', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField()
    password_hash = CharField()

class Chat(BaseModel):
    chat_id = IntegerField()
    user_id = IntegerField()

class Message(BaseModel):
    owner_name = CharField()
    send_time = DateTimeField(default=datetime.datetime.now)
    text = TextField()

class Message_chat(BaseModel):
    message_id = ForeignKeyField(Message, backref='messages')
    chat_id = ForeignKeyField(Chat, backref='chats')

class User_chat(BaseModel):
    user_id = ForeignKeyField(User, backref='users')
    chat_id = ForeignKeyField(Chat, backref='chats')



    