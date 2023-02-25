from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import docx


class DocxIngestor (IngestorInterface):
    """Implementation of IngestorInterface for DOCX files."""

    allowed_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the given DOCX file and return a list of QuoteModel objects.

        Args:
            path: The path of the DOCX file to parse.

        Returns:
            A list of QuoteModel objects parsed from the DOCX file.
        """

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if len(para.text) > 0:
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1].replace('\n', ''))
                quotes.append(new_quote)
        return quotes
