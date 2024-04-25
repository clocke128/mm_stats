from pdfToCsvConverter import pdfToCsvConverter

def printFinalTeams():
    print("The final teams were UConn and Purdue")
    
def printFinalScore():
    print("The Final score was UConn: 75 - Purdue: 60")
    
if __name__ == '__main__':
    printFinalTeams()
    printFinalScore()
    pToCConverter = pdfToCsvConverter("/data/conn_stats_team_site.pdf", "/data/uconn_team_site.csv")
    print(print(pToCConverter))