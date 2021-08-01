'''
Python Code Snippets - stevepython.wordpress.com

150-premier-league-simulation

Source:
https://codereview.stackexchange.com/questions/
225653/premier-league-simulation
'''

import math
import random

H_PARAMETER = 1.148698355
A_PARAMETER = 0.8705505633


class Team:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.points = self.gf = self.ga = self.wins = self.draws = self.losses = self.gdiff = self.mp = 0


def generate_random_goals(delta_skill, parameter):
    if delta_skill == 0:
        raise ValueError
    goals = 0
    lamb = parameter ** (delta_skill)
    z = random.random()
    while z > 0:
        z = z - (((lamb ** goals) * math.exp(-1 * lamb)) /
                 math.factorial(goals))
        goals += 1
    return goals - 1


def generate_random_score(home, away):
    delta_skill = (home.skill - away.skill) / 3
    return (generate_random_goals(delta_skill,
                                  H_PARAMETER), generate_random_goals(delta_skill, A_PARAMETER))


def simulate_league(teams):
    for home_team in teams:
        print("=" * 50)
        print(home_team.name + "'s home games: ")
        print("=" * 50)
        for away_team in teams:
            if home_team == away_team:
                pass
            if home_team != away_team:
                home_score, away_score = generate_random_score(home_team, away_team)
                print(home_team.name, home_score, ":", away_score, away_team.name)
                home_team.gf += home_score
                away_team.gf += away_score
                home_team.ga += away_score
                away_team.ga += home_score
                home_team.gdiff += (home_score - away_score)
                away_team.gdiff += (away_score - home_score)
                home_team.mp += 1
                away_team.mp += 1
                if home_score == away_score:
                    home_team.draws += 1
                    away_team.draws += 1
                    home_team.points += 1
                    away_team.points += 1
                if home_score > away_score:
                    home_team.wins += 1
                    away_team.losses += 1
                    home_team.points += 3
                if away_score > home_score:
                    away_team.wins += 1
                    home_team.losses += 1
                    away_team.points += 3


if __name__ == "__main__":
    teams = [
        Team("Arsenal", 16), Team("Aston Villa", 6), Team("AFC Bournemouth", 8), Team("Brighton and Hove Albion", 5),
        Team("Burnley", 4), Team("Chelsea", 17), Team("Crystal Palace", 11), Team("Everton", 14),
        Team("Leicester City", 12), Team("Liverpool", 19), Team("Manchester City", 20), Team("Manchester United", 15),
        Team("Newcastle United", 3), Team("Norwich City", 2), Team("Sheffield United", 1), Team("Southampton", 7),
        Team("Tottenham Hotspur", 18), Team("Watford", 9), Team("West Ham United", 10),
        Team("Wolverhampton Wanderers", 13)
    ]

    for team in teams:
        print(team.name, team.skill)

    simulate_league(teams)

    sorted_teams = sorted(teams, key=lambda t: t.points, reverse=True)

    print("=" * 108)
    print(
        "| {:<25} | {:^4} | {:^3} | {:^3} | {:^3} | {:^4} | {:^4} | {:^4} | {:^6} |".format("CLUB", "MP", "W", "D",
                                                                                            "L", "GF",
                                                                                            "GA",
                                                                                            "GD", "PTS"))
    for team in sorted_teams:
        print("| {:<25} | {:^4} | {:^3} | {:^3} | {:^3} | {:^4} | {:^4} | {:^4} | {:^6} |".format(team.name, team.mp,
                                                                                                  team.wins,
                                                                                                  team.draws,
                                                                                                  team.losses,
                                                                                                  team.gf,
                                                                                                  team.ga, team.gdiff,
                                                                                                  team.points))
