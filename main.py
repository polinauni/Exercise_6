#Exercise 06
#1

def power (a, b):
    if a <= 0 or b <= 0:
        return -1
    if b == 0:
        return 1
    else:
        return (a*power(a, b-1))


#2
def binary_search(numbers, num):
    first_index = 0
    size = len(numbers)
    last_index = size - 1
    mid = len(numbers) // 2 #midpoint of the list
    is_found = True
    while is_found:
        if first_index == last_index:
            if mid != num:
                is_found = False
                return -1 #here we checked if the mid element is the one we look for (num)
            #and if not, we returned -1
        elif numbers[mid] == num:
            return mid #if it's the one, we return its index number
        elif numbers[mid] > num:
            index = binary_search(numbers[:mid], num) #here we see if the element num in the left half of the list
            if index == -1:
               return -1
            else:
                return index #here we return the index of the element looked for
             #now the same goes for the right half of the list
        else:
             index = binary_search(numbers[mid+1:], num)
             if index == -1:
                return -1
             else:
                return index + mid + 1 #here we adjust the returned index from the right half so that
             #the element we look for gets the correct index from the list and not just from the half
