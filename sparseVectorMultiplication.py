class sparseVector():
	def __init__():
		return 

	def multiplication(vec1, vec2):
		assert type(vec1) is dict and type(vec2) is dict, 'Not correct data type!'
		mul_res = 0
		for k, v in vec1.iteritems():
			try:
				mul_res += vec1[k] * vec2[k]
			except:
				pass

		return nul_res

