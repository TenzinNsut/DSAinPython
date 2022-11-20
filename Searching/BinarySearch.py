
# Listing all of the possible edge cases:
"""
1.) query is the middle of cards.
2.) query is the first element in the card
3.) query is the last element in the card
5.) cards does not contain query
6.) cards is empty
7.) cards contain repeated elements
8.) multiple query elements present in the card
"""

from jovian.pythondsa import evaluate_test_cases

test = []

# query is the middle of cards.
test.append({
       'input':{
        'cards': [8,7,6,5,4,3,2,1,0],
        'query': 4,
    },
    'output': 4
    
})


# query is the first element in the card
test.append({
       'input':{
        'cards': [8,7,6,5,4,3,2,1,0],
        'query': 8,
    },
    'output': 0
    
})

# query is the last element in the card
test.append({
       'input':{
        'cards': [8,7,6,5,4,3,2,1,0],
        'query': 0,
    },
    'output': 8
    
})

# cards does not contain query
test.append({
       'input':{
        'cards': [8,7,6,5,4,3,2,1,0],
        'query': 12,
    },
    'output': -1
    
})

#  cards is empty
test.append({
       'input':{
        'cards': [],
        'query': 2,
    },
    'output': -1
    
})




# NOTE: array must be sorted inorder to implement Binary Search effectively

# signature function | Binary serach
# def locate_card(cards, query):
#     # first and last index of cards
#     lo, hi = 0, len(cards)-1
    
#     while lo <= hi:
#     # middle element of cards array
#         mid = (lo+hi)//2 #we are using // to get integer value 
#     # number at mid index = mid_number
#         mid_number = cards[mid]

#     # checking all the values
#         print("low:",lo, " high:",hi, " mid:",mid, "mid_number:",mid_number)

#         if mid_number == query:
#             return mid_number

#         elif mid_number < query:
#             hi = mid - 1
    
#         elif mid_number > query:
#             lo = mid + 1
#     return -1





# signature function
def locate_card(cards,query):
    # first and last index of cards array
    lo, hi = 0, len(cards)-1
    
    while lo <= hi:
        mid_index = (lo+hi)//2
        mid_number = cards[mid_index]

        if(query == mid_number):
            return mid_index
        
        elif( query < mid_number):
            lo = mid_index + 1

        elif(query > mid_number):
            hi = mid_index - 1

        elif(mid_index is not -1):
            return mid_index
    
    return -1

evaluate_test_cases(locate_card, test)
