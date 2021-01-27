from os import environ, urandom
from flask import Flask, request, redirect, session
from requests_oauthlib import OAuth2Session
import logging
from rich.logging import RichHandler

logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
log = logging.getLogger("rich")
log.info("Starting PeerlockDB API")

pdb_client_id = environ.get("PDB_CLIENT_ID")
pdb_client_secret = environ.get("PDB_CLIENT_SECRET")
if not pdb_client_id:
    log.fatal("PDB_CLIENT_ID environment variable is not defined")
    exit(1)
if not pdb_client_secret:
    log.fatal("PDB_CLIENT_SECRET environment variable is not defined")
    exit(1)

pdb_auth_url = "https://auth.peeringdb.com/oauth2/authorize/"
pdb_token_url = "https://auth.peeringdb.com/oauth2/token/"
pdb_profile_url = "https://auth.peeringdb.com/profile/v1"

app = Flask(__name__)
app.secret_key = urandom(32)


@app.route("/")
def login():
    peeringdb = OAuth2Session(pdb_client_id)
    authorization_url, state = peeringdb.authorization_url(pdb_auth_url)
    session["oauth_state"] = state
    return redirect(authorization_url)


@app.route("/auth/redirect")
def callback():
    peeringdb = OAuth2Session(pdb_client_id, state=session["oauth_state"])
    peeringdb.fetch_token(token_url=pdb_token_url, authorization_response=request.url.replace("http", "https"), client_secret=pdb_client_secret, client_id=pdb_client_id)
    print(peeringdb.get(pdb_profile_url).json())
    return "hi"


app.run()
