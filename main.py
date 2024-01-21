import functions_framework
from flask import redirect, flask
from firebase_admin import db

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args


    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    print(type(request_json))
    return request_json

def write_urls(request_json):
    # Grab the url parameters.
    callbackurl = request_json['callbackurl']
    #returnurl = request_json['returnurl']
    ref = db.reference('')
    if callbackurl is None:
        return flask.response("No callbackurl parameter provided", status=400)

    firestore_client: google.cloud.firestore.Client = firestore.client()

    # Push the new message into Cloud Firestore using the Firebase Admin SDK.
    _, doc_ref = firestore_client.collection("messages").add(
        request_json
    )

    # Send back a message that we've successfully written the message
    return flask.response(f"Message with ID {doc_ref.id} added.", status=200)