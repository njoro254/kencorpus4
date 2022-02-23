from flask import Blueprint
from .api import HomeAPI, HomePDFAPI, AboutAPI, LoginAPI, CareersAPI, LocationAPI, DoctorsAPI


guest_app = Blueprint("guest_app", __name__)


homeapi_view = HomeAPI.as_view('home_api')

guest_app.add_url_rule('/',
	view_func=homeapi_view, 
	methods=['GET'])

homepdfapi_view = HomePDFAPI.as_view('homepdf_api')

guest_app.add_url_rule('/pdf',
	view_func=homepdfapi_view, 
	methods=['GET'])

aboutapi_view = AboutAPI.as_view('about_api')

guest_app.add_url_rule('/about',
	view_func=aboutapi_view, 
	methods=['GET'])


loginapi_view = LoginAPI.as_view('login_api')

guest_app.add_url_rule('/login',
	view_func=loginapi_view, 
	methods=['GET'])


careersapi_view = CareersAPI.as_view('careers_api')

guest_app.add_url_rule('/careers',
	view_func=careersapi_view, 
	methods=['GET'])


doctorsapi_view = DoctorsAPI.as_view('doctors_api')

guest_app.add_url_rule('/doctors',
	view_func=doctorsapi_view, 
	methods=['GET'])


locationapi_view = LocationAPI.as_view('location_api')

guest_app.add_url_rule('/location',
	view_func=locationapi_view, 
	methods=['GET'])