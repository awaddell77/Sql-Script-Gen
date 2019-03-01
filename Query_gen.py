#Sql_script_gen
from Insert_statement import *
class Query_gen:
	def __init__(self,params):
		
		self._params = params

	def gen_query(self):
		try:
			q_type = self._params['type']
			if q_type.lower() == 'insert':
				f_query = Insert_statement( 
					self._params['values'], 
					self._params['columns'], 
					self._params['table']
					)
				f_query.construct_query()
			
		except TypeError as TE:
			raise Param_type_error("params must be dict")
		except KeyError as KE:
			raise Param_key_error("Cannot find key in params: {0}".format(str(KE)))
		return f_query

class Param_type_error(TypeError):
	pass
class Param_key_error(KeyError):
	pass




