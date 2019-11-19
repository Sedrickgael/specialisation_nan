import graphene

import quiz.schema


class Query(quiz.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass
class Mutation(quiz.schema.RelayMutation,graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)