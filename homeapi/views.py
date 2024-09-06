from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import GoogleSheetRowSerializer
from .utils import read_data, add_data


class ListData(generics.ListAPIView):
    """
    This view lists all the data from Google Sheets.
    """
    serializer_class = GoogleSheetRowSerializer

    def get(self, request, *args, **kwargs):
        result = read_data()  # Fetch the data from Google Sheets
        return Response({'values': result}, status=status.HTTP_200_OK)
    
class CreateRow(generics.CreateAPIView):
    """
    This view creates a new row in Google Sheets.
    """
    serializer_class = GoogleSheetRowSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = add_data(serializer.validated_data['values'])
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)