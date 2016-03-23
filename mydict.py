class Dict(dict):
	def _init_(self,**kw):
	#**kw关键字参数，适用于字典。*args非关键字参数，适用于元组。
		super(Dict,self)._init_(**kw)
	def _getattr_(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" %key)
	def _setattr_(self,key,value):
		self[key]=value
		
	
			
			