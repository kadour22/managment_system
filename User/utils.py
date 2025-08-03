from .models import Account
from rest_framework.response import Response
from .serializers import accounts_serializer, user_serializer
from rest_framework import status

def get_account_data(user):
    try:
        account = Account.objects.get(user=user)
        serializer = accounts_serializer(account, many=False)
        user_data = user_serializer(user, many=False)
        return Response({"user": user_data.data, "account": serializer.data}, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return None
