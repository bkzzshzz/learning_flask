##### August 20

### Models and Databases

Start with importing library.

`from flask_sqlalchemy import SQLAlchemy`

To start with an instance of the class
`db = SQLAlchemy`

> Those classes that are made into tables for a database are called Models. 

This creates the database file and gives the database a key.
`app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'`

To initiate and give attributes to a database:
```python
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode= db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
```
1. A class named *ITem* is created that imports the database Model.
2. `id = db.Column(db.Integer(), primary_key=True)` this is the identifier. The attribute `primary_key=True` assigns *id* as a unique identifier. 
3. `d.Column()` is a convention; `db.String(length=value)` rules that the data must be a string and the lenght of the string to that value.
4. `nullable=False` : It should not be a null(None).
5. `unique=True`: That the data must be unique

Now, I go the the terminal and type:
```python
from market import db
db.create_all()
```
The above command creates the database named *market.db*.

Now, to provide information to the database:
```python
from market import Item
item1 = Item(name="name", price=price, barcode="barcode", description="description")
db.session.add(item1)
db.session.commit()
```

And to check whether there's any entry in the data base or not: `Item.query.all()`

To view every item in the Item class of database, or the database.  
`Item.query_all()` stores all the data by columns. 
```python
for item in Item.query.all():
    item.name
    item.price
    item.description
    item.id
    item.barcode
```

To filter by a certain information:
`print(Item.query.filter_by(price=500))` which returns only the column with this value. But it returns a memory address. 
To actually extract data:
```python
for item in Item.query.filter_by(price=500):
    print(item.name)
```

### Project restructure:
It was all about creating a package of our application. For this we need to create a file named *__init__.py* where we import all the needed libraries from python library and variables from other files. 

**Side learning:**
To clear screen when python shell is open: `os.system('cls')`.
