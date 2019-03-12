from Csv_processor import *
import sys
if __name__ == '__main__':
	fname = sys.argv[1]
	table = sys.argv[2]

	m_inst = Csv_processor(fname, table)
	m_inst.load_csv()
	m_inst.set_header()
	if len(sys.argv) > 3:
		date_opt = str(sys.argv[3]).replace("'", '')
		date_col = str(sys.argv[4]).replace("'", '')
		print('Date opt: ' + date_opt)
		print('Date col: ' + date_col)
		print(len(date_opt))
		for i in range(0, len(date_opt)):
			print(date_opt[i])
		print(len('datetime'))
		m_inst.fix_dates(date_col,date_opt)
	m_inst.gen_statements()
