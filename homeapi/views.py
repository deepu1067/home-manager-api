from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import GoogleSheetRowSerializer
from .utils import (
    read_data,
    add,
    update_data,
    delete_row,
    read_data_given,
    get_total,
    get_user,
    get_list,
)


class ListData(generics.ListAPIView):
    """
    This view lists all the data from Google Sheets.
    """

    serializer_class = GoogleSheetRowSerializer

    def get(self, request, *args, **kwargs):
        result = read_data()  # Fetch the data from Google Sheets
        return Response({"values": result}, status=status.HTTP_200_OK)


class ListDataGiven(generics.ListAPIView):
    serializer_class = GoogleSheetRowSerializer

    def get(self, request, *args, **kwargs):
        result = read_data_given()  # Fetch the data from Google Sheets
        return Response({"values": result}, status=status.HTTP_200_OK)


class CreateRow(generics.CreateAPIView):
    """
    This view creates a new row in Google Sheets.
    """

    serializer_class = GoogleSheetRowSerializer

    def post(self, request, user, sheet, day=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = add(
                serializer.validated_data["values"], user=user, sheet=sheet, day=day
            )
            if result["status"] == "success":
                return Response(result, status=status.HTTP_201_CREATED)
            else:
                return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateRow(generics.UpdateAPIView):
    """
    This view updates a row in Google Sheets.
    """

    serializer_class = GoogleSheetRowSerializer

    def put(self, request, day, user, sheet, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = update_data(serializer.validated_data["values"], day, user, sheet)
            if result["status"] == "success":
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


class GetTotal(generics.ListAPIView):
    serializer_class = GoogleSheetRowSerializer

    def get(self, request, user=None, *args, **kwargs):
        result = get_total(user)  # Fetch the data from Google Sheets
        return Response({"values": result}, status=status.HTTP_200_OK)


class GetAllUsers(generics.ListAPIView):
    serializer_class = GoogleSheetRowSerializer

    def get(self, request, *args, **kwargs):
        result = get_user()

        return Response({"values": result}, status=status.HTTP_200_OK)


class GetUserMeal(generics.ListAPIView):
    serializer_class = GoogleSheetRowSerializer

    def get(self, request, user, sheet, *args, **kwargs):
        result = get_list(user, sheet)

        return Response({"values": result}, status=status.HTTP_200_OK)
