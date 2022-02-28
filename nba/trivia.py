nba_dict = {
    "Joel Embiid": "Philadelphia 76ers", "Giannis Antetokounmpo": "Milwaukee Bucks",
    "Jimmy Butler": "Miami Heat", "LeBron James": "Los Angeles Lakers",
    "Luka Doncic": "Dallas Mavericks", "Jalen Brunson": "Dallas Mavericks",
    "Spencer Dinwiddie": "Dallas Mavericks", "Stephen Curry": "Golden State Warriors"
}


class Trivia:
    def __init__(self, answers, athletes):
        self.answers = answers
        self.athletes = athletes

    # Determine how many user answers were correct
    def scoring(self):
        correct = 0
        for i in range(5):
            team = nba_dict.get(self.athletes[i])
            if team == self.answers[i]:
                correct += 1
        return correct

    @property
    def score(self):
        return self.scoring()


# Tester Code
# print value from dictionary
print(nba_dict.get("James Harden"))

# test case 1
ath = ["Joel Embiid", "James Harden", "Tobias Harris", "Giannis Antetokounmpo", "Jrue Holiday"]
# two correct answers
ans = ["76ers", "Philadelphia 76ers", "Los Angeles Lakers", "Milwaukee Bucks", "holidays"]

test = Trivia(ans, ath)
print(Trivia.scoring(test))

# test case 2
ath2 = ["Stephen Curry", "Zion Williamson", "LeBron James", "Anthony Davis", "Kyrie Irving"]
# no correct answers
ans2 = ["not sure", "Pelicans", "Cavaliers", "Detroit Pistons", "Raptors"]

test = Trivia(ans2, ath2)
print(Trivia.scoring(test))
