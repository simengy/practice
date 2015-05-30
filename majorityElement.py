def majority(array):

    dictionary = {}
    N = len(array)
    
    for key in array:
        if key not in dictionary:
            dictionary[key] = 1 
        else:
            print key, dictionary[key]
            dictionary[key] += 1
            
            if dictionary[key] > float(N) / 2.0:
                return key


array = [1,1,2,3,4,5,2,1,1,1,1]

print majority(array)
