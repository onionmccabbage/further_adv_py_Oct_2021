# here we use the rxpy library for asynchronous observable operators

import requests # pip install requests
import rx # pip install rx
import json
from rx import operators as op

# we will access an API nd point at https://jsonplaceholder.typicode.com/users
# a function to filter the returned data by 'starts with...'
def filterNames(x, l): # x is the object being tested, l is the letter
    if( x['name'].startswith(l) ):
        return x['name'] # match - so return this name
    else:
        return '' # no matches

def main():
    # ask the user which letter to match
    letter = input('starts with...? ')
    # fetch all the users from the API end point
    content = requests.get('https://jsonplaceholder.typicode.com/users')
    # convert from JSON to Python structure
    y = json.loads(content.text) # we now have a dict
    # we need an observable
    source = rx.from_(y) # note the trailing underscore
    # use observable
    case1 = source.pipe( # this will async wait for the data to be ready
        op.filter(lambda c:filterNames(c, letter)),
        op.map(lambda a:a['name'])
    )
    # now we subscribe to the observable (maybe multiple subscribers)
    case1.subscribe(
        # implement next, error and complete handlers
        on_next = lambda i: print('Received {}'.format(i)),
        on_error = lambda e: print('Received Error {}'.format(e)),
        on_completed = lambda: print('All done')
    )

if __name__ == '__main__':
    main()