from application import db


class ProcedureCosts(db.Document):
	procedurename = db.StringField(db_field="procedurename")
	procedurecost  = db.IntField(db_field="procedurecost")