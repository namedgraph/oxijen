from enum import Enum

class XSD(Enum):

    NS : str = "http://www.w3.org/2001/XMLSchema#"

    INTEGER = NS + "integer"
    STRING = NS + "string"
    FLOAT = NS + "float"