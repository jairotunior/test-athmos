#!/usr/bin/python
import os
import logging
import argparse
from pathlib import Path
from datasources import JSONDataSource

logging.basicConfig(format='[+] - %(message)s', level=logging.INFO)

parser = argparse.ArgumentParser(description="")

subparsers = parser.add_subparsers(dest='operation')
subparsers.required = True

# subparser list
parser_list = subparsers.add_parser('list')

# subparser create
parser_create = subparsers.add_parser('create')
# subparset create arguments
parser_create.add_argument('-n', '--nombres', dest='nombres', type=str, help='Nombres del usuario', required=True)
parser_create.add_argument('-a', '--apellidos', dest='apellidos', type=str, help='Apellidos del usuario', required=True)
parser_create.add_argument('-e', '--edad', dest='edad', type=int, help='Edad del usuario', required=True)
parser_create.add_argument('-m', '--email', dest='email', type=str, help='Email del usuario', required=True)

# subparser delete
parser_delete = subparsers.add_parser('delete')
# subparset delete arguments
parser_delete.add_argument('-i', '--index', dest='index', type=int, help='Numero de posicion a editar a eliminar', required=True)

# subparser modify
parser_modify = subparsers.add_parser('modify')
# subparset modify arguments
parser_modify.add_argument('-i', '--index', dest='index', type=int, help='Numero de posicion a editar', required=True)
parser_modify.add_argument('-n', '--nombres', dest='nombres', type=str, help='Nombres del usuario', required=True)
parser_modify.add_argument('-a', '--apellidos', dest='apellidos', type=str, help='Apellidos del usuario', required=True)
parser_modify.add_argument('-e', '--edad', dest='edad', type=int, help='Edad del usuario', required=True)
parser_modify.add_argument('-m', '--email', dest='email', type=str, help='Email del usuario', required=True)


args = parser.parse_args()

CURRENT_DIR = Path(__file__).resolve().parent / "data"
filename = 'data.json'

process_data = JSONDataSource(path=CURRENT_DIR / filename)

if args.operation == 'list':
    logging.info(process_data.get_list())
    
elif args.operation == 'create':
    properties = args.__dict__
    del properties['operation']

    logging.info("{}".format(properties))
    
    process_data.create(**properties)

elif args.operation == 'delete':
    process_data.delete(index=args.index)
    logging.info("{}".format(args.__dict__))

elif args.operation == 'modify':
    properties = args.__dict__
    del properties['operation']

    process_data.modify(**properties)
    logging.info("{}".format(properties))