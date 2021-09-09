##### September 8

### Model Relationships

This part of the tutorial shows the interaction and relationships between databases. 

First we create another class called User to store user-based infomations like username, passwords, email, ets.

```python
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False) #Cuz most hashkeys are 60 chars long
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)
```

1. `id = db.Column(db.Integer(), primary_key=True)` This is a must as it gives a unique id to each column.
2. The *password_hash* is **60 characters** as the encryption methods in flask mostly uses 60 characters. 
3. In `budget = db.Column(db.Integer(), nullable=False, default=1000)` the *default* keyword gives the default value to *budget*.
4. Now, this is important: `items = db.relationship('Item', backref='owned_user', lazy=True)`. `backref` does back reference to user module. `lazy=True` has to be set up 
to grab all the objects at once. 

```python
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode= db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
```
The `owner = db.Column(db.Integer(), db.ForeignKey('user.id'))` sets up the relationship. What *ForeignKey* it searches for the primary key the item is related to. The text inside *ForeignKey* should be in **lower case**

Now in terminal:
1. `db.drop_all()` deletes all the previously stored database items. 
2. `db.create_all()` creates new table. 
3. `db.session.rollback()` restores to the previous changes and commits of the database.
4. `item1.owner = User.query.filter_by(username='jsc').first().id` stating the owner. 
5. `item1 = Item.query.filter_by(name='Iphone 10').first()` The *first()* keyword grabs the specific object.  
6. `db.session.add(item)` and `db.session.commit()` to add items and to commit respectively.
7. `item1.owner` returns 1. 

### Flask Forms
