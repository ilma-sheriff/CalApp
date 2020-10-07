from datetime import datetime

import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False
events = []


@app.route("/", methods=["GET"])
def home():
    if not events:
    	# if event is empty then handle it gracefully
        response = dict(message="Most recent events not available")
    else:
    	# Return the most recent event logs
        response = events[-1]
    return response, 200


@app.route("/currentevents", methods=["GET"])
# Return most recent 10 event logs
def current_events():
    return jsonify(events[-10:][::-1]), 200


@app.route("/allevents", methods=["GET"])
# Returns all event logs
def all_events():
    return jsonify(events), 200


@app.route("/compute", methods=["GET"])
def compute():

    if "operation" in request.args:
        operation = request.args["operation"]
    if "user_name" in request.args:
        user_name = request.args["user_name"]
    else:
        return dict(error="Calculation Error", message="Invalid operation parameters"), 400
    result = 0
    # Check for the type and get the result
    try:
    	#addition
        if "+" in operation:
            compute = operation.split("+")
            result = int(compute[0]) + int(compute[1])
        #multiplication
        if "*" in operation:
            compute = operation.split("*")
            result = int(compute[0]) * int(compute[1])
        response = {"user_name": user_name, "updated_date": datetime.now(), "operation": operation, "result": result}
        events.append(response)
        return response, 200
    except Exception as e:
        return dict(error="Calculation Error", exception=str(e), message="Try again"), 400


@app.errorhandler(404)
def page_not_found(error):
    return dict(response="This page does not exist"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0")

# Home - Show the most recent event logs: http://0.0.0.0:5000/
# Show all event logs: http://0.0.0.0:5000/allevents