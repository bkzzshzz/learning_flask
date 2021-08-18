##### August 18

## Setting up flask environment

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'
```

### After having typed this, we go to the terminal and set the FLASK_APP to the filename by: 
`export FLASK_APP=market.py`

For windows we use `set` instead of `export`

### And to run
`flask run`

### To turn on the debug mode:
`export FLASK_DEBUG=1`

> Why debug mode? Cuz, we have to exit the server everytime we make any changes to it and then re-run it to see if the changes occured. Turning on the debug mode removes this hassle. 

### To set debug mode off
`esport FLASK_DEBUG=0`

### Dynamic routes
```python
@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'
```

In `def hello_world()` there is no arguement. But in `def about_page(username)` the arguement is username as it needs to be passed. The *username* part in `@app.route('/about/<username>')` acts as a variable.

### render_template

This is a built-in library that renders the html file. Syntax: `render_template('filename)`.

### Iteration in HTML using Jinja

```python
@app.route('/market')
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150},
    ]
    return render_template('market.html', items=items)
```
```html
{% for item in items %}
<tr>
    <td>{{ item.id }}</td>
    <td>{{ item.name }}</td>
    <td>{{ item.barcode }}</td>
    <td>${{ item.price }}</td>
    <td>
        <button class="btn btn-outline btn-info">More Info</button>
        <button class="btn-outline btn-success">Puchase</button>
    </td>
</tr>
{% endfor %}
```

It's amazing how the Jinja convention works. 

### Template Inheritance

Inheriting certain lines of codes from a base HTML page to other pages.

1.`{% extends '<template_html>' %}` inherits the entire page of the template_html page. 
2. `{% block <blockname> %}` - `{% endblock %}` creates a block and fills in the place of that block with the blockname.
3. `{% for item in items %}` - `{% endfor %}` now isn't this sweet. The main file sends items to items by `return render_template('market.html', items=items)`




