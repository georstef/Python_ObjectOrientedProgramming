import cherrypy
from chapter12_website_sqlalchemy import Session, Article, Comment
from chapter12_website_jinja import templates

class Blog():
    @cherrypy.expose
    def index(self):
        session = Session()
        articles = session.query(Article).all()
        template = templates.get_template("index.html")
        content = template.render(articles=articles)
        session.close()
        return content
    
    @cherrypy.expose
    def add(self):
        template = templates.get_template("add.html")
        return template.render()

    @cherrypy.expose
    def process_add(self, title=None, message=None):
        session = Session()
        article = Article(title, message)
        session.add(article)
        session.commit()
        session.close()
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def process_comment(self, article_id, name=None, message=None):
        session = Session()
        comment = Comment(article_id, name, message)
        session.add(comment)
        session.commit()
        session.close()
        raise cherrypy.HTTPRedirect("/")

if __name__=="__main__":
    tutconf = 'E:/Python33/external 3rd party tools/CherryPy-3.2.4/cherrypy/tutorial/tutorial.conf'
    try:
        cherrypy.quickstart(Blog(), config=tutconf)
    except:
        cherrypy.close()

    
