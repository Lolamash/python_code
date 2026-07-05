import pprint, pickle

with open('pickle_test_data.pkl', 'rb') as pkl_file:
	data1 = pickle.load(pkl_file)
	pprint.pprint(data1)
	data2 = pickle.load(pkl_file)
	pprint.pprint(data2)

