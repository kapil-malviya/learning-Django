from django.shortcuts import render
from django.core.cache import cache
# import pdb

# Create your views here.



def home(request):
	mv = cache.get('movie', 'has expired')
	# pdb.set_trace()
	if mv == 'has expired':
		cache.set('movie', 'Bahubali2', 50)
		mv = cache.get('movie')

	return render(request, 'testapp/course.html', {'xx':mv})


'''
# version will create another cache_key in the database 

def home(request):
	mv = cache.get_or_set('fee', 88, 50, version=2)
	return render(request, 'testapp/course.html', {'xx':mv})



# setting and getting many values 

def home(request):
	data = {'name':'kapil', 'owns':'owns', 'bike':'S1000RR'}
	cache.set_many(data, 50)
	mv = cache.get_many(data)
	print('data : ',mv)
	return render(request, 'testapp/course.html', {'xx':mv})



# delete cache_key from database

def home(request):
#	cache.delete('owns')                # delete *owns* cache_key
#	print('deleting owns cache_key from database')
	cache.delete('fee')   # it will delete *fee* cache_key with version=1 only
	print('deleting fee with version=1')
	cache.delete('fee', version=2)
	print('deleting fee cache_key with version=2')
	return render(request, 'testapp/course.html')



def home(request):
	cache.set('age', 27, 228)
	xx = cache.get('age')
	print('age : ', xx)
	return render(request, 'testapp/course.html')


# incr for increasing value by delta & decr for decreasing

def home(request):
	xx = cache.incr('age', delta=1)
	print('age : ', xx)
	return render(request, 'testapp/course.html')



# clear() for deleting all the data from database my_cache_table

def home(request):
	cache.clear()
	return render(request, 'testapp/course.html')

'''