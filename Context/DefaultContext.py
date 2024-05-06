class DefaultContext:

	@staticmethod
	def null():
		return 127
		
	@staticmethod
	def mediane(*args):
		args = list(args)
		args.sort()
		return args[len(args)//2]
