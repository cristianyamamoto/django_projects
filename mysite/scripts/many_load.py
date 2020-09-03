import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, Region, Iso, State, Site

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Category.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    State.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name,description,justification,year,longitude,latitude,area_hectares,category,states,region,iso

    for row in reader:
        #print(row)

        cat, created = Category.objects.get_or_create(name=row[7])
        reg, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])
        sta, created = State.objects.get_or_create(name=row[8], region = reg)
        try:
            sit, created = Site.objects.get_or_create(name=row[0], description=row[1], justification=row[2], year=row[3], longitude=row[4], latitude=row[5], area_hectares=row[6], category = cat, state = sta, iso = iso)
        except:
            sit, created = Site.objects.get_or_create(name=row[0], description=row[1], justification=row[2], year=row[3], longitude=row[4], latitude=row[5], area_hectares=None, category = cat, state = sta, iso = iso)

        cat.save()
        reg.save()
        iso.save()
        sta.save()
        sit.save()