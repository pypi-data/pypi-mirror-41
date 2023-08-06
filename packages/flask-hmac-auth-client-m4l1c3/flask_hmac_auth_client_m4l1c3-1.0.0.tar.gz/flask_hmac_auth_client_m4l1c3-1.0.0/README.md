# flask-hmac-auth-client
Python client library for flask-hmac-auth

# Use:
- Create an environment variable named APIKEY:

```bash
export APIKEY="WHATEVER_YOU_WANT!!!"
```
```python
from flask_hmac_auth_client import MessageAuthentication()
a = MessageAuthentication()
a.compute('a', 'a')
```
