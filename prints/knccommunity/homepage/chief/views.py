from flask import Blueprint
from .api import *

chief_app = Blueprint("chief_app", __name__)


#Chief add procedure
procedurecost_view = ProcedureCostAPI.as_view('procedure_api')

chief_app.add_url_rule('/chief/procedurecosts',
	view_func=procedurecost_view, 
	methods=['POST', 'GET'])




# ADMIN USER ACCOUNT VERIFICATION
chiefverifyaccount_view = ChiefVerifyAccountAPI.as_view('chiefverifyaccount_api')

chief_app.add_url_rule('/chief/verify', 
	view_func=chiefverifyaccount_view, 
	methods=['POST', 'GET' ])