from pymemcache.client import base
client = base.Client(('localhost', 11211))
client.set('a', 'apple')
print(client.get('a'))
