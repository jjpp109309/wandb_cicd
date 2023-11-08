import os
from ghapi.core import GhApi

owner, repo = os.environ['REPO'].split('/')
number = os.environ['NUMBER']

api = GhApi(owner=owner, repo=repo)

label = api.issues.create_label('bug', color="ff0000")
api.issues.add_labels(number, labels=['bug'])
