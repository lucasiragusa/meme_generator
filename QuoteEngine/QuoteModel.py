
class QuoteModel():
    """Represents a quote with body and author information."""
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        return f'"{self.body}" - {self.author}'