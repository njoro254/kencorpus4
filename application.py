from flask import Flask
from flask_mongoengine import MongoEngine
# from flask_mail import Mail


# from flask_cors import CORS
# cross_origin

from subprocess import call

from settings import MONGODB_SETTINGS, mail_settings

db = MongoEngine()








def create_app(**config_overrides):
    app = Flask(__name__)
    # mail = Mail(app)
    # CORS().init_app(app=app, resources={r"/*": {"origins": "*"}})
    # CORS(app)
    # ,  resources={r"/*": {"origins": "*"}})
    # .init_app(app=app, resources={r"/*": {"origins": "*"}})
    # app.config['CORS_HEADERS'] = 'Content-Type'


    # Load Config File
    app.config.from_pyfile('settings.py')

    # Apply Overrides for tests
    app.config.update(config_overrides)
    app.config.update(mail_settings)

    # Set up db
    db.init_app(app)

    # import blueprints
    from prints.auth.views import auth_app

    
    from prints.homepage.chief.views import chief_app
    from prints.homepage.staff.views import staff_app
    from prints.homepage.guest.views import guest_app

    
    
    from prints.modules.reception.views import reception_app
    from prints.modules.billing.views import billing_app


    from prints.modules.lab.views import lab_app

    from prints.modules.general.views import general_app
    from prints.modules.labour.views import labour_app
    from prints.modules.delivery.views import delivery_app
    

    from prints.modules.optheatre.views import optheatre_app
    from prints.modules.postnatal.views import postnatal_app
    from prints.modules.newborn.views import newborn_app
 

    
    # register blueprints    
    app.register_blueprint(auth_app)

    
    app.register_blueprint(chief_app)
    app.register_blueprint(staff_app)

    app.register_blueprint(reception_app)
    app.register_blueprint(billing_app)
    app.register_blueprint(guest_app)

    app.register_blueprint(lab_app)

    app.register_blueprint(general_app)
    app.register_blueprint(labour_app)
    app.register_blueprint(delivery_app)

    
    app.register_blueprint(optheatre_app)
    app.register_blueprint(postnatal_app)
    app.register_blueprint(newborn_app)


    return app
