#insert statement
from Query import *
class Insert_statement(Query):
	def __init__(self, values = [], columns = [], table='', **kwargs):
		super().__init__('Insert', values, table)
		self._columns = columns

		
	@property
	def columns(self):
		return self._columns
	@columns.setter
	def columns(self, col_values):
		return


	def construct_query(self):

		lst_str_delim = ', '
		tmp_cols = ''
		#columns must be strings otherwise join will fail
		if len(self._columns) > 1:
			tmp_cols = lst_str_delim.join(self._columns)
		else: tmp_cols = str(self._columns[0])
		#values must also be strings 
		self._value_cleanse()
		tmp_vals = lst_str_delim.join(self._values)
		self._query_str = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(self.table, tmp_cols, tmp_vals)
		print(self._query_str + " HERE")
		return
	def _value_cleanse(self):
		for i in range(0, len(self._values)-1):
			self._values[i] = str(self._values[i])
		return







