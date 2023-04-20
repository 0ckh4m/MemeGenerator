from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DOCXIngestor import DOCXIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    ingestors = [DOCXIngestor, CSVIngestor, TXTIngestor, PDFIngestor] 

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)