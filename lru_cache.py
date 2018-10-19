import pylru

# This is an overview , not the complete code
cache_size = 50
cache = pylru.lrucache(cache_size)
value  = cache[key]  # access the cache
# inserting new cache element on the top
cache[key= value
# Storing the access time when the key is accessed 

# deleting the cache element if not used recently
del cache[key]

# getting the creation time of cache
# Setting time limit for cache
# clearing the cache once time is expired
cache.clear()





