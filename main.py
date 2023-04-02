# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    phonebook = {}
    for request in queries:
        if request.type == 'add':
            phonebook[request.number] = request.name
        elif request.type == 'del':
            if request.number in phonebook:
                del phonebook[request.number]
        elif request.type == 'find':
            response = phonebook.get(request.number, "not found")
            result.append(response)
        else:
            response = "invalid input"
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
