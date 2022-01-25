
"""
********************************************************************************************
Module:     api
Prefix:     /api
Purpose:    create all the routes for the api

requests api docs: https://docs.python-requests.org/en/latest/api/#requests.request

********************************************************************************************
"""
from __future__ import annotations
import requests
import flask
from . import enums, globals as g
from .structs import SingleRequest

#------------------------------------------------------
# Forward the incoming flask request to the external destination
# This is a flask url rule view function
# It's added by calling add_url_rule to the flask application
#------------------------------------------------------
def forward(endpoint: str) -> flask.Response:
    response = sendExternalRequest(flask.request, endpoint)
    return toFlaskResponse(response)


#------------------------------------------------------
# Sends a translated flask.Request object to the external api
# Returns the external api's response
#------------------------------------------------------
def sendExternalRequest(flask_request: flask.Request, endpoint: str) -> requests.Response:
    
    body = SingleRequest(
        method  = flask_request.method,
        url     = f'{g.url}{endpoint}',
        auth    = g.auth,
        params  = flask_request.args.to_dict(),
        files   = flask_request.files.to_dict(),
        data    = _getData(flask_request),
        headers = flask.request.headers,
        cookies = flask.request.cookies,
    )

    return sendRequest(body)


#------------------------------------------------------
# Transform a requests.Response into a flask.Response (tuple)
#------------------------------------------------------
def toFlaskResponse(response: requests.Response) -> tuple:
    return (response.text, response.status_code, response.headers.items())


#------------------------------------------------------
# Get the request data payload
# If the incoming request mimetype is a form, return the form data
# Otherwise, return the raw request data
#------------------------------------------------------
def _getData(flask_request: flask.Request) -> dict | bytes:
    if flask_request.mimetype in enums.ParsedMimeTypes.values():
        payload = flask_request.form.to_dict()
    else:
        payload = flask_request.get_data()

    return payload

#------------------------------------------------------
# combine the global url prefix with the path specified in the flask request 
#------------------------------------------------------
def _buildUrl(flask_request: flask.Request) -> str:
    suffix = _getViewPathEndpoint(flask_request)
    return f'{g.url}{suffix}'

#------------------------------------------------------
# get the path value in the flask request object
#------------------------------------------------------
def _getViewPathEndpoint(flask_request: flask.Request) -> str:
    return list(flask_request.view_args.values())[0]

#------------------------------------------------------
# Send a pyrequests 
#------------------------------------------------------
def sendRequest(request_body: SingleRequest) -> requests.Response:
    return requests.request(
        method  = request_body.method,
        url     = request_body.url,
        auth    = request_body.auth,
        params  = request_body.params,
        files   = request_body.files,
        data    = request_body.data,
        headers = request_body.headers,
        cookies = request_body.cookies,
    )
