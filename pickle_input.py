import pickle
data1 = {'a': [1, 2.0, 3, 4+6j],
	 'b': ('string', u'Unicode string'),
	 'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

with open('pickle_test_data.pkl', 'wb') as output:
	pickle.dump(data1, output)
	pickle.dump(selfref_list, output, -1)
