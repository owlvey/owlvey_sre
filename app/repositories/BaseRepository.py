from app.components.ConfigurationComponent import ConfigurationComponent
import mysql.connector

from app.core.BaseFrame import BaseFrame


class BaseRepository:
    def __init__(self, configuration: ConfigurationComponent):
        self._configuration = configuration

    def _build_connection(self):
        db = mysql.connector.connect(
          host=self._configuration.db_host,
          user=self._configuration.db_username,
          passwd=self._configuration.db_password,
          database=self._configuration.db_name,
          auth_plugin='mysql_native_password'
        )
        return db

    def _list(self, frame: BaseFrame):
        try:
            db = self._build_connection()
            cursor = db.cursor()
            cursor.execute("SELECT {} FROM {}".format(",".join(frame.get_metadata()), frame.get_schema()))
            frame.load_data(list(cursor))
        finally:
            if db:
                db.close()
            if cursor:
                cursor.close()

        return frame

    def _get_one(self, frame, key):
        try:
            db = self._build_connection()
            cursor = db.cursor()
            cursor.execute("SELECT {} FROM {} where {}=%s".format(
                ",".join(frame.get_metadata()),
                frame.get_schema(), frame.get_metadata()[0]),
                [key]
            )
            frame.load_data(list(cursor))
        finally:
            if db:
                db.close()
            if cursor:
                cursor.close()

        return frame

    def _delete_one(self, frame, key):
        try:
            db = self._build_connection()
            cursor = db.cursor()
            cursor.execute("delete FROM {} where {}=%s".format(
                frame.get_schema(), frame.get_metadata()[0]), [key]
            )
            frame.load_data(list(cursor))
        finally:
            if db:
                db.close()
            if cursor:
                cursor.close()

        return frame

