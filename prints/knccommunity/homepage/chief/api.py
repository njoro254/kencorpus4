from flask.views import MethodView
from flask import request, abort, jsonify, render_template, redirect, url_for, session,send_from_directory
from prints.homepage.chief.models import ProcedureCosts
from prints.auth.api import build_preflight_response
from prints.auth.decorators import auth_required
from prints.auth.models import StaffProfiles
import json

class ProcedureCostAPI(MethodView):

	decorators =[auth_required]

	def options(self):
		if request.method == 'OPTIONS':
			return build_preflight_response()

	def get(self):
		try:
			procedurename = request.headers["procedurename"]
			return ProcedureCosts.objects.filter(procedurename=procedurename).to_json()
		except:
			return ProcedureCosts.objects().to_json()
		
		# procedurecostsdict=[]
		
		# for items in ProcedureCosts.objects.all():
		# 	a={}
		# 	a["procedurename"]=items.procedurename
		# 	a["procedurecost"]=items.procedurecost
		# 	procedurecostsdict.append(a)

		# return jsonify(procedurecostsdict)

	def post(self):
		savenewcost=ProcedureCosts(procedurename = request.json["procedurename"], procedurecost = request.json["procedurecost"])
		savenewcost.save()
		return jsonify({"success":savenewcost.procedurename+" and " +str(savenewcost.procedurecost)})



class ChiefVerifyAccountAPI(MethodView):

    decorators = [auth_required]

    def options(self):
        if request.method == 'OPTIONS':
            return build_preflight_response()


    def get(self):
        #form=UnVerifiedForm()
        unverified_dict={}
        for name in StaffProfiles.objects.filter(verification_status=False):
            unverified_dict[name.username]=False

        #checklist dict unverified users
        return jsonify(unverified_dict)


    def post(self):
        # verifiedusernames = json.loads(json.dumps(request.get_json()))
        verified, unverified=[],[]
        persons = request.json ["verified"]
        # for persons in verifiedusernames:
        for item in StaffProfiles.objects.filter(username=persons):
            # if verifiedusernames[persons]==True:
                # verified.append(persons)   
                item.update(acceptance_status=True, verification_status=True)
            # elif verifiedusernames[persons]==False:
                # unverified.append(persons) 
                # item.update(acceptance_status=False, verification_status=True)
            
        body={"status":{"verified":persons}}
        # ,"unverified":unverified}}
        return jsonify(body), 200
 