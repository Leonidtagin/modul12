import unittest
import test_12_3

atheleticsTS = unittest.TestSuite()
atheleticsTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.Runner))
atheleticsTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
ut_runner = unittest.TextTestRunner(verbosity=2)
ut_runner.run(atheleticsTS)
