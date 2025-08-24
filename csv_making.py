# program to make random lemonade csv !
"""
date {
    - generate up to names for each order
    - generate that many orders
}
"""
# installing my desired packages
import pandas as pd
import random as rm
from faker import Faker

fake = Faker()
# my methods

def initialize_values():
    # creating initial variables
    order_num = rm.randint(1,1000)
    return order_num

def create_mycsv():
    order = []
    order_num=initialize_values()
    for i in range(order_num):
        orders_made = rm.randint(1,5) ; random_name = fake.name()
        order.append([random_name,orders_made]) 
        print(order)

    my_csv = pd.DataFrame({
        'name' : order[0][0],
        'orders made' : order[1][1]
    })
    my_csv.to_csv("my_data.csv", index=False)

create_mycsv()