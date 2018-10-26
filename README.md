# Webapps in Denodo

1. First, create a flask webapp using [these](https://scotch.io/bar-talk/processing-incoming-request-data-in-flask) intructions. The app.py file in this repo is based on those intructions, but it is worth following that tutorial first to understand the mechanics of flask.

1. Now notice the app2.py file in this repom which has been modified to return JSON format from the POST request, see [JSONIFY](https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view) details.

1. Now to virtualize in Denodo. The VQL files contained in this repo contain all the details, and the VQL folder can be virtualized into Denodo.

1. We can now run queries against our base view in Denodo, such as 'select * from f_post_api_test where lang  = \'TEST\'' which will execute a POST against the API, and return the results from the API.

