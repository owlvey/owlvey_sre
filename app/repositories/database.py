import threading

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.core.QueryEntity import QueryEntity
from app.components.ConfigurationComponent import ConfigurationComponent

#  add reference to register automatic creation

from app.core.UserEntity import UserEntity
from app.core.CustomerEntity import CustomerEntity
from app.core.SubscriptionEntity import SubscriptionEntity

configuration = ConfigurationComponent()

if configuration.get_environment() == "prod":
    engine = create_engine(configuration.build_db_connection(), convert_unicode=True)
elif configuration.get_environment() == "dev":
    engine = create_engine('sqlite:///dev.db')
    QueryEntity.metadata.create_all(bind=engine)
else:
    engine = create_engine('sqlite://')
    QueryEntity.metadata.create_all(bind=engine)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

QueryEntity.query = db_session.query_property()


def db_init():
    QueryEntity.metadata.create_all(bind=engine)



