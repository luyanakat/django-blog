from rest_framework.response import Response
from rest_framework import status


def custom_response(data=None, code=status.HTTP_200_OK, success=True):
    """Hàm chuẩn hóa phản hồi API"""
    return Response({
        "code": code,
        "success": success,
        "data": data,
    }, status=code)