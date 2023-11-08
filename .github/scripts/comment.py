import os
from ghapi.core import GhApi

owner, repo = os.environ['REPO'].split('/')
number = os.environ['NUMBER']

api = GhApi(owner=owner, repo=repo)
api.issues.create_comment(number, "Hi! I'm making a comment from a GH Action!")
