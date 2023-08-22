import re

def formatIsOk(str):
  regExp = re.compile(r"^[a-zA-Z0-9_]+$")
  return regExp.search(str)

def hasSpace(str):
  regExp  = re.compile(r"^\s*$")
  return regExp.search(str)