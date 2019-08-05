import argparse
parser = argparse.ArgumentParser(description='Create collaboration users for a tenant')
parser.add_argument('tenant', metavar='tenant', type=str,
                    help='tenant for which collaboration accounts to be created')
parser.add_argument('--user', type=str,
                    help='if you want to create account for specifi user')
parser.add_argument('--firstname', type=str,
                    help='firstname of user you want to create account for(Pass this only if you are passing --user argument).')
args = parser.parse_args()
print('*' * 80)
print('args', args)
# print(args.accumulate(args.integers))
