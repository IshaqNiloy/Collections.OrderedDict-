from collections import OrderedDict

def item_name_and_net_price(ordered_dictionary):
    #Prints the dictionary
    for key, value in ordered_dictionary.items():
        print('{} {}'.format(key, value))


if __name__ == '__main__':
    #Initializing an ordered dictionary
    ordered_dictionary = OrderedDict()
    #Taking the input for number of items in the for loop
    for _ in range(int(input())):
        #The rpartition() method searches for the last occurrence of a specified string,          and splits the string into a tuple containing three elements. The first element          contains the part before the specified string. The second element contains the           specified string. The third element contains the part after the string.

        item, space, quantity = input().rpartition(' ')
        #get() method takes maximum of two parameters:
        #key - key to be searched in the dictionary
        #value (optional) - Value to be returned if the key is not found. The default             value is None.

        ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(quantity) 
        #Calls the function
    item_name_and_net_price(ordered_dictionary)

