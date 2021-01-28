from sqlalchemy import Table

from base import metadata, Base


class ManagementCompany(Base):
    __table__ = Table('management_companies', metadata, autoload=True)


class Activity(Base):
    __table__ = Table('activities', metadata, autoload=True)


class IssueType(Base):
    __table__ = Table('issue_types2', metadata, autoload=True)
