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

    def get(self, request, sheet_id, *args, **kwargs):
        result = read_data(sheet_id)  # Fetch the data from Google Sheets
        return Response({"values": result}, status=status.HTTP_200_OK)


class ListDataGiven(generics.ListAPIView):
    serializer_class = GoogleSheetRowSerializer

    def get(self, request, sheet_id, *args, **kwargs):
        result = read_data_given(sheet_id)  # Fetch the data from Google Sheets
        return Response({"values": result}, status=status.HTTP_200_OK)


class CreateRow(generics.CreateAPIView):
    """
    This view creates a new row in Google Sheets.
    """

    serializer_class = GoogleSheetRowSerializer

    def post(self, request, user, sheet, sheet_id, day=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = add(
                serializer.validated_data["values"],
                user=user,
                sheet=sheet,
                day=day,
                spreadsheet_id=sheet_id,
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

    def put(self, request, sheet_id, day, user, sheet, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = update_data(
                serializer.validated_data["values"], day, user, sheet, sheet_id
            )
            if result["status"] == "success":
                return Response(result, status=status.HTTP_200_OK)
            else:
                return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteRow(generics.DestroyAPIView):
    """
    This view deletes row data in a specific day from Google Sheets.
    """

    def delete(self, request, sheet_id, day, sheet, *args, **kwargs):
        result = delete_row(day, sheet, sheet_id)
        return Response(result, status=status.HTTP_204_NO_CONTENT)


class GetTotal(generics.ListAPIView):
    serializer_class = GoogleSheetRowSerializer

    def get(self, request, sheet_id, user=None, *args, **kwargs):

        result = get_total(spreadsheet_id=sheet_id, user=user)
        return Response({"values": result}, status=status.HTTP_200_OK)


class GetAllUsers(generics.ListAPIView):
    serializer_class = GoogleSheetRowSerializer

    def get(self, request, sheet_id, *args, **kwargs):
        result = get_user(sheet_id)

        return Response({"values": result}, status=status.HTTP_200_OK)


class GetUserMeal(generics.ListAPIView):
    serializer_class = GoogleSheetRowSerializer

    def get(self, request, user, sheet, sheet_id, *args, **kwargs):
        result = get_list(user, sheet, sheet_id)

        return Response({"values": result}, status=status.HTTP_200_OK)
