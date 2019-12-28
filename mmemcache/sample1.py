from pymemcache.client import base


client = base.Client('localhost', 11211)

print(client)
print(client.set)
client.set('some_key', 'some value')

print(client.get('some_key'))
