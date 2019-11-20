import graphene
from graphene import relay, ObjectType , Connection 
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


from . import models
from django.contrib.auth.models import User

class ExtendConnection(Connection):
    class Meta:
        abstract = True
    total_count = graphene.Int()
    edge_count = graphene.Int()
    def resolve_total_count(root,info,**kwargs):
        return root.length
    def resolve_edge_count(root,info,**kwargs):
        return len(root.edges)

class SpecialisationNode(DjangoObjectType):
    class Meta:
        model = models.Specialisation
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'langage': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact'], 
            
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection

class RelayCreateSpecialisation(graphene.relay.ClientIDMutation):
    specialisation = graphene.Field(SpecialisationNode)
    class Input:
        nom = graphene.String()
        langage = graphene.String()
        status = graphene.Boolean()
        pk = graphene.ID()

    def mutate_and_get_payload(root,info,**kwargs):
        pk = kwargs.get('id') or None
        nom = kwargs.get('nom') or None
        langage = kwargs.get('nom') or None
        status = kwargs.get('status') or None
        if nom is not None and status is not None and langage is not None and pk is None:
            special = models.Specialisation(nom=nom, langage=langage, status=status)
        elif nom is not None and status is not None and langage is not None and pk is not None :
            special = models.Specialisation.objects.get(pk=pk)
            special.nom = nom
            special.langage = langage
            special.status = status
        elif nom is not None and  langage is not None and status is None and pk is not None:
            special = models.Specialisation.objects.get(pk=pk)
            special.nom = nom
            special.langage = langage
        elif nom is None and langage is not None and status is not None and pk is not None:
            special = models.Specialisation.objects.get(pk=pk)
            special.langage = langage
            special.status = status
        elif nom is not None and langage is None and status is not None and pk is not None:
            special = models.Specialisation.objects.get(pk=pk)
            special.nom = nom
            special.status = status
        elif nom is None and langage is None and status is not None and pk is not None:
            special = models.Specialisation.objects.get(pk=pk)
            special.status = status
        else:
            raise Exception('must be give parameters for Spécialisation mutations')
        special.save()
        return RelayCreateSpecialisation(specialisation = special)

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith'],
            'is_active': ['exact'], 
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection


class ProfileNode(DjangoObjectType):
    class Meta:
        model = models.Profile
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'statut': ['exact'], 
        }
        interfaces = (relay.Node, )
        
        
class QuizzNode(DjangoObjectType):
    class Meta:
        model = models.Quizz
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'niveau': ['exact'],
            'pourcentage': ['exact'],
            'nbq': ['exact'],
            'duree': ['exact'],
            'statut': ['exact'], 
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection
       
class QuestionNode(DjangoObjectType):
    class Meta:
        model = models.Question
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'niveau': ['exact'],
            'contenu': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact'], 
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection


class ReponseNode(DjangoObjectType):
    class Meta:
        model = models.Reponse
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'contenu': ['exact', 'icontains', 'istartswith'],
            'isrtue': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact'], 
        } 
        interfaces = (relay.Node,)
        connection_class = ExtendConnection

        
        
class QuizzUserNode(DjangoObjectType):
    class Meta:
        model = models.QuizzUser
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'note': ['exact'],
            'statut': ['exact'], 
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection

        
class ReponseUserNode(DjangoObjectType):
    class Meta:
        model = models.ReponseUser
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'istrue': ['exact'],
            'statut': ['exact'], 
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection

class Query(graphene.ObjectType):
    Specialisation = relay.Node.Field(SpecialisationNode)
    all_Specialisation = DjangoFilterConnectionField(SpecialisationNode)

    Profile = relay.Node.Field(ProfileNode)
    all_Profiles = DjangoFilterConnectionField(ProfileNode)

    Profile = relay.Node.Field(UserNode)
    all_Users = DjangoFilterConnectionField(UserNode)

    Quizz = relay.Node.Field(QuizzNode)
    all_Quizzs = DjangoFilterConnectionField(QuizzNode)

    Question = relay.Node.Field(QuestionNode)
    all_Questions = DjangoFilterConnectionField(QuestionNode)

    Reponse = relay.Node.Field(ReponseNode)
    all_Reponses = DjangoFilterConnectionField(ReponseNode)

    QuizzUser = relay.Node.Field(QuizzUserNode)
    all_QuizzUsers = DjangoFilterConnectionField(QuizzUserNode)

    ReponseUser = relay.Node.Field(ReponseUserNode)
    all_ReponseUsers = DjangoFilterConnectionField(ReponseUserNode)

class RelayMutation(graphene.AbstractType):
    relay_create_specialisation = RelayCreateSpecialisation.Field()