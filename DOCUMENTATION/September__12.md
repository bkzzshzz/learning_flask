##### September 12

## Flask Forms

Creating a form using Flask with the help of jinja conventions.

I don't know why but I need to set up a secret key(maybe it's to ensure security). So, I go the terminal and generate 12 digit hex numeral by:
```python
import os
print(os.urandom(12).hex())
``` 

And in the *__init__.py* file:
```python
app.config['SECRET_KEY'] = 'bbdf39c755e204a1ecfad191'
```

In the *forms.py* file:
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='User Name')
    email_address = StringField(label='Email Address')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Create Account')
```
**flask_wtf** and **wtforms** are built-in libraries to manage forms from where we import *FlaskForm, StringField, PasswordField and SubmitField*

`label='text` gives a name to the variable which is displayed later. 

Created a route for form register:
```python
@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)
```

```html
<body class="text-center">
    <div class="container">
        <form method="POST" class="form-register" style="color:white">
            <img class="mb-4" src="https://res.cloudinary.com/jimshapedcoding/image/upload/v1597332609/android-icon-192x192_ove2a7.png" alt="">
            <h1 class="h3 mb-3 font-weight-normal">
                Please Create Your Account
            </h1>
            <br>
            {{ form.username.label() }}
            {{ form.username(class="form-control", placeholder="User Name") }}

            {{ form.email_address.label() }}
            {{ form.email_address(class="form-control", placeholder="Email Address") }}
            
            {{ form.password1.label() }}
            {{ form.username(class="form-control", placeholder="Password") }}
            
            {{ form.password2.label() }}
            {{ form.username(class="form-control", placeholder="Confirm Password") }}

            <br>
            {{ form.submit(class="btn btn-tg btn-black btn-primary") }}
        </form>
    </div>
</body>
```

Now, here's an interesting one. 
1. `{{ form.username.label() }}` accesses the label of the variable called *username*.
2. `{{ form.username(class="form-control", placeholder="User Name") }}` creates the text-area and gives the text-area a placeholder.

## Form Validations

1. `from wtforms.validators import Length, EqualTo, Email, DataRequired` these built-in modules help in form validations. 
2. `username = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])` checks if the username is greater than 1 or less than 31 characters. `password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])` checks if the *password2* is equal to *password1*.

```python
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                            email_address=form.email_address.data,
                            password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: #if no errors from validations
        for err_msg in form.errors.values():
            print(f'There was an error creating user: {err_msg}')
    return render_template('register.html', form=form)
```
1. This block of code checks if there are any errors and displays the error in formatted output. 
2. But first i need to include the methods like **GET** and **POST** for the route */register*. 
3. `form.validate_on_submit()` this checks if the submit button is pressed or not.


### Keynote:
If i want to import a function or a class from a file to another, then i have to do `from the_folder.the_file import the_class/the_function`