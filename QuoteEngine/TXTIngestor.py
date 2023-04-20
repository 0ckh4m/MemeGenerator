from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    """ Ingestor of TXT files. Returns a list of Quote objects. """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        txt = open(path, 'r')

        for line in txt:
            if line != "":
                parse = line.split('-')
                new_quote = QuoteModel(parse[0].strip(), parse[1].strip())
                quotes.append(new_quote)
        txt.close()

        return quotes
