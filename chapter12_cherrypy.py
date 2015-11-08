import cherrypy
import os.path

template = """<!DOCTYPE html>
<html>
<body>
{message}
</body>
</html>"""

class SimplePage:
    @cherrypy.expose
    def index(self):
        with open("chapter12_cherrypy.html") as file:
            return file.read()
    # index.exposed = True

class AboutPage:
    @cherrypy.expose
    def index(self):
        return template.format(message=" let's see this ")

@cherrypy.expose
def contactPage(self):
    print(self)
    return template.format(message=" contact")
    

class ContactFormPage:
    @cherrypy.expose
    def index(self, message=None, message2=None):
        if message:
            print("The user submitted:{0}".format(message))
            return 'Thank you!<br><a href="/">back</a>'
        return '<form><textarea name="message"></textarea><textarea name="message2"></textarea><input type="submit"/></form>'

class MainPage:
    about = AboutPage()
    contact = contactPage
    contact_form_page = ContactFormPage()

    @cherrypy.expose
    def index(self):
        return template.format(
            message='''this is the main page<br>
                <a href="/about/">About Me</a><br>
                <a href="/contact/">Contact Me</a><br>
                <a href="/contact_form_page/">Contact Form</a><br>
                <a href="/links/">Some Links</a>''')

    @cherrypy.expose
    def links(self):
        return template.format(message="No Links Yet")    

if __name__=="__main__":
    tutconf = 'E:/Python33/external 3rd party tools/CherryPy-3.2.4/cherrypy/tutorial/tutorial.conf'
    try:
        # cherrypy.quickstart(SimplePage(), config=tutconf)
        cherrypy.quickstart(MainPage(), config=tutconf)
    except:
        cherrypy.close()
                    
'''
there are 3 ways to add a page to a site
(besides the exposed method into the main class, like [links])
--------------------------------
1. By defining a separate function and including the attribute
   in the class definition as we did with [contactPage]
2. By defining a separate class and including an instance of it
   in the class definition, as we did with [AboutPage] + [ContactFormPage]
3. By adding the exposed method to the object after the class has been
   instantiated using code such as app.some_page = AnExposedClass() [????]
'''
