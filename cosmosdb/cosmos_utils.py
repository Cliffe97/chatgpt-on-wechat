import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import os
from dotenv import load_dotenv
import sys
sys.path.append("/home/lifugao/workSpace/chatgpt-on-wechat/")

import config

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

def create_items(container):
    print('\nCreating Items\n')

    # Create a SalesOrder object. This object has nested properties and various types including numbers, DateTimes and strings.
    # This can be saved as JSON as is without converting into rows/columns.
    sales_order = get_sales_order("SalesOrder1")
    container.create_item(body=sales_order)

    # As your app evolves, let's say your object has a new schema. You can insert SalesOrderV2 objects without any
    # changes to the database tier.
    sales_order2 = get_sales_order_v2("SalesOrder2")
    container.create_item(body=sales_order2)

def get_user_entry(user_id):
    user = {'id' : user_id,
            'partitionKey' : 'Account1',
            'purchase_order_number' : 'PO18009186470',
            'order_date' : datetime.date(2005,7,11).strftime('%c'),
            'subtotal' : 419.4589,
            ''
            }

    return user
