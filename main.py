# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    # Added constraint to the input
    assert 1 <= n <= 10**5, "Number of queries is out of bounds"
    # Added limit to splits, 
    # so that if entered name is more than just one word (bob ross) 
    # it prints out full name (bob ross) instead of just first entry (bob)
    return [Query(input().split(' ', 2)) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Changed from list to dictionary
    phonebook = {}
    for request in queries:
        if request.type == 'add':
            # Adds phone number (as key) with names (as values) to the phonebook
            # If the phone number exists, just rewrites the name
            phonebook[request.number] = request.name
        elif request.type == 'del':
            # Looks up the phonebook for specific number
            if request.number in phonebook:
                # If found, deletes key-value pair
                del phonebook[request.number]
        elif request.type == 'find':
            # Searches for specific number in phonebook
            # If no such number found, gives default answer "not found"
            response = phonebook.get(request.number, "not found")
            # Adds response to the result list
            result.append(response)
        else:
            # If entered anything else, outputs message about wrong command
            response = "invalid input"
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
