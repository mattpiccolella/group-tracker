from app import db
from app.models.Member import Member
from app.models.Organization import Organization
from datetime import datetime

class Event(db.Document):
    name = db.StringField(required=True, max_length=500)
    attendees = db.ListField(db.ReferenceField(Member))
    created_at = db.DateTimeField(default=datetime.now, required=True)
    # Make a list later so we can co-host events.
    organization = db.ReferenceField(Organization)

    # MongoEngine ORM metadata
    meta = {
        'allow_inheritance': True,
        'ordering': ['-created_at']
    }

    def __repr__(self):
        return '<Event name={}>'.format(self.name)

