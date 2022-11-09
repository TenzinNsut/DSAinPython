from jovian.pythondsa import evaluate_test_cases


# Brute force

# Signature function

""" def locate_card(cards,query):
    # creating a variable for index of cards
    position = 0 #initially setting the position 0 -> to start from first element in the cards

    # Setting up a loop
    while True:
        if cards[position] == query:
            # Answer found!, return and exit
            return position

        # increment position
        position += 1

        # traverse till and of list
        if position == len(cards):
            
            # query not found, exit
            return -1

        # cards is empty, return
        if cards == None:

            return-1
  """

# signature function
def  locate_card(cards,query):
    # variable to keep track of index
    position = 0
    # tackling if cards is empty -> 0 < 0 : False
    print('cards:', cards)
    print('query:', query)
    while position < len(cards): 
        if cards[position] == query:
            return position
        position += 1
    return -1
        
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

# cards contain repeated elements


test.append({
       'input':{
        'cards': [8,7,8,5,3,2,1,0],
        'query': 7,
    },
    'output': 1
    
})

#  multiple query elements present in the card
test.append({
       'input':{
        'cards': [8,8,6,6,3,2,1,0],
        'query': 8,
    },
    'output': 0
    
})

evaluate_test_cases(locate_card, test)