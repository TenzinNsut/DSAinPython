# signature function
# def locate_card(cards, query):
#     pass

# # driver code
# cards = [8,7,6,5,4,3,2,1,0]
# query = 4




# TEST CASE:
"""
cards = [8,7,6,5,4,3,2,1,0]
query = 6
---------------
OUTPUT: 2

"""

# Test cases with dictionary
# test = {
#     'inputs':{
#         'cards': [8,7,6,5,4,3,2,1,0],
#         'query': 6,
#     },
#     'output': 2
# }


# passing this test cases into function
# locate_card(**test['inputs']) == test['output']


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


test = []

# query is the middle of cards.
test.append({
       'inputs':{
        'cards': [8,7,6,5,4,3,2,1,0],
        'query': 4,
    },
    'output': 4
    
})


# query is the first element in the card
test.append({
       'inputs':{
        'cards': [8,7,6,5,4,3,2,1,0],
        'query': 8,
    },
    'output': 0
    
})

# query is the last element in the card
test.append({
       'inputs':{
        'cards': [8,7,6,5,4,3,2,1,0],
        'query': 0,
    },
    'output': 9
    
})

# cards does not contain query
test.append({
       'inputs':{
        'cards': [8,7,6,5,4,3,2,1,0],
        'query': 12,
    },
    'output': 0
    
})

#  cards is empty
test.append({
       'inputs':{
        'cards': [],
        'query': 2,
    },
    'output': 0
    
})

# cards contain repeated elements


test.append({
       'inputs':{
        'cards': [8,7,8,5,3,2,1,0],
        'query': 7,
    },
    'output': 1
    
})

#  multiple query elements present in the card
test.append({
       'inputs':{
        'cards': [8,8,6,6,3,2,1,0],
        'query': 8,
    },
    'output': 0
    
})