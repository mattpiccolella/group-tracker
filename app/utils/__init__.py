import hashlib

def hash_pass(password):
  # used to hash the password similar to how MySQL hashes passwords with the password() function.
  hash_password = hashlib.sha1(password.encode('utf-8')).digest()
  hash_password = hashlib.sha1(hash_password).hexdigest()
  hash_password = '*' + hash_password.upper()
  return hash_password