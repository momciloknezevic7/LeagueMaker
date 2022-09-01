from fixturesLib import generate_fixtures, create_fixture_file

if __name__ == "__main__":
    teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]

    # True for two-leg fixtures, False for single
    fixtures = generate_fixtures(teams, False)

    for game_week in range(len(fixtures)):
        create_fixture_file(game_week+1, fixtures[game_week])
