#query gen test
from Query_gen import *
from Script_gen import *
params = {
	'type':'insert',
	'values':[str(i) for i in range(0, 10)],
	'columns':['column '+ str(i) for i in range(1,11)],
	'table':'table_2'
	}
tst_res = Query_gen(params).gen_query()
m = Script_gen('test1.txt')
m.single_q_create(params)