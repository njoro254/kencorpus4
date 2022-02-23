from flask.views import MethodView
from flask import request, abort, jsonify, render_template, redirect, url_for, session,send_from_directory, make_response, send_file
from prints.auth.api import build_preflight_response
from prints.auth.decorators import auth_required

# from prints.modules.reception.models import *
# from prints.modules.billing.models import *

# import pdfkit, os



class HomeAPI(MethodView):
	def options(self):
		if request.method == 'OPTIONS':
			return build_preflight_response()


	def get(self):
		bodytitleparagraph="Newlife Hospital is committed to provide compassionate care and <br> excellent service that transcends conventional healthcare."
		bodytitle="MEDICAL SERVICES"
		title="Hargeisa Obstetrics and Gynaecology"
		return render_template("homepage/guest/index.html",title=title, bodytitle=bodytitle,bodytitleparagraph=bodytitleparagraph,)



class HomePDFAPI(MethodView):
	def options(self):
		if request.method == 'OPTIONS':
			return build_preflight_response()


	def get(self):
		# Visits.objects.all().delete()
		# Patients.objects.all().delete()
		# ModuleVisit.objects.all().delete()
		return ("pdf to page")
# 		# bodytitleparagraph="Newlife Hospital is committed to provide compassionate care and <br> excellent service that transcends conventional healthcare."
# 		# bodytitle="MEDICAL SERVICES"
# 		# title="Hargeisa Obstetrics and Gynaecology"
# 		# rendered = render_template("homepage/guest/sample.html")
# 		# rendered = render_template("homepage/guest/index.html",title=title, bodytitle=bodytitle,bodytitleparagraph=bodytitleparagraph,)
# 		# config=pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
# 		name = 'samplehomepage.pdf'
# 		url = 'https://hgh-obs.com'
# 		dirs = "./docs/documentation/pdfhtml"
# 		files = os.path.join(dirs, name)
# 		pdf = pdfkit.from_url(url, files )
# 		#, configuration=config)


# 		# pdf  = pdfkit.from_url(url , name)
# 		# with open("searchpatients.pdf", "w") as f:
# 		# 	f.write(pdf)
# 		# pdf = pdfkit.from_string(rendered, False)
# 		return send_from_directory(dirs, name, name)

		# return str(type(pdf))


		# response = make_response(pdf)
		# response.headers['Content-Type']='application/pdf'
		# response.headers['Content-Disposition']='inline: filename=homepage.pdf'
		# return response


class AboutAPI(MethodView):
	def options(self):
		if request.method == 'OPTIONS':
			return build_preflight_response()


	def get(self):
		return render_template("homepage/guest/aboutus.html")




class LoginAPI(MethodView):

	def options(self):
		if request.method == 'OPTIONS':
			return build_preflight_response()


	def get(self):
		return render_template("homepage/guest/login.html")



class CareersAPI(MethodView):

	def options(self):
		if request.method == 'OPTIONS':
			return build_preflight_response()


	def get(self):
		return render_template("homepage/guest/careers.html")


class DoctorsAPI(MethodView):

	def options(self):
		if request.method == 'OPTIONS':
			return build_preflight_response()


	def get(self):
		return render_template("homepage/guest/doctors.html")


class LocationAPI(MethodView):

	def options(self):
		if request.method == 'OPTIONS':
			return build_preflight_response()


	def get(self):
		return render_template("homepage/guest/ourlocation.html")