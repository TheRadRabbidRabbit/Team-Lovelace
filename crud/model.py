from sqlalchemy.exc import IntegrityError
from __init__ import db


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Users(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)
    feedback = db.Column(db.String(255), unique=True, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, email, phone, feedback):
        self.name = name
        self.email = email
        self.phone = phone
        self.feedback = feedback

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "feedback": self.feedback
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name, phone="", feedback=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(phone) > 0:
            self.phone = phone
        if len(feedback) > 0:
            self.feedback = feedback
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Users(name='James', email='jlee@example.com', phone='123456789', feedback='Collaboration is crucial!')
    u2 = Users(name='Susan', email='susanh123@example.com', phone='2067891234', feedback='What are some tools for '
                                                                                         'collaboration?')
    u3 = Users(name='John', email='jabcd@example.com', phone='651123456', feedback='Very informative website')
    u4 = Users(name='Emily', email='emily@example.com', phone='760123456', feedback='This website was a great study '
                                                                                    'resource.')
    table = [u1, u2, u3, u4]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {row.email}")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()
