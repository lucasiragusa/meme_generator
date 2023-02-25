from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    An abstract base class that defines an interface for ingesting different file formats and creating a list of QuoteModel objects.

    ...

    Methods
    -------
    can_ingest(cls, path: str) -> bool:
        Checks if the given file path can be ingested by this ingestor.

    parse(cls, path:str) -> List[QuoteModel]:
        Parses a file at the given path using this ingestor and returns a list of QuoteModel objects.

    """

    allowed_extension = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Checks if the given file path can be ingested by this ingestor.

        Parameters
        ----------
        path : str
            The path to the file to check.

        Returns
        -------
        bool
            True if the file can be ingested, False otherwise.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses a file at the given path using this ingestor and returns a list of QuoteModel objects.

        Parameters
        ----------
        path : str
            The path to the file to parse.

        Returns
        -------
        List[QuoteModel]
            A list of QuoteModel objects parsed from the file.
        """
        pass
