
def validate_parcel_data(data):
    """validate parcel delivery orders details"""
    try:
        # check if description is empty
        if data["descr"] is False:
            return "parcel description required"
        elif isinstance(data["descr"], int) is True:
            return "Description must be a string"
        elif data["quantity"] is False: 
            return "parcel quantity required"
        elif data["quantity"] == "":
            return "parcel quantity is required"
        elif isinstance(data["quantity"], int) is False:
            return "Quantity must be a number"
        elif data["price"] is False: 
            return "price required"
        elif data["price"] == "":
            return "price is required"
        elif data["price"] < 0:
            return "The minimum unit price must be above 0"
        elif isinstance(data["price"], int) is False:
            return "price must be a number"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)