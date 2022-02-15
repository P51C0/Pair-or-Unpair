import sys

def menu():
	print("""
Welcome to pair or unpair
""")

def pair_unpair():
	if int(sys.argv[1]) >= 1001:
		print(f'Error, the number {int(sys.argv[1])} is higher than 1000')

	elif int(sys.argv[1]) <= 0:
		print(f"Error, the number {int(sys.argv[1])} is less than 0 or is 0")

	elif int(sys.argv[1]) % 2 == 0:
		print(f'The number {int(sys.argv[1])} is pair')

	else:
		print(f'The number {int(sys.argv[1])} is unpair')


menu()
pair_unpair()
