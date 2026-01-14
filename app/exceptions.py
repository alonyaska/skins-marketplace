from fastapi import HTTPException,status


class InventoryException(HTTPException):
    status_code = 500 # По умолчанию
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserNotLogIn(InventoryException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User not LogIn"


class UserNotRegister(InventoryException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User not Registered"


class UserAlreadyExistException(InventoryException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "User already registered"

class TokenIsExpireException(InventoryException):
    status_code =  status.HTTP_401_UNAUTHORIZED
    detail = "Token is over"


class TokenAbsentException(InventoryException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token is absent"

class IncorrectTokenType(InventoryException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Wrong format token"

class InventoryNotFound(InventoryException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Inventory or skin not Found"

class SkinAlreadyOnMarket(InventoryException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Skin already on Market"


class NotEnoughMoney(InventoryException):
    status_code = status.HTTP_402_PAYMENT_REQUIRED
    detail = "Not Enough Money"



class InventoryIsNull(InventoryException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "No skins found. You may have set your filter criteria too strict"