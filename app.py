import master_api
import dbman as db

from flask_restful import Api

from sqlalchemy.orm import (
    sessionmaker, scoped_session
)

from sqlalchemy.orm.exc import (
    NoResultFound
)

from model import (
    db_schemas, Login, LoginFailed
)

from services import (
    remadness
)

from security import (
    Passwrod, HashesDoNotMatch
)

from flask import (
    Flask, make_response, redirect, url_for, request, g,
        abort, session, render_template, current_app
)

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(remadness.bp)

api = Api(app)
master_api.register_endpoints(api)

db.create_all()
db_session = scoped_session(sessionmaker(bind=db.engine))

app.secret_key = 'hah!!!'


@app.before_request
def share_db_session():
    g.db_session = db_session


@app.teardown_appcontext
def close_db_session(exception=None):
    if 'db_session' in g:
        db_session.remove()
        g.pop('db_session')


@app.route('/', methods=['GET'])
def index():
    cookies = request.cookies

    if request.method == 'GET':
        #TODO: check if session cookie exists and if it does, redirect to usercp
        response = make_response(
            redirect(url_for('mglogin'))
        )

        return response


@app.route('/usercp/', methods=['GET', 'POST'])
def usercp():
    cookies = request.cookies

    if request.method == 'GET':
        response = make_response(
            render_template('usercp.html')
        )


#Create api endpoint for this with PUT and GET methods to manage user's cloud apps using AJAX
@app.route('/cloudapps/', methods=['GET'])
def cloudapps(token=None, target=None):
    cookies = request.cookies

    if request.method == 'GET':
        #TODO: check if user logged in
        #TODO: create json schema with cloud apps and pass it to render_template
        logged_in = 1
        if logged_in:

            #TODO: get user by session id

            response = make_response(
                render_template('cloudapps.html')
            )





@app.route('/mglogin/', methods=['GET', 'POST'])
def mglogin():
    cookies = request.cookies
    session['pip'] = 1

    '''if request.method == 'GET':
        #TODO: generate public key and save it to cookie to be used by script in brwsr
        #TODO: implement session cookie creation
        response = make_response(
            render_template('mglogin.html', wrong_creds=False)
        )

        return response

    if request.method == 'POST':
        login = Login(
            request.form['username'],
            request.form['passwrod']
        )

        try:
            session_id = login.auth()
            response = make_response(
                redirect(url_for('usercp'))
            )

        except LoginFailed:
            response = make_response(
                render_template('mglogin.html', wrong_creds=True)
            )

        finally:
            return response'''



    salt = Passwrod.RandomGenerator.get_random_string(50)

    passwrod = Passwrod(
        '11111111', salt
    )

    user = db_schemas.User(username='f1', email='ff', phone=444, passwrod=passwrod.get_hash(), salt=salt, plan='r',
                           device_amount=5, cloudapps=db_schemas.null())

    salt = Passwrod.RandomGenerator.get_random_string(50)

    passwrod = Passwrod(
        '11111111', salt
    )


    user1 = db_schemas.User(username='f', email='ff1', phone=444, passwrod=passwrod.get_hash(), salt=salt, plan='r', device_amount=5, cloudapps={'pidor': db_schemas.JSON.NULL})

    db.DBSessionMan.get_session().add(user)
    db.DBSessionMan.get_session().add(user1)
    db.DBSessionMan.get_session().commit()

    return 'dd'
