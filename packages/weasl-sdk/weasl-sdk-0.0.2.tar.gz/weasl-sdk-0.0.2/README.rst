# Python Weasl SDK

This package is the Python integration for authentication powered by [Weasl](https://www.weasl.in)

## Examples

Here are a couple examples you can use to get started:


### Flask


```
from flask import Flask, jsonify, session
from weasl.integrations.flask import login_required

app = Flask(__name__)
app.config['WEASL_CLIENT_ID'] = 'YOUR CLIENT ID'


@app.route('/me')
@login_required
def user():
    return jsonify(session.current_user)

```
