from QuoteEngine import IngestorInterface, CSVIngestor, DOCXIngestor, TXTIngestor, PDFIngestor, Ingestor

# print(CSVIngestor.parse('./_data/DogQuotes/DogQuotesCSV.csv')) # OK
# print(DOCXIngestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx')) # Ok
# print(TXTIngestor.parse('./_data/DogQuotes/DogQuotesTXT.txt')) # OK
# print(PDFIngestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf')) # Ok

print(Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf')) # Ok