
# "data": [{"AGE": 59.0, "SEX": 2.0, "BMI": 32.1, "BP": 101.0, "S1": 157.0, "S2": 93.2, "S3": 38.0, "S4": 4.0, "S5": 4.8598, "S6": 87.0}]}
# http://23.99.112.112:80/api/v1/service/sugarmodel/score

import requests
import json
import ast
check=''
def passing_data(inputs):
# URL for the web service
	scoring_uri = 'http://23.99.112.112:80/api/v1/service/sugarmodel/score'
	# If the service is authenticated, set the key or token
	key = ''

	# Two sets of data to score, so we get two results back
	data = {"data": [{"AGE": inputs['age'], "SEX": inputs['sex'], "BMI": inputs['bmi'], "BP": inputs['bp'], "S1": 70.0, "S2": 93.2, "S3": 38.0, "S4": 4.0, "S5": 4.8598, "S6": 91.0}]}
	# Convert to JSON string
	input_data = json.dumps(data)

	# Set the content type
	headers = {'Content-Type': 'application/json'}
	# If authentication is enabled, set the authorization header
	# headers['Authorization'] = f'Bearer {key}'

	# Make the request and display the response
	resp = requests.post(scoring_uri, input_data, headers=headers)
	check=resp.text
	check=ast.literal_eval(check)
	check=ast.literal_eval(check)
	check=check['result']
	check=check[0]
	return check
