teamBreak = "This team doesn't have match in this fixture"
fixtureHeader = "----------------------------------------GAME WEEK "
fixtureFooter = "--------------------------------------------------"


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
        for i in range(int(n/2)):
            matches.append((input_teams[i], input_teams[n - 1 - i]))
            if rematch_ind:
                return_matches.append((input_teams[n - 1 - i], input_teams[i]))

        input_teams.insert(1, input_teams.pop())
        all_fixtures.insert(len(all_fixtures)//2, matches)
        if rematch_ind:
            all_fixtures.append(return_matches)

        matches = []
        return_matches = []

    print("DONE!")
    return all_fixtures


def create_fixture_file(gw, fixture):
    print("Creating file for each fixture...")

    # input [('Team1', 'Team5'), ('Day off', 'Team4'), ('Team2', 'Team3')]
    # create file with name fixturesGameWeek[gw]
    filename = "Fixtures/fixturesGameWeek" + str(gw)
    file = open(filename, "w")
    file.write(fixtureHeader + str(gw) + "\n"*2)

    # go throw fixture match by match
    for match in fixture:
        if teamBreak not in match:
            # format for match: Team 1 vs Team 2 | __ : __ |
            match_string = match[0] + " vs " + match[1] + " | __ : __ |\n"
            file.write(match_string)

    file.write("\n" + fixtureFooter)
    file.close()
    print("DONE!")


def parse_last_fixture():
    pass
    # TODO
