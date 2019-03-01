#entity db crawler
from Db_mngr import *
from custom_errors import *
class S_dumicola(Db_mngr):
	def __init__(self, params):
		try:
			super().__init__(params['user'], params['password'], params['database'], params['host'])
			self.entity_parent = params['entity_table']
			
		except KeyError as KE:
			raise Param_key_error("Cannot find key in params: {0}".format(str(KE)))
	def analyze_table(self, table):
		pass
	def generate_row(self, table):
		pass
		




class Table:
	def __init__(self):
		self._p_keys = []
		self._f_keys = []
	@property
	def p_keys(self):
		return self._p_keys




