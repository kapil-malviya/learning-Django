from django import template

register = template.Library()


'''  fixing value to 5 

def truncate5(value) :
	result = value[0:5]
	return result
'''

def truncate_n(value, n) :
	result = value[0:n]
	return result




# register.filter('tcate5', truncate5)
register.filter('tcate', truncate_n)


"""   another way of registering filters :

@register.filter(name='tcate_n')
def truncate_n(value, n) :
	result = value[0:n]
	return result

"""