# Generated by Django 3.2.10 on 2022-02-13 10:56

from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = "data.json"
DATA_FOLDER = "initial_data"


def load_data(apps, schema_editor):
    Shop = apps.get_model("shops_app", "Shop")
    jsonfile = Path(__file__).parents[2] / DATA_FOLDER / DATA_FILENAME

    with open(str(jsonfile), encoding="utf-8") as datafile:
        objects = json.load(datafile)
        for obj in objects["elements"]:
            try:
                objType = obj["type"]
                if objType == "node":
                    tags = obj["tags"]
                    name = tags.get("name", "no-name")
                    longitude = obj.get("lon", 0)
                    latitude = obj.get("lat", 0)
                    location = fromstr(f"POINT({longitude} {latitude})", srid=4326)
                    Shop(name=name, location=location).save()
            except KeyError:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ("shops_app", "0001_initial"),
    ]

    operations = [migrations.RunPython(load_data)]
