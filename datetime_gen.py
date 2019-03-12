
import random
def time_gen(t_range=''):
	if not t_range: t_range = 23
	time_st = ''
	hour = random.randint(1, t_range)
	if hour <= 9: hour = '0' + str(hour)
	else: hour = str(hour)
	minute = random.randint(0, 59)
	if minute <= 9: minute = '0' + str(minute)
	else: minute = str(minute)
	second = random.randint(0, 59)
	if second <= 9: second = '0' + str(second)
	else: second = str(second)
	time_st = hour + ':'+minute+':'+second
	return time_st

	#year


