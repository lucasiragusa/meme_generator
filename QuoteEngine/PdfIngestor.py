from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import subprocess
from typing import List
import random
import os


class PdfIngestor(IngestorInterface):
    """Implementation of IngestorInterface for PDF files."""
    allowed_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the given PDF file and return a list of QuoteModel objects.

        Args:
            path: The path of the PDF file to parse.

        Returns:
            A list of QuoteModel objects parsed from the PDF file.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        tmp = f'./_tmp/{random.randint(0,1000000)}.txt'
        quotes = []
        args = ['pdftotext', '-layout', path, tmp]
        output = subprocess.call(args)

        with open(tmp, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if len(line) > 2:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0],
                                           parse[1].replace('\n', ''))
                    quotes.append(new_quote)

        f.close()
        os.remove(tmp)

        return quotes
