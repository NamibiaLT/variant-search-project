# Create Flask App
# variant_search_app/fullstack/__init__.py
import os
from flask import Flask, render_template
from flask_scss import Scss

# @app.route("/")
# def index():
#     return "Sample Page"

# @app.route("/table")
# def genomic_table(variant_info):
#     return 'This is the table with genomic variant info: {}'.format(variant_info)

# if __name__ == '__main__':
#     app.run(debug=True)

def create_app(script_info=None):

    from logging.config import dictConfig

    # Set up logging at DEBUG level ...
    # From here: http://flask.pocoo.org/docs/dev/logging/
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'DEBUG',
            'handlers': ['wsgi']
        }
    })

    # instantiate the app
    app = Flask(
        __name__,
        #template_folder="../fullstack/templates",
        #static_folder="../static",
    )

    Scss(app)

    ### register blueprints
    from variant_search_app.fullstack.views import fullstack_blueprint

    app.register_blueprint(fullstack_blueprint)

    ### error handlers
    @app.errorhandler(401)
    def unauthorized_page(error):
        return render_template("errors/401.html"), 401

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/500.html"), 500

    ## Clear cache:
    @app.after_request
    def add_header(response):
        response.cache_control.max_age = 1
        return response

    return app
