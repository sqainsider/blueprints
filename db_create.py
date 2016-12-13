
#project/sqlite3.py

from datetime import date

from project import db
from project.models import Task, User

#create the database and the db table
db.create_all()

db.session.add(
  Task(
    "1.Finish this tutorial",date(2015,3,13),10,date(2015,3,16), 1, "admin"
  )
)

db.session.add(
  Task(
    "2.Finish all tutorial",date(2016,3,13),10, date(2016,7,13),1, "admin"
    )
)


db.session.add(
  User(
    "admin","admin@abc.com","admin","user"
    )
)


db.session.add(
  User(
    "sysadmin","sysadmin@sqainsider.com","sysadmin","admin"
    )
)


db.session.commit()
