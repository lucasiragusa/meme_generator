from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

# OLD CODE
# class IngestorInterface(ABC):
#     """Interface for ingesting files and parsing quotes."""
#     allowed_extensions = ['csv', 'docx', 'pdf', 'txt']

#     @classmethod
#     def can_ingest(cls, path: str) -> bool:
#         """Check if the given file can be ingested by this ingestor.

#         Args:
#             path: The path of the file to check.

#         Returns:
#             A boolean value indicating whether the file can be ingested or not.
#         """
#         extension = path.split('.')[-1]
#         return extension in cls.allowed_extensions

#     @classmethod
#     @abstractmethod
#     def parse(cls, path: str) -> List[QuoteModel]:
#         '''Parse the given file and return a list of QuoteModel objects.
#         Abstract class to coerce the declaration of parse in children classes.'''

#         pass

# NEW CODE
class IngestorInterface(ABC):
    allowed_extension = []
    @classmethod
    def can_ingest(cls,path):
        # print("here")
        # print(path)
        ext = path.split('.')[-1]
        # print(ext)
        # print(cls.allowed_extension)
        # print(ext in cls.allowed_extension)
        return ext in cls.allowed_extension
    @classmethod
    @abstractmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        pass