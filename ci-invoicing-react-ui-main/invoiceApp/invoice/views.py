from django.shortcuts import render
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from .data import invoice,userData
from .serializer import *
from rest_framework import status

# Create your views here.

class AllInvoiceView(APIView):
    def get(self,request):
        serializer = InvoiceSerializer(invoice, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


    def post(self,request):
        data = request.data
        data["invoice_id"] = len(invoice) + 1
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            invoice.append(serializer.data)
            return Response({"message":"New Invoice Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class SingleInvoiceView(APIView):
    def get(self,request,id):
        for val in invoice:
            if val["invoice_id"] == id:
                serializer = InvoiceSerializer(val).data
                return Response(serializer,status=status.HTTP_200_OK)
        return Response({"message":"Invoice not found"},status=status.HTTP_400_BAD_REQUEST)

class AddItemView(APIView):
    def post(self,request,id):
        data =request.data
        for val in invoice:
            if val["invoice_id"] == id:
                serializer = ItemsSerializer(data=data)
                if serializer.is_valid():
                    val["items"].append(serializer.data)
                    return Response({"message":"Added new item to invoice"},status=status.HTTP_201_CREATED)
        return Response({"message":"Invoice not found"},status=status.HTTP_400_BAD_REQUEST) 
    

class SignupView(APIView):
    def get(self, request):
        serializer = UserSerializer(userData, many=True).data
        return Response({"message":"Account created"}, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        for val in userData:
            if val["email"] == data["email"]:
                return Response({"message":"User already exists"},status=status.HTTP_400_BAD_REQUEST)
        data["user_id"] = len(userData) + 1
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            userData.append(serializer.data)
            return Response({"message":"user Created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SigninView(APIView):
    def post(self, request):
        data = request.data
        for val in userData:
            if val["email"] == data["email"] and val["password"] == data["password"]:
                encoded = jwt.encode({"email": data["email"]}, "secret", algorithm="HS256")
                return Response({"token":encoded, "message": "Login successful"},status=status.HTTP_200_OK)
        return Response({"message":"Email or Password does not match"},status=status.HTTP_400_BAD_REQUEST)
            
    
