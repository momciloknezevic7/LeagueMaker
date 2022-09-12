import os
import shutil
from tabulate import tabulate
from db.db_init import add_draw, add_win_and_loose, get_standings

teamBreak = "This team doesn't have match in this fixture"
fixtureHeader = "----------------------------------------GAME WEEK "
fixtureFooter = "--------------------------------------------------"

unreadFixtures = "../Results/Unread Fixtures/"
readoutFixtures = "../Results/ReadOut Fixtures/"


def generate_fixtures(input_teams, rematch_ind):
    print("Generate fixtures...")

    # if team number is odd - one of the teams has to take a break every week
    if len(input_teams) % 2:
        input_teams.append(teamBreak)

    n = len(input_teams)
    matches = []
    all_fixtures = []
    return_matches = []

    for current_fixture in range(1, n):
        for i in range(int(n / 2)):
            matches.append((input_teams[i], input_teams[n - 1 - i]))
            if rematch_ind:
                return_matches.append((input_teams[n - 1 - i], input_teams[i]))

        input_teams.insert(1, input_teams.pop())
        all_fixtures.insert(len(all_fixtures) // 2, matches)
        if rematch_ind:
            all_fixtures.append(return_matches)

        matches = []
        return_matches = []

    return all_fixtures


# Fixture for matches that were not played in their schedule
def create_blank_fixture():
    filename = "../Fixtures/fixturesGameWeek_outOfSchedule"
    file = open(filename, "w")
    file.write(fixtureHeader + "\n" * 2)
    file.close()


def create_fixture_file(gw, fixture):
    print("Creating file for fixture gameweek " + str(gw))

    # input [('Team1', 'Team5'), ('Day off', 'Team4'), ('Team2', 'Team3')]
    # create file with name fixturesGameWeek[gw]
    filename = "../Fixtures/fixturesGameWeek" + str(gw)
    file = open(filename, "w")
    file.write(fixtureHeader + str(gw) + "\n" * 2)

    # go throw fixture match by match
    for match in fixture:
        if teamBreak not in match:
            # format for match: Team 1 vs Team 2 | __ : __ |
            match_string = match[0] + " vs " + match[1] + " | __ : __ |\n"
            file.write(match_string)

    file.write("\n" + fixtureFooter)
    file.close()

    create_blank_fixture()
    print("DONE!")


def parse_unread_fixtures():
    unread_files = os.listdir(unreadFixtures)
    num_of_unread = len(unread_files)
    if num_of_unread:
        print("There are " + str(num_of_unread) + " unread fixture files!")

    for file in unread_files:
        print("Parsing " + file + "...")
        parse_fixture(file)

        # Done with this file and move it from this directory
        shutil.move(unreadFixtures + file, readoutFixtures + file)

    print("All played fixtures are parsed!")


def parse_fixture(file):
    file = open(unreadFixtures + file)

    # read header and one blank line
    file.readline()
    file.readline()

    while True:
        curr_match = file.readline()
        if curr_match == "\n":
            break

        teams_and_result = curr_match.split("|")

        teams = teams_and_result[0].split("vs")
        teams = [team.strip() for team in teams]

        result = teams_and_result[1].split(":")
        result = [goals.strip() for goals in result]

        if '__' in result:
            blank_file = open("../Fixtures/fixturesGameWeek_outOfSchedule", "a")
            blank_file.write(curr_match + "\n")
        else:
            result = [int(goals) for goals in result]
            if result[0] == result[1]:
                add_draw(teams[0], teams[1])
            elif result[0] > result[1]:
                add_win_and_loose(teams[0], teams[1], result[0]-result[1])
            else:
                add_win_and_loose(teams[1], teams[0], result[1]-result[0])


def print_standings():
    col_names = ["Team", "Played", "Won", "Drawn", "Lost", "Goal diff", "Points"]
    data = get_standings()
    row_indices = list(range(1, len(data)+1))

    # stdout standings
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex=row_indices))

    # file standings
    with open("../Results/liveStandings", "w") as file:
        file.write(tabulate(data, headers=col_names, showindex=row_indices))
