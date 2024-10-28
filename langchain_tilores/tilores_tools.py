from tilores import TiloresAPI
from tilores.helpers import PydanticFactory
from functools import cached_property
from langchain.tools import StructuredTool
from pydantic import create_model

class TiloresTools:
    """
    This class builds structured tools to be used in Langchain out of an instance of the Tilores API.

    The Tilores API and its objects (Record, SearchParams, RecordInput) are different from instance
    to instance. This class helps build structured tools at runtime, allowing them to be used
    against any Tilores instance.
    """

    def __init__(self, tilores_api: TiloresAPI):
        self.tilores_api = tilores_api

    @cached_property
    def references(self):
        return PydanticFactory(self.tilores_api.schema).generate()

    def all(self):
        return [
            self.search_tool,
            self.edge_tool
        ]

    def search_tool(self):
        return StructuredTool.from_function(**{
            'name': 'tilores_search',
            'description': 'useful for when you need to search one or more persons; each entity represents one unique person and has a list of records with varying information referring to that one person; if more than one entity is returned, you must tell the user that there are several persons found and ask which one he is looking for.',
            'args_schema': self.references['SearchParams'],
            'return_direct': True,
            'func': self.tilores_api.search
        })
    
    def edge_tool(self):
        return StructuredTool.from_function(**{
            'name': 'tilores_entity_edges',
            'description': 'useful for when you need to provide details about why certain records of an entity are matching; a single edge contains two record IDs and a rule ID representing the reason why those two records belong to the same entity',
            'args_schema': create_model("EntityEdgesArgs", entityID=(str, ...)),
            'return_direct': True,
            'func': self.tilores_api.entity_edges
        })

def static_value(val):
    def wrapper():
        print("requested values")
        return val
    return wrapper
