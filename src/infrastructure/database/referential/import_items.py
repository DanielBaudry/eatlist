import csv

from app import app
from src.infrastructure.database.models import ItemSQLEntity
from src.infrastructure.database.models.db import db


#
# CSV format: [nom de l'item]
#
def import_items_in_database(csv_path: str) -> None:
    with app.app_context():
        csv_file = open(csv_path, newline='')
        csv_reader = csv.reader(csv_file, delimiter=',')
        _save_new_item_to_database(csv_reader)
        csv_file.close()
    print("Import terminé avec succès")


def _save_new_item_to_database(csv_reader: iter) -> None:
    for row in csv_reader:
        item_name = row[0]
        item = db.session.query(ItemSQLEntity) \
            .filter(ItemSQLEntity.name == item_name) \
            .first()
        if not item:
            item = ItemSQLEntity()
            item.name = item_name
            db.session.add(item)
            db.session.commit()
