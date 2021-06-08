import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapi.settings')
django.setup()
from api.models import Institution, InstitutionType


def parse():
    with open('institutions.csv') as f:
        reader = csv.reader(f, delimiter=';')

        for row in reader:
            print(row)
            typename, full_name, name, director, address, phone_number, site_url = row

            institution_type = InstitutionType.objects.get_or_create(name=name)

            data = {
                'type': institution_type[0],
                'full_name': full_name,
                'short_name': name,
                'director_name': director,
                'address': address,
                'phone_number': phone_number,
                'site_url': site_url
            }

            institution = Institution(**data)
            institution.save()


if __name__ == "__main__":
    parse()