from dictionarify import *
from w_txt import *
from Query_gen import *

class Csv_processor:
	def __init__(self, fname, table):
		self.fname = fname
		self.table = table
		self.data = ''
		self.header = []
	def load_csv(self):
		self.data =  dictionarify(self.fname)
	def set_header(self):
		self.header = list(self.data[0].keys())
	def gen_statements(self):
		for i in range(0, len(self.data)-1):
			values = []
			for i_2 in range(0, len(self.header)-1): values.append(self.data.get(self.header[i_2]))
			params = {
				'type':'insert',
				'values':values,
				'columns':self.header,
				'table': self.table
			}
			tmp_q= Query_gen(params).gen_query()
			w_txt(self.fname + ' statements.txt')
