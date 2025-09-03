# Liturgical Colour App

A simple app to display the current liturgical colour of the Church of England.

It is based on the [Liturgical Calendar](https://github.com/liturgical-app/liturgical-calendar)
library with a simple UI written with [Flask](https://pypi.org/project/Flask/)
and [Bootstrap](https://getbootstrap.com/).

It is written as a [progressive web app](https://en.wikipedia.org/wiki/Progressive_web_app)
so it can easily be added to your homescreen as an app icon.

The [Latin Cross](https://icons8.com/icon/A51q2n9iZRkQ/latin-cross) icon was
provided by [Icons8](https://icons8.com).

## Develop

The app can be run locally for testing with

```sh
flask run
```

PRs are welcome, but should pass the Pylint tests.

[Issues](https://github.com/liturgical-app/liturgical-app/issues) should
be logged against this project for problems with the UI only.
Problems relating to the calculations of dates, colours and the calendar of
feasts should be logged against the
[Liturgical Colour](https://github.com/liturgical-app/liturgical-calendar/issues) library.

## Build

This project can be built as a Docker image with

```sh
docker build -t liturgical-calendar:dev .
```

## Run

A [Helm chart](https://artifacthub.io/packages/helm/liturgical-app/liturgical-calendar)
is available for deploying on Kubernetes.

## Configure

This app takes only one config option as an environment variable.

* `LITURGICAL_API_URL` - URL of a Liturgical API server. The default is `https://liturgical-api.gazeley.uk` and you would not normally need to override this, unless you are hosting your own Liturgical API.