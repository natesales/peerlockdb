from os import environ
from flask import Flask, request, redirect, session
from flask.json import jsonify
from requests_oauthlib import OAuth2Session

pdb_client_id = environ.get("PDB_OAUTH_CLIENT_ID")
pdb_client_secret = environ.get("PDB_OAUTH_CLIENT_SECRET")

authorization_base_url = "https://auth.peeringdb.com/oauth2/authorize"
token_url = "https://auth.peeringdb.com/oauth2/token"

app = Flask(__name__)


@app.route("/login")
def login():
    github = OAuth2Session(pdb_client_id)
    authorization_url, state = github.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session["oauth_state"] = state
    return redirect(authorization_url)


@app.route("/auth/redirect")
def callback():
    github = OAuth2Session(pdb_client_id, state=session["oauth_state"])
    token = github.fetch_token(token_url, client_secret=pdb_client_secret, authorization_response=request.url)
    return jsonify(github.get("https://auth.peeringdb.com/oauth2/profile/v1").json())


app.run()
