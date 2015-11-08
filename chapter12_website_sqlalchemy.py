import datetime
import sqlalchemy as sqa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = "article"
    # article_id = sqa.Column(sqa.Integer, primary_key=True, autoincrement=True)
    rowid = sqa.Column(sqa.Integer, primary_key=True)
    article_title = sqa.Column(sqa.String)
    article_message = sqa.Column(sqa.String)
    article_publish_date = sqa.Column(sqa.DateTime)

    def __init__(self, title, message):
        self.article_title = title
        self.article_message = message
        self.article_publish_date = datetime.datetime.now()

class Comment(Base):
    __tablename__ = "Comment"
    # comment_id = sqa.Column(sqa.Integer, primary_key=True, autoincrement=True)
    rowid = sqa.Column(sqa.Integer, primary_key=True)
    article_id = sqa.Column(sqa.Integer, sqa.ForeignKey("article.rowid"))
    article = sqa.orm.relationship(Article, backref="comments")
    comment_name = sqa.Column(sqa.String)
    comment_message = sqa.Column(sqa.String)
    
    def __init__(self, article_id, name, message):
        self.article_id = article_id
        self.comment_name = name
        self.comment_message = message

engine = sqa.create_engine('sqlite:///chapter12_website_db.db')
Base.metadata.create_all(engine)
Session = sqa.orm.sessionmaker(bind=engine)
    
        
