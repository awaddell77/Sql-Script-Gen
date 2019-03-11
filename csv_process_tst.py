from Csv_processor import *
import sys
if __name__ == '__main__':
	fname = sys.argv[1]
	table = sys.argv[2]
	m_inst = Csv_processor(fname, table)
	m_inst.load_csv()
	m_inst.set_header()
	m_inst.gen_statements()
