from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TxtIngestor (IngestorInterface): 
    """Implementation of IngestorInterface for TXT files."""

    allowed_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the given TXT file and return a list of QuoteModel objects.        
            Args:
                path: The path of the TXT file to parse.
            Returns:
            A list of QuoteModel objects parsed from the TXT file."""

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1].replace('\n', ''))
                    quotes.append(new_quote)
        return quotes

