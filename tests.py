from unittest import TestCase, main
from TestTask import minsort, maxsort

class MinsortTest(TestCase):
    def test_minT(self):
        self.assertEqual(minsort(["Gon","Li"],"Li"),True)

    def test_minF(self):
        self.assertEqual(minsort(["Gon","Li"],"Gon"),False)

class MaxsortTest(TestCase):
    def test_maxF(self):
        self.assertEqual(maxsort(["Gon","Li"],"Li"),False)

    def test_maxT(self):
        self.assertEqual(maxsort(["Gon","Li"],"Gon"),True)

if __name__ == '__main__':
    main()