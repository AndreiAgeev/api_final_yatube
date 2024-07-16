from rest_framework import status
from rest_framework.exceptions import APIException


class FollowMyselfError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ("You can't follow yourself")
    default_code = 'wrong_data'


class FollowTwiceError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ("You've already followed this person")
    default_code = 'wrong_user'
