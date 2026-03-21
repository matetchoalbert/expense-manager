from django.shortcuts import render
from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset= Transaction.objects.all()
    serializer_class=TransactionSerializer # la classe de serialisation
    

class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all() # pour recuperer toute les transaction
    serializer_class=TransactionSerializer
    lookup_field = "id" # cette class doit recuperer l'id de l'element qu'on veut traiter
    
