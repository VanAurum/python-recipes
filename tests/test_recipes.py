#Standard Python library imports
import unittest

#Local imports
from recipes.recipes import (
    get_combinations,
    sort_on_multiple,
    flatten,
    matrify,
    generate_anagrams,
    get_similarity,
)

class TestRecipes(unittest.TestCase):

    a = [(1,2,3), (5,6,7), (1,1,10)]
    b = [1, 4, 6, 4, 6, 7, 8, 9, 34]
    c = [1,2,3,4]
    d = [[1,2,3], [4,5,6], [7,8,9]]
    e = ['1','2','3','4','5']
    f = 'abcd'
    g = 'abcde'


    def test_get_combinations(self):
        c_exp_01=[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        c_exp_02=[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
        self.assertEqual(get_combinations(self.c,2), c_exp_01)
        self.assertEqual(get_combinations(self.c,3), c_exp_02)

    def test_sort_on_multiple(self):
        a_exp=[(1, 1, 10), (1, 2, 3), (5, 6, 7)]
        self.assertEqual(sort_on_multiple(self.a, [(0,'desc'), (1,'asc')]), a_exp)    

    def test_flatten(self):
        d_exp = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(flatten(self.d), d_exp)

    def test_matrify(self):
        b_exp = [[1,4,6],[4,6,7],[8,9,34]]
        self.assertEqual(matrify(self.b), b_exp)

    def test_generate_anagrams(self):
        f_exp = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 
                'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 
                'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 
                'dbac', 'dbca', 'dcab', 'dcba']
        self.assertEqual(generate_anagrams(self.f), f_exp)        

    def test_get_similarity(self):
        pass



