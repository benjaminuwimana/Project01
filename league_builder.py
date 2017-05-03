from random import choice
import csv


def print_player_letter(teams):    
    for team in teams:
        #Making file name for each player
        for player in team["players"]:
            player_names = player["Name"].lower()
            list_player_names = player_names.split()
            file_name = '_'.join(list_player_names) + ".txt"
            #Opening the file for writting
            with open(file_name, "w") as file:
                #Writting appropriate message to the player's guardian
                file.write("\n\tDear " + player["Guardian Name(s)"] + "\n\n")
                file.write("\tWe are happy to welcome " + player["Name"] + " as one of our soccer players.\n\n")
                file.write("\t\tTeam: " + team["team_name"] + "\n")
                file.write("\t\tFirst Practice on: May 11 2017")
                file.write("\n\n\tRegards.")


def print_teams_to_file(teams):
    #Opening the 'teams.txt' to be written to
    with open("teams.txt", "w") as file:
        for team in teams:
            #Writting the name of a team to the file
            file.write(team["team_name"])
            #Underlining the team name
            underline = "=" * len(team["team_name"])
            file.write("\n" + underline + "\n\n")
            #Writting team's players (names, experience and guardian) beneath team's name
            for player in team["players"]:
                file.write(player["Name"] + ", " + player["Soccer Experience"] +", " + player["Guardian Name(s)"])
                file.write("\n")
            file.write("\n\n")

            
def distribute_players(players, teams):#players is a list of groups of players, teams is a list of teams
    i = 0
    j = 0
    chosen_players = []
    #For each list of players we dispatch them into teams
    for player_list in players:
        j += 1
        while i < len(player_list):
            #We randomly choose one player
            player = choice(player_list)
            if player in chosen_players:
                continue
            else:
                chosen_players.append(player)
                i += 1            
                for team in teams:
                    #Check if the number of players in current team does not exceed the number of players needed in each team
                    if len(team["players"]) < (len(player_list) / len(teams)) * j:
                        team["players"].append(player)
                        break
                    else:
                        continue
        i =0

                
def split_players():
    #Reading data from the provided csv file
    with open('soccer_players.csv') as csvfile:
        csv_data_reader = csv.DictReader(csvfile, delimiter = ',')
        rows = list(csv_data_reader)
        #Splitting players into two groups: experienced and non experienced
        players_with_experience = []
        players_without_experience = []
        for row in rows[:]:
            if row['Soccer Experience'].upper() == 'YES':
                players_with_experience.append(row)
            else:
                players_without_experience.append(row)
        #Return a tuple of the two groups
        return players_with_experience, players_without_experience


def main():
    #Creating the three teams without players
    teams = [{"team_name":"Sharks", "players":[]}, {"team_name":"Dragons", "players":[]}, {"team_name":"Raptors", "players":[]}]

    #Make two groups of players: those with experience and those without experience
    players = split_players()

    #Dispach players from the two groups to available teams
    distribute_players(players, teams)

    #Printing teams and their respective players into 'teams.txt' file
    print_teams_to_file(teams)

    #Printing letters into files for different players's guardians 
    print_player_letter(teams)

    #Display message showing how players have been deployed into their teams
    print("\nPlayers have been distributed in teams as follows:\n\n")
    for team in teams:
        print("\nTeam Name: {}".format(team["team_name"]))
        print("=================\n")
        for player in team["players"]:
            print("{}, {}, {}".format(player["Name"], player["Soccer Experience"], player["Guardian Name(s)"]))    

#Preventing this file execution when imported
if __name__ == '__main__':
    #Start the program
    main()
