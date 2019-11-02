import os


def preprocessing():
	train_fire = os.listdir('../data/training/fire')
	train_not_fire = os.listdir('../data/training/not_fire')
	valid_fire = os.listdir('../data/validation/fire')
	valid_not_fire = os.listdir('../data/validation/not_fire')

	file = open('../data/data.txt', 'w')
	file.truncate(0)
	file.write('fire_notfire_filtered\n')
	file.write('|__ train\n')
	file.write('    |______ fire: [')
	for i in range(len(train_fire)):
		if i < len(train_fire) - 1:
			file.write(train_fire[i] + ', ')
		else:
			file.write(train_fire[i])
	file.write(']\n')
	file.write('    |______ not_fire: [')
	for i in range(len(train_not_fire)):
		if i < len(train_not_fire) - 1:
			file.write(train_not_fire[i] + ', ')
		else:
			file.write(train_not_fire[i])
	file.write(']\n')
	file.write('|__ validation\n')
	file.write('    |______ fire: [')
	for i in range(len(valid_fire)):
		if i < len(valid_fire) - 1:
			file.write(valid_fire[i] + ', ')
		else:
			file.write(valid_fire[i])
	file.write(']\n')
	file.write('    |______ not_fire: [')
	for i in range(len(valid_not_fire)):
		if i < len(valid_not_fire) - 1:
			file.write(valid_not_fire[i] + ', ')
		else:
			file.write(valid_not_fire[i])
	file.write(']\n')
	file.close()


