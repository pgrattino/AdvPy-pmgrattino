import unittest
import unittest.mock
import bishops2
import io

class testBishops(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test1(self, mock_stdout):
        boardNum = "2\n3"
        bishops2.solve(boardNum)
        self.assertEqual(mock_stdout.getvalue(), "2\n4")

if __name__ == "__main__":
    unittest.main(verbosity=2)