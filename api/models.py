from django.db.models import Model, TextField, CharField, ForeignKey, CASCADE


class InstitutionType(Model):
    name = TextField()


class Institution(Model):
    short_name = TextField()
    full_name = TextField()

    type = ForeignKey(InstitutionType, on_delete=CASCADE)

    director_name = TextField()
    address = TextField()
    phone_number = TextField()
    site_url = TextField()

