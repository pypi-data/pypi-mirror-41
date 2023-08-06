# Nice HTTP authentication support for Django

This is a common base for supporting multiple auth methods in an app.

Right now, we provide only the HTTP Basic auth module; but you can easily add your own specific schemes, if you need them, and more generic ones are going to be added in the future (see Planned features).

## Requirements
* Django 2.0+

## Installation
```sh
pip install dj-authentication
```

### settings.py
* Add `'dj_authentication'` to the list of `INSTALLED_APPS`.
* Remove `'django.contrib.auth.middleware.AuthenticationMiddleware'` from the list of `MIDDLEWARE`s.
* Add `dj_authentication.request_http_auth.HTTPAuthMiddleware` to the list of `MIDDLEWARE`s.
* Choose backends used for determining `request.user`, for example:
```python
REQUEST_USER_BACKENDS = [
    'dj_authentication.methods.basic', # HTTP Basic Auth
    'django.contrib.auth',
]
```

## Tips
To trigger an authentication dialog in a browser, if the user is not authenticated:
```python
if not request.user.is_authenticated:
    return HttpResponse(status=401)
```
Note: this requires `dj_authentication.methods.basic` backend.

## Planned features
* Support for Bearer scheme with JWT tokens verified against an OAuth/OIDC auth server thru [`jwks_uri`](https://tools.ietf.org/html/rfc8414#section-2)
* Support for Bearer scheme with opaque tokens verified against an OAuth/OIDC auth server thru [Introspection Endpoint](https://tools.ietf.org/html/rfc7662)
* Support for client certificates (see also [OAuth 2.0 Mutual TLS](https://tools.ietf.org/html/draft-ietf-oauth-mtls-12))
* Support for [OIDC `private_key_jwt` scheme](https://openid.net/specs/openid-connect-core-1_0.html#ClientAuthentication)
