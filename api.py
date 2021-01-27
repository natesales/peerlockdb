from os import environ, urandom
from typing import Optional
import logging

from flask import Flask, request, redirect, session, Response, jsonify
from pymongo.errors import DuplicateKeyError
from requests_oauthlib import OAuth2Session
from rich.logging import RichHandler
from rich.console import Console

from pymongo import MongoClient, ASCENDING

logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
log = logging.getLogger("rich")
log.info("Starting PeerlockDB API")
console = Console()

pdb_client_id = environ.get("PEERLOCKDB_PDB_CLIENT_ID")
if not pdb_client_id:
    log.fatal("PEERLOCKDB_PDB_CLIENT_ID environment variable is not defined")
    exit(1)

pdb_client_secret = environ.get("PEERLOCKDB_PDB_CLIENT_SECRET")
if not pdb_client_secret:
    log.fatal("PEERLOCKDB_PDB_CLIENT_SECRET environment variable is not defined")
    exit(1)

mongo_uri = environ.get("PEERLOCKDB_MONGO_URI")
if not mongo_uri:
    log.fatal("PEERLOCKDB_MONGO_URI environment variable is not defined")
    exit(1)

# PeeringDB OAuth URL constants
pdb_auth_url = "https://auth.peeringdb.com/oauth2/authorize/"
pdb_token_url = "https://auth.peeringdb.com/oauth2/token/"
pdb_profile_url = "https://auth.peeringdb.com/profile/v1"

app = Flask(__name__)
app.secret_key = urandom(32)

db = MongoClient(mongo_uri)["peerlockdb"]
db["users"].create_index([("peeringdb_id", ASCENDING)], unique=True)


def _resp(success: bool, message: str, data: Optional[object] = None) -> Response:
    """
    Return a JSON response
    :param success: Did the request succeed?
    :param message: What went wrong/right?
    :param data: Additional data
    :return:
    """
    return jsonify({
        "meta": {"success": success, "message": message},
        "data": data
    })


@app.route("/login")
def login() -> Response:
    """
    Log a user in through PeeringDB redirect
    :return:
    """
    peeringdb = OAuth2Session(pdb_client_id)
    authorization_url, state = peeringdb.authorization_url(pdb_auth_url)
    session["oauth_state"] = state
    return redirect(authorization_url)


@app.route("/auth/redirect")
def callback() -> Response:
    """
    Handle inbound PeeringDB redirect and validate user account
    :return:
    """
    peeringdb = OAuth2Session(pdb_client_id, state=session["oauth_state"])
    peeringdb.fetch_token(token_url=pdb_token_url, authorization_response=request.url.replace("http", "https"), client_secret=pdb_client_secret, client_id=pdb_client_id)
    pdb_resp = peeringdb.get(pdb_profile_url).json()
    if not (pdb_resp.get("verified_email") and pdb_resp.get("verified_user")):
        return _resp(False, "PeeringDB user is not verified")

    try:
        db["users"].insert_one({
            "email": json_body["email"],
        })
    except DuplicateKeyError: # User already exists
        return _resp(False, "User with this email already exists")

    console.log(pdb_resp)
    return _resp(True, "Authenticated against PeeringDB")


app.run()
