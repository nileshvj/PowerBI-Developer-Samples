# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license

class Customer:

    # Camel casing is used for the member variables as they are going to be serialized and camel case is standard for JSON keys

    CustomerId = None
    CustomerName = None
    Location = None
    Product = None

    def __init__(self, customer_id, customer_name, location, product):
        self.CustomerId = customer_id
        self.CustomerName = customer_name
        self.Location = location
        self.Product = product