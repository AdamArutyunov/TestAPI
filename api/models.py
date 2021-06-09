from django.db.models import Model, TextField, CharField, ForeignKey, CASCADE
from django.forms.models import model_to_dict


class Institution(Model):
    short_name = TextField(null=True)
    full_name = TextField(null=False)
    type = TextField(null=True)
    director_name = TextField(null=True)
    address = TextField(null=True)
    phone_number = TextField(null=True)
    site_url = TextField(null=True)

    def to_dict(self):
        institution_dict = model_to_dict(self)

        return institution_dict
