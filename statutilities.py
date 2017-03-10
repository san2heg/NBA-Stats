# Some utilities and testing the getStatsForPlayer function

from scraper import getStatsForPlayer

def getStatsAgainstTeam(playerName, teamName):
	statsList = getStatsForPlayer(playerName, 2017)
	newList = []
	for stat in statsList:
		if stat['Opp'] == teamName:
			newList.append(stat)
	return newList

def getStatsForLastFiveGames(playerName):
	statsList = getStatsForPlayer(playerName, 2017)
	return statsList[-5:]

# Calculates score for a statline for letsRUMBL
def calculateLRScore(stat):
	if (stat['PTS'] == 'N/A'):
		return 0
	totalScore = int(stat['PTS']) + 1.5 * int(stat['TRB']) + 1.5 * int(stat['AST']) + 2 * int(stat['BLK']) + 2 * int(stat['STL']) - int(stat['TOV'])
	return totalScore

# Calculates score for a statline for FanDuel
def calculateFDScore(stat):
	if (stat['PTS'] == 'N/A'):
		return 0
	totalScore = int(stat['PTS']) + 1.2 * int(stat['TRB']) + 1.5 * int(stat['AST']) + 2 * int(stat['BLK']) + 2 * int(stat['STL']) - int(stat['TOV'])
	return totalScore

def center(string):
	return "{:^80}".format(string)

def printStats(statList):
	lrSum = 0
	fdSum = 0
	avgLR = 0
	avgFD = 0
	subtract = 0
	for stat in statList:
		if (stat['PTS'] != 'N/A'):
			lrSum += calculateLRScore(stat)
			fdSum += calculateFDScore(stat)
		else:
			subtract += 1
		print "Game: " + stat['Rk'] + ", Date: " + stat['Date'] + ":\t\tLR Score - " + str(calculateLRScore(stat)) + "\t\tFD Score - " + str(calculateFDScore(stat))
		if (stat['PTS'] == 'N/A'):
			print "Did Not Play"
		else:
			print "Points: " + stat['PTS'] + ", Rebounds: " + stat['TRB'] + ", Assists: " + stat['AST']
		print
	if (len(statList)-subtract != 0):
		avgLR = lrSum / (len(statList)-subtract)
		avgFD = fdSum / (len(statList)-subtract)
	print center("AVERAGE LR SCORE: " + "{0:.2f}".format(avgLR))
	print center("AVERAGE FD SCORE: " + "{0:.2f}".format(avgFD))
	print


