from typing import List
from .IngestorInterface import IngestorInterface
from .CsvIngestor import CsvIngestor
from .PdfIngestor import PdfIngestor
from .TxtIngestor import TxtIngestor
from .DocxIngestor import DocxIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """
    A class that provides methods for parsing different file formats to create a list of QuoteModel objects.

    ...

    Methods
    -------
    parse(path:str) -> List[QuoteModel]:
        Parses a file at the given path using the appropriate ingestor and returns a list of QuoteModel objects.

    """

    ingestors = [DocxIngestor, TxtIngestor, PdfIngestor, CsvIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses a file at the given path using the appropriate ingestor and returns a list of QuoteModel objects.

        Parameters
        ----------
        path : str
            The path to the file to parse.

        Returns
        -------
        List[QuoteModel]
            A list of QuoteModel objects parsed from the file.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
