import hashlib
from flask import session

def hash_pass(password):
  # used to hash the password similar to how MySQL hashes passwords with the password() function.
  hash_password = hashlib.sha1(password.encode('utf-8')).digest()
  hash_password = hashlib.sha1(hash_password).hexdigest()
  hash_password = '*' + hash_password.upper()
  return hash_password

def is_authenticated():
  return "email" in session and "organization_id" in session

