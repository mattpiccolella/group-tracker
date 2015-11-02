from app import db
from datetime import datetime
from flask.ext.mongoengine.wtf import model_form

class Organization(db.Document):
    """An organization model.

    :ivar date_created: :class:`mongoengine.fields.DateTimeField` - The date
        that this user was created.
    :ivar date_modified: :class:`mongoengine.fields.DateTimeField` - The date
        the this user was last modified.
    :ivar name: :class:`mongoengine.fields.StringField` - The name of the organization.
    :ivar email: :class:`mongoengine.fields.EmailField` - The email of the organization.
    :ivar password: :class:`mongoengine.fields.
        address.
    """

    date_created = db.DateTimeField(required=True, default=datetime.now())
    date_modified = db.DateTimeField(required=True, default=datetime.now())
    name = db.StringField(required=True, max_length=510)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, max_length=510)

    # MongoEngine ORM metadata
    meta = {
        'allow_inheritance': True,
        'indexes': ['email', ]
    }

    def hash_pass(password):
        # used to hash the password similar to how MySQL hashes passwords with the password() function.
        hash_password = hashlib.sha1(password.encode('utf-8')).digest()
        hash_password = hashlib.sha1(hash_password).hexdigest()
        hash_password = '*' + hash_password.upper()
        return hash_password

    def clean(self):
        """Called by Mongoengine on every ``.save()`` to the object.

        Update date_modified.
        Hash the password.

        :raises: :class:`wtforms.validators.ValidationError`
        """
        self.date_modified = datetime.now()

    def __repr__(self):
        """The representation of this user.

        :returns: The user's details.
        :rtype: str
        """
        return '<User name={}, email={}>'.format(self.name, self.email)
