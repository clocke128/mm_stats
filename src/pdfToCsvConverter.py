class pdfToCsvConverter:

    _pdfPath = ""
    _csvPath = ""
        
    def _setCsv(self, path):
        print("Setting CSV")
        self._csvPath = path
        
    def _setPdf(self, path):
        print("Setting PDF")
        self._pdfPath = path
        
        
    def __str__(self):
        return "PDF: " + self._pdfPath + "\nCSV: " + self._csvPath + "\n"
                    
    def __init__(self, pdfPath, csvPath):
        self._setCsv(csvPath)
        self._setPdf(pdfPath)