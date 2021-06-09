import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapi.settings')
django.setup()
from api.models import Institution


def parse():
    with open('institutions.csv') as f:
        f.readline()
        reader = csv.reader(f, delimiter=';')

        for row in reader:
            typename, full_name, short_name, director, address, phone_number, site_url = row

            full_name = full_name.strip()
            typename = typename.strip()
            short_name = short_name.strip()
            director = director.strip()
            address = address.strip()
            site_url = site_url.strip()
            phone_number = ''.join(list(filter(lambda x: x.isdigit() or x in ',;', list(phone_number.strip()))))

            data = {
                'type': typename,
                'full_name': full_name,
                'short_name': short_name,
                'director_name': director,
                'address': address,
                'phone_number': phone_number,
                'site_url': site_url
            }

            institution = Institution(**data)
            institution.save()


if __name__ == "__main__":
    Institution.objects.all().delete()
    parse()
