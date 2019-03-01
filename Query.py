#query object

class Query:
	def __init__(self, q_type, values = [], table = ''):
		self._q_type = q_type
		self._values = values
		self._table = table
		self._query_str = 'test'
	@property
	def q_type(self):
		return self._q_type
	@q_type.setter
	def q_type(self, params):
		self.q_type = q_type 
	@property
	def values(self):
		return self._values
	@values.setter
	def values(self, values):
		#if not isinstance(values, list):
			#raise TypeError('Must be int')
		#self._values = values
		return
	
	@property
	def table(self):
		return self._table
	@table.setter
	def table(self, table_val):
		return
	@property
	def query_str(self):
		return self._query_str
	@query_str.setter
	def query_str(self, q_str_value):
		self._query_str = q_str_value
		#return
	def _construct_query(self):
		return ''
	def __repr__(self):
		return self._query_str
	
