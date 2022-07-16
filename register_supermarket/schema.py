import graphene
from graphene_django import DjangoObjectType
from .models import Supermarket


class SupermarketsTypes (DjangoObjectType):
    class Meta:
        model = Supermarket
        fields = ("name_sup", "national_num_sup")


class Query (graphene.ObjectType):
    all_supermarkets = graphene.List(SupermarketsTypes)


schema = graphene.Schema(query=Query)
