from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import GoogleSheetRowSerializer
from .utils import read_data, add_data_meal, update_data_meal, delete_row, add_given, update_given


class ListData(generics.ListAPIView):
    """
    This view lists all the data from Google Sheets.
    """
    serializer_class = GoogleSheetRowSerializer

    def get(self, request, *args, **kwargs):
        result = read_data()  # Fetch the data from Google Sheets
        return Response({'values': result}, status=status.HTTP_200_OK)
    
class CreateRowMeal(generics.CreateAPIView):
    """
    This view creates a new row in Google Sheets.
    """
    serializer_class = GoogleSheetRowSerializer

    def post(self, request, day=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = add_data_meal(serializer.validated_data['values'], day)
            if result['status'] == 'success':
                return Response(result, status=status.HTTP_201_CREATED)
            else:
                return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateRowMeal(generics.UpdateAPIView):
    """
    This view updates a row in Google Sheets.
    """
    serializer_class = GoogleSheetRowSerializer

    def put(self, request, day, user, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = update_data_meal(serializer.validated_data['values'], day, user)
            if result['status'] == 'success':
                return Response(result, status=status.HTTP_200_OK)
            else:
                return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteRow(generics.DestroyAPIView):
    """
    This view deletes row data in a specific day from Google Sheets.
    """
    def delete(self, request, day, sheet, *args, **kwargs):
        result = delete_row(day, sheet)
        return Response(result, status=status.HTTP_204_NO_CONTENT)
    

class CreateRowGiven(generics.CreateAPIView):
    serializer_class = GoogleSheetRowSerializer

    def post(self, request, day=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = add_given(serializer.validated_data['values'], day)
            if result['status'] == 'success':
                return Response(result, status=status.HTTP_201_CREATED)
            else:
                return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateRowGiven(generics.UpdateAPIView):
    """
    This view updates a row in Google Sheets.
    """
    serializer_class = GoogleSheetRowSerializer

    def put(self, request, day, user, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = update_given(serializer.validated_data['values'], day, user)
            if result['status'] == 'success':
                return Response(result, status=status.HTTP_200_OK)
            else:
                return Response(result, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)