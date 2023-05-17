# Project: Putting it All Together

## Author: Darran Holmes

### Deployments
front-end: cookie-stand-admin-darran-holmes.vercel.app
back-end: cookie-stand-api-darran-holmes.vercel.app

### How to initialize/run your application

you will need to run pip install -r requirements.txt

docker compose run web python manage.py test

docker compose up or docker compose up --build

#### get request

http get 0.0.0.0:8000/api/v1/cookie/

#### post request

http post 0.0.0.0:8000/api/token/ username=yourUserName password=yourPassword

#### access data

http 0.0.0.0:8000/api/v1/cookie/ 'Authorization: Bearer pasteAccessTokenOverThisString'

## Tests

### How do you run tests?

docker compose run web python manage.py test