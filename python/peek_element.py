# find first peek element in a given array, peek is the element which is greater than its adjacent elements. 
#
def find_peek_linear(a):
	for i in range(len(a)):
		if a[0] > a[1]:
			return a[0]
			break
		if i > 0:
			if _is_peek(a,i):
				return a[i]
				break


def find_peek_binary_search_recursion(a):
	mid = (len(a)-1)/2
	if len(a) == 1:
		return a[0]
	if _is_peek(a,mid):
		return a[mid]
	elif a[mid -1] > a[mid]:
		end = mid -1
		if end ==0:
			return find_peek_binary_search_recursion(a[:1])
		else:
			return find_peek_binary_search_recursion(a[:mid-1])
	elif a[mid-1] < a[mid]:
		return find_peek_binary_search_recursion(a[mid+1:])

def find_peek_binary_search_iterative(a):
	while(True):
		mid = (len(a)-1)/2
		if len(a) == 1:
			return a[0]
		if _is_peek(a,mid):
			return a[mid]
		elif a[mid -1] > a[mid]:
			end = mid -1
			if end ==0:
				a = a[:1]
			else:
				a = a[:mid-1]
		elif a[mid-1] < a[mid]:
			a = a[mid+1:]

def _is_peek(a,i):
	return (a[i] > a[i-1] and a[i] > a[i+1])

if __name__ == '__main__':
	a = [2,2,12,22,73,5,8]
	print find_peek_linear(a)
	print find_peek_binary_search_recursion(a)
	print find_peek_binary_search_iterative(a)



