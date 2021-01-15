# pokemonapi
pokemonapi is a Django API that you can use to managey our pokemon trainers, pokemon teams and pokemon themselves. The pokemon information is retrieved from http://pokeapi.co/

## Installation
Clone the repo to your computer and then activate the virtual environment to use this API

```bash
env\Scripts\activate
```

Since this project uses a mySQL database to store your information, you need to create a mySQL database with the name 'pokemon'. The user should be called 'user' and shouldn't have a password. If you want to edit this settings (or if your mySQL database isn't connected to the port 3306), you can modify this in pokemonapi/settings.py

```bash
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'pokemon',
        'USER':'user',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
```

## Usage

There are 3 endpoints for each model: trainers, teams and pokemon. If you want to create a new instance of any of this, you can POST a new object by going to the URL

```bash
http://localhost:8000/api/trainers
http://localhost:8000/api/pokemon
http://localhost:8000/api/teams
```

If you want to update/delete/get any specific object, you can access each one by id

```bash
http://localhost:8000/api/trainers/1
```

Since each time you get the information for a pokemon you make an API call to pokeapi.co, to diminish the amount of requests per second given to that API, when listing pokemons you only get 1 result per page.
