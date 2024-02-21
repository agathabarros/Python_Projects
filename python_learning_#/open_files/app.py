import operations

operations.save_to_file('Rolf', 'data_test.txt')

from operations import save_to_file, read_file

save_to_file('Rolf', 'data_test.txt')
print(read_file('data.txt'))