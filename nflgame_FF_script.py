import nflgame

def selectPosition():
    title = "Select Position"
    print title
    print ("= " * 20)
    print ("1: Quarterbacks")
    print ("2: Wide Receivers")
    print ("3: Running Backs")
    print ("4: Exit")

def yearAndWeek():
    # Enter the year and week: games(year, week,) or games(year, week=None)
    games = nflgame.games(2015, 10)
    players = nflgame.combine_game_stats(games)
    return players

def qb():
    for p in yearAndWeek().passing().sort('passing_yds').limit(10):
        msg = '%s %d for %d and %d YDs and %d'
        print msg % (p, p.passing_cmp, p.passing_att, p.passing_yds, p.passing_td)

def rb():
    for p in yearAndWeek().rushing().sort('rushing_yds').limit(10):
        msg = '%s %d carries for %d yards and %d TDs'
        print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)

def wr():
    for p in yearAndWeek().receiving().sort('receiving_yds').limit(10):
        msg = '%s %d YDs %d REC and %d TDs'
        print msg % (p, p.receiving_yds, p.receiving_rec, p.receiving_td)



def positionOutput():
    selectPosition()
    loop = 1
    while loop == 1:
        userInput = raw_input("Please choose a option 1-4: ")
        if userInput == "1":
            qb()
        elif userInput == "2":
            wr()
        elif userInput == "3":
            rb()
        elif userInput == "4":
            loop = 0
        else:
            print "Please enter a value from 1-4"

positionOutput()
