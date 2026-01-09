from fastapi import HTTPException,status


UserAlreadyExistException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail = "User already register"
)



UserNotRegisterException = HTTPException(
    status_code= status.HTTP_401_UNAUTHORIZED,
    detail= "User not Register"
)


UserNotLogInException = HTTPException(
    status_code= status.HTTP_401_UNAUTHORIZED,
    detail= "User not Log in"
)



TokenAbsentException = HTTPException(
    status_code= status.HTTP_401_UNAUTHORIZED,
    detail= "Token is absent"

)


TokenIsExpireException = HTTPException(
    status_code= status.HTTP_401_UNAUTHORIZED,
    detail= "Token is over"
)


IncorrectTokenType = HTTPException (
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail="Wrong Format of Token"
)



InventoryNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="skin or Inventory not Found"
)