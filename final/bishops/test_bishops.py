import unittest
import unittest.mock
import bishops
import io

class testBishops(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test1(self, mock_stdout):
        boardNum = "2"
        bishops.main(boardNum)
        self.assertEqual(mock_stdout.getvalue(), "2\n")
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test2(self, mock_stdout):
        boardNum = "3"
        bishops.main(boardNum)
        boardNum = "2"
        bishops.main(boardNum)
        self.assertEqual(mock_stdout.getvalue(), "4\n2\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test3(self, mock_stdout):
        boardNum = "358362"
        bishops.main(boardNum)
        boardNum = "10000000"
        bishops.main(boardNum)
        boardNum = "200"
        bishops.main(boardNum)
        self.assertEqual(mock_stdout.getvalue(), "716722\n19999998\n398\n")

if __name__ == "__main__":
    unittest.main(verbosity=2)