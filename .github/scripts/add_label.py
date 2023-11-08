import os
from ghapi.core import GhApi

owner, repo = os.environ['REPO'].split('/')
number = os.environ['NUMBER']

api = GhApi(owner=owner, repo=repo)

api.issues.add_labels(number, labels=['bug'])
