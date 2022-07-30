import os
import re
from flask import Flask, render_template, request, Response
from dotenv import load_dotenv
from peewee import *  # abstracts away the need to manually create tables
import datetime  # for TimelinePost
from playhouse.shortcuts import model_to_dict # for post_time_line_post()

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route("/work")
def work():
    return render_template('work.html')

@app.route("/hobbies")
def hobbies():
    return render_template('hobbies.html')

@app.route("/travel")
def travel():
    return render_template('travel.html')

@app.route("/timeline")
def timeline():
    return render_template('timeline.html')


if os.getenv("TESTING") == "true":  # testing database
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:  # add MySQL Database
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306)


print(mydb)
# db.close() // may be necessary?

# ORM model/Create Database Table
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
mydb.connect()
mydb.create_tables([TimelinePost])
# db.close() // may be necessary?

# new POST route which adds a timeline post
@app.route('/api/timeline_post', methods = ['POST'])
def post_time_line_post():
    # Email Validation
    def validate(email):
        pattern = "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"
        if re.match(pattern,email):
            return True
        return False

    # Invalid Input Error Messages
    if 'name' not in request.form or request.form['name'] == '':
        return Response("Invalid Name", status = 400)
    if 'email' not in request.form or validate(request.form['email']) == False:
        return Response("Invalid Email", status = 400)
    if 'content' not in request.form or request.form['content'] == '':
        return Response("Invalid Content", status = 400)
    
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

# GET endpoint that retrieves all timeline posts ordered by created_at descending so the newest timeline posts are returned at the top.
@app.route('/api/timeline_post', methods = ['GET'])
def get_time_line_post():
    return{
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

# DELETE endpoint
# @app.route('/api/timeline_post', methods = ['DELETE'])
# def delete_time_line_post(id):
#     post = TimelinePost.query.get(id)
#     mydb.session.delete(post)
#     mydb.session.commit()

#     return{
#         'timeline_posts': [
#             model_to_dict(p)
#             for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
#         ]
#     }
