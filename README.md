# POST requests to JSON data sources in Denodo

The purpose of this repo is to demonstrate the use of Denodo's ability to perform a POST request using SQL. 

This repo is a nice example of the relatively undocumented ability to POST data to an API using Denodo.

> Denodo standard and well documented features include turning JSON data from an API into flattened views, as well as doing INSERT commands to JDBC databases.

## Instructions

Follow the below steps to explore this feature:

1. First, create a flask webapp using [these](https://scotch.io/bar-talk/processing-incoming-request-data-in-flask) intructions. The `app.py` file in this repo is based on those intructions, but it is worth following that tutorial first to understand the mechanics of flask.
	* Start the app using `python app.py`

1. Now notice the `app2.py` file in this repom which has been modified to return JSON format from the POST request, see [JSONIFY](https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view) details. The JSONIFY is necessary to ensure that the API returns whatever is posted to it in JSON format, which Denodo is able to turn into a virtual view.

1. Now to virtualize in Denodo. The VQL files contained in this repo contain all the details, and the VQL folder can be virtualized into Denodo.
	1. Import the `flask_post_api.vql` into Denodo using the Denodo IMPORT functionality.
	2. Notice that a data source, base view and flattened view is imported

1. We can now run queries against our flatted view in Denodo, such as `select * from f_post_api_test where lang  = \'TEST\'` which will execute a POST against the API, and return the results from the API.

## Notes



