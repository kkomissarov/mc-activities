import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

DB_HOST = os.environ.get('WS_STAGE_HOST')

engine = create_engine(f'postgresql://postgres:postgres@{DB_HOST}:5432/smart_space_test')

Base = declarative_base(bind=engine)
metadata = MetaData(bind=engine)

session = sessionmaker(bind=engine)()







