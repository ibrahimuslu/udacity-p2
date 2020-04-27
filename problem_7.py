

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, fullpath, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for path in fullpath:
            if path not in current_node.handlers:
                current_node.handlers[path] = RouteTrieNode(handler) if fullpath[-1]==path else RouteTrieNode(False)
                if current_node.handlers[path] == None:
                    current_node.handler = False
            current_node = current_node.handlers[path]
        current_node.handler = handler

    def find(self, fullpath):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for path in fullpath:
            if path not in current_node.handlers:
                return False
            current_node = current_node.handlers[path]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.handlers = {}
        self.handler = handler

    def insert(self, path, handler):
        # Insert the node as before
        self.handlers[path] = RouteTrieNode(handler)

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root, not_found):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(root)
        self.not_found = not_found

    def add_handler(self, path_string, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        fullpath = self.split_path(path_string)
        self.root.insert(fullpath, handler)

    def lookup(self, path_string):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        fullpath = self.split_path(path_string)

        # remove trailing slash
        if fullpath[-1]=='': 
            fullpath = fullpath[:-1]
        
        if fullpath[-1]=='':
            return self.root.root.handler 
        handler = self.root.find(fullpath)
        if(handler):
            return handler
        else:
            return self.not_found

    def split_path(self, path_string):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        return path_string.split('/')
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home", "home handler")  # add a route
router.add_handler("/contact", "contact handler")  # add a route
router.add_handler("/finance", "finance handler")  # add a route
router.add_handler("/home/about/you", "about you handler")  # add a route
router.add_handler("/home/about/me/udacity/you", "about udacity handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/you")) # should print 'about you handler' 
print(router.lookup("/finance")) # should print 'finance handler'
print(router.lookup("/contact")) # should print 'contact handler'
print(router.lookup("/cart")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me/udacity/")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me/udacity/you")) # should print 'about udacity handler'