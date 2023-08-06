The [Python port](https://github.com/textile/python-textile) of Dean Allen's [humane web text generator](https://www.textile-lang.com) packaged for use with [Flask](http://flask.pocoo.org).

    pip install flask-textile

Import into our project:

    from flask_textile import Textile

And then...

    app = Flask(__name__)
    textile = Textile(app)

Or, if one prefers, with an [application factory](http://flask.pocoo.org/docs/1.0/patterns/appfactories/):

    textile = Textile()

    def create_app(config_class=Config):
        app = Flask(__name__)
        app.config.from_object(config_class)
        textile.init_app(app)
        #...

Simple usage within a Jinja2 template:

    {{ text|textile }}

Or use as a filter:

    {% filter textile %}
    h2. Textile

    * is a _shorthand syntax_ used to generate valid HTML
    * is *easy* to read and *easy* to write
    * can generate complex pages, including: headings, quotes, lists, tables and figures

    Textile integrations are available for "a wide range of platforms":/article/.
    {% endfilter %}

Additionally, Flask-Textile offers a static method, `parse()`, which returns a raw HTML sting from Textile input—i.e. the direct output of python-textile. (Useful for working with Textile outside of a template):

    from flask_textile import Textile
    Textile.parse(text)

    # Or if you already have an instance laying around...
    app = Flask(__name__)
    textile = Textile(app)
    #...
    textile.parse(text)
