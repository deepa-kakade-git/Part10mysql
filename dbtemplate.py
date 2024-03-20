# db template code
import sqlalchemy as db  #object relational mapper
import mysqlclient
# mysqlclient (a maintained fork of MySQL-Python)
engine = db.create_engine("mysql+mysqldb://deep:deep7573_mysql@localhost/data5zero")

conn = engine.connect()
metadata = db.MetaData()

Person = db.Table('Person', metadata,
              db.Column('Id', db.Integer(),primary_key=True),
              db.Column('FirstName', db.String(255), default=''),
              db.Column('LastName', db.String(255), default=''),
              )

metadata.create_all(engine)

query = db.insert(Person).values(Id=101, FirstName ='Andrew', LastName='Johnson')

Result = conn.execute(query)  # insert the above record into the database

output = conn.execute(Person.select()).fetchall()
print(output)












