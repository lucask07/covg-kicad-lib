# Lucas J. Koerner
# 2021/05/20
# parse KiCAD library and OpalKelly pins and create new KiCAD symbol
# koerner.lucas@stthomas.edu
# University of St. Thomas

'''
2021/06

'''

# standard library imports
import time
import sys

# imports that may need installation
import pandas as pd
library_file = 'xem6310.lib'  # input script file to be read 
output_file = 'xem7310.lib'  # file with test_net_name replaced based on Excel
csv_file = 'XEM7310.csv'
df = pd.read_csv(csv_file)


with open(library_file, 'r') as f:
	with open(output_file, 'w') as fout:
		for l in f:
			if ('JP2-' in l) or ('JP1-' in l):
				l = l.replace('JP', 'MC')
				j_pos = l.split()[2]
				jump_num = j_pos.replace('MC', '').split('-')[0]
				pin_num = int(j_pos.replace('MC', '').split('-')[1])

				desc = df.loc[df['Connector']=='MC{}'.format(jump_num)].loc[df['Pin']==pin_num]['Description'].item()

				total_split = l.split()

				# change the description 
				total_split[1] = desc 
				# change in/out/bidirectional
				# will keep these all the same 
				l = ' '.join(total_split)
				print(l)
				fout.write(l + '\n')
			else:
				fout.write(l)
