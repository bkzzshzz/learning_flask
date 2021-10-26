#### September 13

## Flash and Advanced Validations

Now we are talking. Flask does things in ways so peculiar but it does work. 

First I `from flask import flash`. *flash* as the name suggests is used for flashing(displaying) informations. 

`flash(f'There was an error creating user: {err_msg}', category='danger')` The category danger is defining what category the message belongs to. 

```h
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">
                    <button type="button" class="m1-2 mb-2" data-dismiss="alert" aria-label="="Close>
                        <span aria-hidden="true">&times;</span>
                    </button>
                    {{ message }}
                </div>
            {% endfor %}

        {% endif %}
    {% endwith %}
```
The information for first line: `{% with messages = get_flashed_messages(with_categories=true) %}` is sent from `flash(f'There was an error creating user: {err_msg}', category='danger')`. It looks so sophisticated, 

Then I move to the point where we validate things. 
```py
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different usrename')

    
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists.')
```

To use the **ValidationError** keyword, I have to `from wtforms import ValidationError`.

If we see the funtion names, we see we used *validate_(text)*. The text should be the variable name that we want to validate. 




