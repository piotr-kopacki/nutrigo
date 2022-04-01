<h1 align="center">nutrigo</h1>
<p align="center">Calculate nutrition for your favourite recipe!</p>
<p align="center">
  <img alt="Coveralls github branch" src="https://img.shields.io/coveralls/github/MakuZo/nutrigo/1.0.0-dev">
<img alt="Travis (.com)" src="https://img.shields.io/travis/com/MakuZo/nutrigo/1.0.0-dev.svg">
</p>
<p align="center">Try live <a href="https://oneciabatta.dev/nutrigo">here</a></p>
<p align="center">
<img align="center" width="70%" height="70%" src="https://i.imgur.com/7zhqcxq.jpg"></img>
</p>

## Overview

Nutrigo uses basic parsing techniques and USDA's Food Database to calculate nutrition for recipes.
Nevertheless it provides good results for well-structured and uncomplicated recipes (ingredient list).

## Installing

nutrigo requires [Python](https://www.python.org/) 3.6+ to run.

Install the dependencies using [Pipenv](https://github.com/pypa/pipenv), download corpora and run the server.

```sh
$ pipenv install --dev
$ python3 -m textblob.download_corpora
$ python3 manage.py runserver
```

## Usage

Open your web browser, type ```localhost:8000``` and enter recipe url.

## Running with Docker Compose

```sh
$ docker-compose build nutrigo
$ docker-compose up nutrigo
```

## Supported websites
--Note that parsing third-party websites is only possible by using API Endpoint /api/calculate-from-url

So far the only supported websites are:
Yummly.com, KwestiaSmaku.com

Adding support for a recipe website is very simple. See recipe.py for examples.

## Running the tests

```sh
$ pytest
```

## Contribution

Feel free to contribute to the project by creating pull requests!

## Built With

* [Django](https://www.djangoproject.com/) - Python Web framework
* [Django REST framework](https://www.django-rest-framework.org/) - Django REST framework

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
