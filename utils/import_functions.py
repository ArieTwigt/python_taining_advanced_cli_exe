import requests


def import_cars_brand(brand: str, amount: int):
    '''
    Function to import cars based on brand:

    Input:
    * brand: Brand to import
    * amount: Number of cars to import
    '''
    # uppercase the brand
    brand_upper = brand.upper()

    # endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}&$limit={amount}"

    # execute the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()

    return data
