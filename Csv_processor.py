from dictionarify import *
from w_txt import *
from Query_gen import *
from datetime_gen import *

import os

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
	def fix_dates(self, date_column, date_opt):
		print("FIX DATES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		print("DATE COLUMN: {0} ".format(date_column))
		print("DATE OPT: {0} ".format(date_opt))
		d_t = "datetime"
		for i in range(0, len(self.data)):
			
			print(type(date_opt))
			if date_opt in d_t:
				d_time = time_gen()
				if not d_time: d_time = 'LOOOOOL'
				t_date = self.data[i][date_column].replace("'", '') 
				t_date = "'" + t_date + ' ' + d_time + "'"
				print("New date: " + t_date)
				self.data[i][date_column] = t_date
			
	def gen_statements(self):
		for i in range(0, len(self.data)):
			values = []
			for i_2 in range(0, len(self.header)): values.append(self.data[i].get(self.header[i_2]))
			params = {
				'type':'insert',
				'values':values,
				'columns':self.header,
				'table': self.table
			}
			tmp_q= Query_gen(params).gen_query()
			w_txt(str(tmp_q),  self.fname + ' statements.txt', os.getcwd() )
