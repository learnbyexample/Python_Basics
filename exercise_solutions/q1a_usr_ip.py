#!/usr/bin/python3

print('Please provide the following details')
name = input('Enter your name: ')
dept = input('Enter your department: ')
colg = input('Enter your college: ')

op_fmt = '{:<11}: {}'

print('\n------------------------------------')
print(op_fmt.format('Name', name))
print(op_fmt.format('Department', dept))
print(op_fmt.format('College', colg))


####### Alternate
#print('Please provide the following details')
#labels = ('Name', 'Department', 'College')
#usr_details = [input('Enter your ' + itm + ': ') for itm in labels]
#
#itm_size = len(sorted(labels, key=len)[-1]) + 1
#op_fmt = '{:<' + str(itm_size) + '}: {}'
#print('\n------------------------------------')
#for k,v in zip(labels, usr_details):
#    print(op_fmt.format(k, v))
