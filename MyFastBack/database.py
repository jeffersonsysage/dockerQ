from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'mysql+pymysql://root:@mysql:3306/jdb'
# -x- SQLALCHAMY_DATABASE_URL = 'mysql+pymysql://root:@localhost:3306/jdb'
#     SQLALCHAMY_DATABASE_URL = 'mysql+pymysql://root:@127.0.0.1:3306/jdb'
# -x- SQLALCHAMY_DATABASE_URL = 'mysql+pymysql://root:@0.0.0.0:3306/jdb'
# SQLALCHAMY_DATABASE_URL = 'mysql+pymysql://root:@10.3.0.6:3306/jdb'
# -x- SQLALCHAMY_DATABASE_URL = 'mysql+pymysql://root:@host.docker.internal:3306/jdb'
#SQLALCHAMY_DATABASE_URL = 'mysql+pymysql://root:@10.3.0.5:3306/jdb'


engine = create_engine(SQLALCHAMY_DATABASE_URL, echo=False, pool_recycle=1200, pool_size=120)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

