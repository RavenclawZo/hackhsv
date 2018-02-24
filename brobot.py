from bottlepy import request, route, run, template
import json
import requests
clientID='320307516676.320451889637'
clientSecret='5c5083b1dd14ba83a748e9fcf41a17e9'
@route('/hello/<name>', ['GET', 'POST'])
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
def get_reply(msg):
	if msg == "hey":
		return "hey back"
	else:
		return None
@route('/event', ['GET', 'POST'])
def event():
	print(request.json)
	incoming_message = request.json['event']['text']
	reply = get_reply(incoming_message)
	if reply:
		body={'text':reply}
		requests.post('https://hooks.slack.com/services/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', json=body)
	return 'hello'
run(host='localhost', port=8000)
