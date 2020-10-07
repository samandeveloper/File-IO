#read & readlines
my_file=open('test.txt')
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.read())
print(my_file.readlines())

#read
with open ('test.txt', mode='r') as my_file:
	print(my_file.readlines())
	
#write
with open ('test.txt', mode='r+') as my_file:
	text=my_file.write('hey it\'s me')
	print(text)

#create a file & write in it
with open ('./sad2.txt', mode='w') as my_file:
	text=my_file.write(':(')
	print(text)

#file IO Errors
try:
	with open ('../sad.txt', mode='r') as my_file:
		print('my_file.read()')
except FileNotFoundError as err:
	print('file not exist')
	raise err
except IOError as err:
	print('IO error')
	raise err
	