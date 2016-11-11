import sys

risk = {
	1: {
		SHORT_DESC: 'No Risk',
		LONG_DESC: 'Provides simple or uninteresting suggestions.'
	}
	2: {
		SHORT_DESC: 'Mild Risk',
		LONG_DESC: 'Provides slightly interesting suggestions.'
	}
	3: {
		SHORT_DESC: 'Normal Risk',
		LONG_DESC: 'Most things are included, but nothing outlandish.'
	}
	4: {
		SHORT_DESC: 'High Risk',
		LONG_DESC: 'Might include some weird/unthought of options.'
	}
	5: {
		SHORT_DESC: 'Extreme Risk',
		LONG_DESC: 'Fuck me up, fam.'
	}
}

def get_system_arguments(args):
	type = ''
	risk = 3
	number = 1

if __name__ == '__main__':
	get_system_arguments(sys.argv[1:])