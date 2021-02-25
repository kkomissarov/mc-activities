import os

import config
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

db_string = f'postgresql://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}'
engine = create_engine(db_string)

Base = declarative_base(bind=engine)
metadata = MetaData(bind=engine)

session = sessionmaker(bind=engine)()







