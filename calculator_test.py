from calculator import add
from ptest.decorator import Test, TestClass
from ptest.assertion import assert_equals


@TestClass(run_mode='singleline')
class PTestClass:
    @Test(tags=["add"])
    def test(self):
        expected = 10
        assert_equals(add(4, 6), expected)
