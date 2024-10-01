from utils.import_functions import import_cars_brand
from utils.conversion_functions import convert_list_to_df

from argparse import ArgumentParser

# initate the argument parser
parser = ArgumentParser()

# add arguments to the parser
parser.add_argument("--brand",
                    help="brand of the car",
                    type=str)

parser.add_argument("--amount",
                    help="amount of cars to import",
                    type=int)

# parse the arguments
args = parser.parse_args()

# get the args from the parser
brand = input("Insert a car brand")
amount = int(input("How many cars:"))

# import the cars
cars_list = import_cars_brand(brand, amount)

# convert the list to a DataFrame
cars_df = convert_list_to_df(cars_list)

# export the file
cars_df.to_csv("export.csv")

pass