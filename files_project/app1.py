my_file = open('data.txt', 'r') # r is for read mode 
file_content = my_file.read()

my_file.close() #is really important to close the file

print(file_content)

user_name = input('Enter your name: ')

my_file_writing = open('data.txt', 'w') # w is for write mode
my_file_writing.write(user_name)

my_file_writing.close() 


