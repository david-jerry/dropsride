# dropsride

Ride hailing app with affordable driver subscriptions per location

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

-   To populate all **countries_plus**, use this command:

        $ python manage.py update_countries_plus  

-   To get **currencies supported within the app**, use this command:

        $ python manage.py get_currency_exchange   

-   To populate **supported banks in nigeria**, use this command:

        $ python manage.py get_ng_banks 

-   To generate **webpack for PWA**, use this command:

        $ python manage.py webpack_init                

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

ALso on generation of the webpack directory you can choose to run your **yarn or npm**
commands from root directory or within your desired frontend directory name

### Type checks

Running type checks with mypy:

    $ mypy dropsride

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

This is handled by the **yarn or npm** command:
    $ npm install    
    $ npm start    
    $ npm build    

**or for yarn**
    $ yarn install    
    $ yarn start    
    $ yarn build    

### Tailwindcss Support and DaisyUI
This is generated and managed with **yarn or npm** commands:
    $ npm tailwind init    
    $ npm watch    

**or for yarn**
    $ yarn tailwind init    
    $ yarn watch    

## Deployment

The following details how to deploy this application.

### Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).
