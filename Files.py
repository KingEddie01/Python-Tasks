# with open('account.txt', mode='r') as my_file:
#     print(my_file.read())

# file_obj = open('account.txt', mode='r')
# print(file_obj.read())
# file_obj.close()

# file_obj = open('account.txt', mode='r')
# print(file_obj.readline())
# file_obj.seek(0)

# file_obj = open('account.txt', mode='r')
# print(file_obj.readlines())
# file_obj.seek(0)
# print(file_obj.readlines())
# file_obj.close()

# with open('../account.txt', mode ='w') as my_file:
#     my_file.write('001 west 20\n')
#     my_file.write('002 you 20\n')
#     my_file.write('003 Paul 20\n')
#     my_file.write('004 green 20\n')


accounts_dict = {'accounts': [{'accounts': 100, 'name': 'Jones', 'balance': 24.98},
                              {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

import json


with open('accounts.json', 'w') as accounts:
    json.dump(accounts_dict, accounts)

with open('accounts.json', 'r') as accounts:
    accounts_json = json.load(accounts)

with open('accounts.json', 'r') as accounts:
    print(json.dumps(json.load(accounts), indent=4))
