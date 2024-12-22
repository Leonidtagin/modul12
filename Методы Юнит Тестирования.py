import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __eq__(self, other):
        return self.name == other.name
    def run(self, distance):
        return distance / self.speed
    def walk(self, distance):
        return distance / (self.speed / 2)

class Tournament:
    def __init__(self, distance, participants):
        self.distance = distance
        self.participants = participants

    def start(self):
        results = {}
        for runner in self.participants:
            time =runner.run(self.distance)
            results[runner.name] = time
        return results
class TournamentTest(unittest.TestCase):
    all_results = []
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for name, result in cls.all_results.items():
            print(f'{name}: {result}')

    def test_race_ucain_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(results, key=results.get) == self.runner3.name)

    def test_race_andrey_nik(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(results, key=results.get) == self.runner3.name)

    def test_race_usain_andrey_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(results, key=results.get) == self.runner3.name)

if __name__ == '__main__':
    unittest.main()