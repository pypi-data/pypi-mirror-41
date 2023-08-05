# What is this?

This is a Flask extension to deal URL with [ULID](https://github.com/ulid/spec).


# How to install

$ pip install flask-ulid

# How to use

## Wrap Flask app

```python
from flask import Flask
from flask_ulid import FlaskULID

app = Flask(__name__)
FlaskULID(app)


@app.route('/article/<ulid:article_id>')
def article(article_id):
    return '{} is valid ulid'.format(article_id)
```

## Add converter for Flask app

```python
from flask import Flask
from flask_ulid import ULIDConverter

app = Flask(__name__)
app.url_map.converters['ulid'] = ULIDConverter


@app.route('/article/<ulid:article_id>')
def article(article_id):
    return '{} is valid ulid'.format(article_id)
```
