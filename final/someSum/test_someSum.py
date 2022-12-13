import unittest
import unittest.mock
import someSum
import io

class testSomeSum(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test1(self, mock_stdout):
        testSum = 1
        someSum.solve(testSum)
        self.assertEqual(mock_stdout.getvalue(), "Either\n")
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test2(self, mock_stdout):
        testSum = 2
        someSum.solve(testSum)
        self.assertEqual(mock_stdout.getvalue(), "Odd\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test3(self, mock_stdout):
        testSum = 3
        someSum.solve(testSum)
        self.assertEqual(mock_stdout.getvalue(), "Either\n")
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test4(self, mock_stdout):
        testSum = 4
        someSum.solve(testSum)
        self.assertEqual(mock_stdout.getvalue(), "Even\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test5(self, mock_stdout):
        testSum = 10
        someSum.solve(testSum)
        self.assertEqual(mock_stdout.getvalue(), "Odd\n")

if __name__ == "__main__":
    unittest.main(verbosity=2)