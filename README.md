# Liturgical App

A simple app to display the current liturgical colour of the Church of England.

It gets its data from the [Liturgical API](https://github.com/liturgical-app/liturgical-api), which in turn is based on the [Liturgical Calendar](https://github.com/liturgical-app/liturgical-calendar)
library.

It has a simple UI written with [Flask](https://pypi.org/project/Flask/) and [Bootstrap](https://getbootstrap.com/). It is written as a [progressive web app](https://en.wikipedia.org/wiki/Progressive_web_app)
so it can easily be added to your homescreen as an app icon. The [Latin Cross](https://icons8.com/icon/A51q2n9iZRkQ/latin-cross) icon was
provided by [Icons8](https://icons8.com).

This app can be self-hosted, or there is a free-to-use instance hosted at [liturgical.uk](https://liturgical.uk)

## Develop

The app can be run locally for testing with

```sh
flask run
```

## Build

This project can be built as a Docker image with

```sh
docker build -t liturgical-calendar:dev .
```

## Pull image

```console
docker pull ghcr.io/liturgical-app/liturgical-app:latest
```

- Stable releases are built as image tags, e.g. `1.0.0`
- The `latest` tag points to the latest stable release
- The `edge` tag is built from the latest commit to `main`

## Run

A [Helm chart](https://artifacthub.io/packages/helm/liturgical/liturgical-app)
is available for deploying on Kubernetes.

## Configure

This app takes only one config option as an environment variable.

* `LITURGICAL_API_URL` - URL of a Liturgical API server. The default is `https://api.liturgical.uk` and you should not normally need to override this, unless you are hosting your own Liturgical API.

## Issues

[Issues](https://github.com/liturgical-app/liturgical-app/issues) should
be logged against this project for problems with the UI only.
Problems relating to the calculations of dates, colours and the calendar of
feasts should be logged against the
[Liturgical Calendar](https://github.com/liturgical-app/liturgical-calendar/issues) library.

PRs are welcome, but should pass the Pylint tests.