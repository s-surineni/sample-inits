import re


url = 'https://redis-app.qa-ui-alpha2.aviso.com/welcome/home/collaboration'
url = 'redis-app.qa-ui-alpha2.aviso.com'
# reg_str = r'([^.]+\.)(.*)'
reg_str = r'([^.]+\.)([^.]+\.)([^.]+\.)'


res = re.search(reg_str, url)
print(res.group(1))

if res:
    url = url.replace(res.group(1), '')
    print(url)


url = 'https://qa-ui-alpha2.aviso.com/welcome/home/collaboration'
reg_str = r'//([^.]+\.)(.*)'
reg_str = r'//([^.]+\.)([^.]+\.)([^.]+\.)'
res = re.search(reg_str, url)

print(res.group(1))
reg_str2 = r'([^.]+\.)'

# res2 = re.sub(reg_str, '', url, )
# print(res2)
