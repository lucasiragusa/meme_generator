import pandas as pd
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from typing import List


class CsvIngestor(IngestorInterface):
    """Implementation of IngestorInterface for CSV files."""
    allowed_extension = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the given CSV file and return a list of QuoteModel objects.

        Args:
            path: The path of the CSV file to parse.

        Returns:
            A list of QuoteModel objects parsed from the CSV file.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
