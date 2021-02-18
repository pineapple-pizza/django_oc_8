## the api
- `cd api`
- create a virtual env (`python3 -m venv venv`)
- activate virtual env (`. venv/bin/activate`)
- install dependencies (`pip3 install requirements.txt`)
- `python3 manage.py runserver`

## in the browser
- after last command, should open on : http://127.0.0.1:PORT/
- application is ready to be used
- after registration is done, email verification is sent and you should click on the link
- copy the given token in the email, click on "Authorize" and add in value : _Bearer(space) the given token_
- when the authorization is granted, you can use the /products/ route

## api routes
_can be used seperatly from the front (ex : on postman or in the browser alone)_
- `/api/register` (POST)
- `/api/login` (POST)
- `/api/email-verify/?token=` : 1 query param needed (**token**) (GET)
- `/products/` (GET)
- `/products/` (POST)
- `/products/favorites/` (GET)
- `/products/favorites/` (POST)
- `/products/id` (GET)
- `/products/id` (PUT)
- `/products/id` (PATCH)
- `/products/id` (DELETE)

## to start unit testing 
- `python3 manage.py test`

## the web app (vue.js)
- `cd client`
- `yarn install`
- to run the vue app : `yarn serve`
- to build the vue app (for prod or deployment purposes) : `yarn build`

## make a api/.env file
- export EMAIL_HOST_USER=your mailgun
- export EMAIL_HOST_PASSWORD=mailgun password

- SECRET_KEY = django secret key

- DEBUG = True

- DB_NAME=db name
- DB_USER=db username
- DB_PASSWORD=db password
- DB_HOST=127.0.0.1

## make a client/.env file
- VUE_APP_URL=LOCALHOST_URL OR DEPLOYED URL

- VUE_APP_VERIFIED_EMAIL=VERIFIED ACCOUNT
- VUE_APP_VERIFIED_PASSWORD=PASSWORD FROM THE SAME ACCOUNT

- VUE_APP_NEW_EMAIL=test_usercase@test.com
- VUE_APP_NEW_USERNAME=user_selenium
- VUE_APP_NEW_PASSWORD=123456

## for e2e testing 
- `cd client`
- `node selenium/TEST NAME` _(example : test_search_product.js)_
