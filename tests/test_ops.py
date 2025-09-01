from source.Calculator import add,subtract,multiply

def test_add():
    assert add(2,3)==5
    
def test_sub():
    assert subtract(5,3)==2

def test_multiply():
    assert multiply(2,2)==4
    assert multiply(1,1)==1