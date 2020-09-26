import unittest
import bubblesort as st
import random

class Test_TestValue(unittest.TestCase):
    def test_simple(self):
        testList = [4,2,1,3]
        expectedList = testList.copy()
        expectedList.sort()
        sortedList = st.bubblesort(testList)
        self.assertEqual(expectedList, sortedList)
        
    def test_empty(self):
        testList = []
        expectedList = testList.copy()
        expectedList.sort()
        actualList = st.bubblesort(testList)
        self.assertEqual(actualList, expectedList)

    def test_presorted(self):
        testList = [1,2,3,4]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = st.bubblesort(testList)
        self.assertEqual(actualList, expectedList)

    def test_negative(self):
        testList = [-4,-1,-3,-2]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = st.bubblesort(testList)
        self.assertEqual(actualList, expectedList)
    
    def test_random(self):
        testList = [random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20)]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = st.bubblesort(testList)
        self.assertEqual(actualList, expectedList)
    
    
    def test_reverse(self):
        testList = [-4,-1,-3,-2]
        expectedList = testList.copy()
        expectedList.sort()
        expectedList.reverse()
        actualList = st.bubblesort(testList, 1)
        self.assertEqual(actualList, expectedList)