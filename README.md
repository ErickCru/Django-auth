# Ingresar mediante Google +

Ejemplo básico que te permite loguearte con tu cuenta de google obteniendo los datos de tu cuenta.


## Instruciones de uso

- Instalar las librerías necesarias.

```
    pip install -r requirements.txt
```

- Adecuar los datos para la conexión con el API de Google +.

```
    Abrir el arcivo settings.py y llenar con los datos que te proporciona Google.
    * SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
    * SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
```

- Uso

```
    Terminal: 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

    Navegador:
    http://localhost:8000/accounts/login/
```


## Referencias
[Social Auth](https://github.com/python-social-auth/social-examples)