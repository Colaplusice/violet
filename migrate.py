import os
from datetime import datetime

from peewee import AutoField, CharField, DateTimeField
from werkzeug.utils import import_string

from app.extensions import db


class MigrateRecord(db.Model):
    created_at = DateTimeField(default=datetime.now())
    name = CharField(null=False)
    migrate_id = AutoField()


def run():
    """
    database make migrate
    integration with flask-script
    usage: python run.py migrate
    """
    if not db.database.table_exists("migraterecord"):
        db.database.create_tables([MigrateRecord])
    package_name = "app/migrations"
    if not os.path.exists(package_name):
        raise FileNotFoundError('migration is not exist!')
    file_list = os.listdir(package_name)
    migration_list = []
    for file in file_list:
        if not file.endswith(".py") or file == "__init__.py":
            continue
        import_name = package_name.replace("/", ".") + "." + file[:-3] + ":migrate_up"
        function = import_string(import_name)
        migration_list.append((file[:-3], function))
    migrate_records = {record.name for record in MigrateRecord.select()}
    for migrate in migration_list:
        if migrate[0] not in migrate_records:
            try:
                migrate[1]()
                MigrateRecord.create(**{"name": migrate[0]})
                print('migrate success :{}'.format(migrate[0]))
            except Exception:
                raise Exception
