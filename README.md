# Flask-Altair-VueJs-Vuetify Example

_An demonstration of data-visualization web app with basic dashboard UI_

![Flask Logo](/docs/flask-logo.png "Flask Logo")
![Altair logo](docs/altair-logo.png "altair Logo")
![Vue Logo](/docs/vue-logo.png "Vue Logo")
![Vuetify Logo](/docs/vuetify-logo.png "Vuetify Logo")

## Intro
This example is built upon Gui Talarico's [Flask-Vuejs-Template](https://github.com/gtalarico/flask-vuejs-template) with additional inspirations from these following online resources:
* [xhochy/altair-vue-vega-example](https://github.com/xhochy/altair-vue-vega-example)
* [oleg-agapov/flask-vue-spa](https://github.com/oleg-agapov/flask-vue-spa)
* [oleg-agapov/basic-spa-vue-firebase](https://github.com/oleg-agapov/basic-spa-vue-firebase/tree/part-1)


## Features
* Flask backend with [Flask-RestPlus](http://flask-restplus.readthedocs.io) API
* [Altair](https://altair-viz.github.io/) plotting and Vega spec json object serving from backend
* [Vega](https://vega.github.io/vega/) and [Vega-Embed](https://github.com/vega/vega-embed) for plot rendering at frontend
* [vue-cli 3](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md) + yarn
* [Vuex](https://vuex.vuejs.org/) state management
* [Vue Router](https://router.vuejs.org/)
* [Vuetify material design](https://vuetifyjs.com/en/) for dashboard UI
* [Axios](https://vuex.vuejs.org/) for backend communication
* Heroku Configuration with one-click deployment + Gunicorn

## Demo
[Live Demo](https://flask-altair-vuejs-vuetify-exp.herokuapp.com/#/api)

## Repo Structure and Usage

The details on the directory structure and usage can be found in the `README.md` file of Gui Talarico's [repo](https://github.com/gtalarico/flask-vuejs-template). For reader's convenience, here I will only copy and paste the [key files](#Key-Files) and some basic [installation](Installation) instructions below.

#### Key Files

| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/app`               | Flask Application                          |
| `/app/api`           | Flask Rest Api (`/api`)                    |
| `/app/client.py`     | Flask Client (`/`)                         |
| `/src`               | Vue App .                                  |
| `/src/main.js`       | JS Application Entry Point                 |
| `/public/index.html` | Html Application Entry Point (`/`)         |
| `/public/static`     | Static Assets                              |
| `/dist/`             | Bundled Assets Output (generated at `yarn build` |


## Installation

##### Before you start

Before getting started, you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install#mac-stable)
- [X] Vue Cli 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3
- [X] Pipenv (optional)
- [X] Heroku Cli (if deploying to Heroku)

##### Template and Dependencies

* Clone this repository:

	```
	$ git clone git@github.com:xujiboy/flask-vega-vuejs-vuetify-example.git
	```

* Setup virtual environment, install dependencies, and activate it:

	```
	$ pipenv install --dev
	$ pipenv shell
	```

* Install JS dependencies

	```
	$ yarn install
	```


## Development Server

Run Flask Api development server:

```
$ python run.py
```

From another tab in the same directory, start the webpack dev server:

```
$ yarn serve
```

The Vuejs application will be served from `localhost:8080` and the Flask Api
and static files will be served from `localhost:5000`.

The dual dev-server setup allows you to take advantage of
webpack's development server with hot module replacement.

Proxy config in `vue.config.js` is used to route the requests
back to Flask's Api on port 5000.

If you would rather run a single dev server, you can run Flask's
development server only on `:5000`, but you have to build build the Vue app first
and the page will not reload on changes.

```
$ yarn build
$ python run.py
```


## Production Server and Heroku Deployment

Please refer to the `README.md` file of Gui Talarico's [repo](https://github.com/gtalarico/flask-vuejs-template).
