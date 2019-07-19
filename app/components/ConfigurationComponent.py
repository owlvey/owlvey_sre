import os


class ConfigurationComponent:
    def __init__(self):
        self.db_username = "root"
        self.db_password = "p@ssw0rd"
        self.db_name = "sredb"
        self.db_host = "localhost"

    def get_environment(self):
        return os.environ.get("environment") or "dev"

    def build_db_connection(self):
        return 'mysql+pymysql://{}:{}@{}/{}'.format(self.db_username,
                                                    self.db_password,
                                                    self.db_host,
                                                    self.db_name)
