from typing import List
from .IngestorInterface import IngestorInterface
from .CsvIngestor import CsvIngestor
from .PdfIngestor import PdfIngestor
from .TxtIngestor import TxtIngestor
from .DocxIngestor import DocxIngestor
from .QuoteModel import QuoteModel

class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, TxtIngestor, PdfIngestor, CsvIngestor]
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
