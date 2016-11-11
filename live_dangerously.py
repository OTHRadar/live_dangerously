#!/usr/bin/python
import sys, getopt

SHORT_DESC = 'short_desc'
LONG_DESC = 'long_desc'

risk = {
	1: {
		SHORT_DESC: 'No Risk',
		LONG_DESC: 'Provides simple or uninteresting suggestions.'
	},
	2: {
		SHORT_DESC: 'Mild Risk',
		LONG_DESC: 'Provides slightly interesting suggestions.'
	},
	3: {
		SHORT_DESC: 'Normal Risk',
		LONG_DESC: 'Most things are included, but nothing outlandish.'
	},
	4: {
		SHORT_DESC: 'High Risk',
		LONG_DESC: 'Might include some weird/unthought of options.'
	},
	5: {
		SHORT_DESC: 'Extreme Risk',
		LONG_DESC: 'Fuck me up, fam.'
	}
}

def print_usage(program_name):
	print program_name + ' -t <type of decision to make> -r <risk factor of decision> -n <number of decisions to output>'

def get_system_arguments(argv):
	type = ''
	risk = 3
	number = 1
	if len(argv) == 1:
		print 'No arguments specified. Running with defaults.'
	try:
		opts, args = getopt.getopt(argv[1:],'ht:r:n:',['help','type=','risk=','number='])
	except getopt.GetoptError:
		print_usage(argv[0])
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('h', 'help'):
			print_usage(argv[0])
	
if __name__ == '__main__':
	get_system_arguments(sys.argv)