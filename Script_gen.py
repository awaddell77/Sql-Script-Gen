#script gen
from Query_gen import *
from w_txt import *
import os
class Script_gen:
	def __init__(self, fname, t_dir = os.getcwd() + os.sep):
		self.fname = fname
		self.t_dir = t_dir
	def single_q_create(self, q_params):
		tmp_q = Query_gen(q_params).gen_query()
		
		w_txt(tmp_q.query_str, self.fname,self.t_dir)


