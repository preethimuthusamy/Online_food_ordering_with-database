import unittest
from pre import food
class Test_pre(unittest.TestCase):
    def setup(self):
        self.a=food('preethi','salad','4a',2)
        #self.b=food(“riya”,”rice”,”west street”,1)
    def teardown(self):
       pass
    def test_getc_name(self):
       self.assertEqual(food.getc_name(),'preethi')
      # self.assertEqual(self.b.getc_name(),”riya”)
    def test_getf_name(self):
        self.assertEqual(food.getf_name(),'salad')
       # self.assertEqual(self.b.getf_name(),”rice”)
    def test_getc_address(self):
        self.assertEqual(food.getc_address(),'4a')
        #self.assertEqual(self.b.getc_address(),”west street”)
    def test_getquantity(self):
        self.assertEqual(food.getquantity(),2)
        #self.assertEqual(self.b.getquantity(),1)
   #def test_getamount(self):
      #  self.assertEqual(self.a.getamount(),1000)
       # self.assertEqual(self.b.getamount(),150)
if __name__=="__main__":
    unittest.main()
