import subprocess
# import sys
import random
from typing import List
import os

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
    

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', '-raw', path, tmp])
    
        file_ref = open(tmp, "r")
        quotes = []
    
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0].strip(' "'), parse[1])
                quotes.append(new_quote)
    
        file_ref.close()
        os.remove(tmp)
        return quotes