<h1 align="center">nutrigo</h1>
<p align="center">Calculate nutrition for your favourite recipe!</p>
<p align="center">
  <img alt="Coveralls github branch" src="https://img.shields.io/coveralls/github/MakuZo/nutrigo/master.svg">
<img alt="Travis (.com)" src="https://img.shields.io/travis/com/MakuZo/nutrigo/master.svg">
</p>
<p align="center">Try live <a href="https://nutrigo.makuzo.usermd.net">here</a></p>
<p align="center">
<img align="center" width="70%" height="70%" src="https://i.imgur.com/3YKGyEt.jpg"></img>
</p>

## Overview

Nutrigo uses basic parsing techniques and USDA's Food Database to calculate nutrition for recipes.
Nevertheless it provides good results for well-structured and uncomplicated recipes (ingredient list).

## Installing

nutrigo requires [Python](https://www.python.org/) 3.6+ to run.

Install the dependencies, download WordNet and run the server.

```sh
$ pip install -r requirements.txt
$ python3 -m textblob.download_corpora
$ python3 manage.py runserver
```

## Usage

Open your web browser, type ```localhost:8000``` and enter recipe url.

## Running with docker

```sh
$ docker build -t nutrigo .
$ docker run --rm -it -p 8000:8000 nutrigo
```

## Supported websites

So far the only supported websites are:
Yummly.com, KwestiaSmaku.com

Adding support for a recipe website is very simple. See recipe.py for examples.

## Running the tests

```sh
$ pytest
```

## Contribution

Feel free to contribute to the project by making pull requests!

## Built With

* [Django](https://www.djangoproject.com/) - Python Web framework

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
