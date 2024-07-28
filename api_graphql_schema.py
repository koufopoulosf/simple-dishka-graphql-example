import strawberry

from api_graphql_mutation import Mutation
from api_graphql_query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)