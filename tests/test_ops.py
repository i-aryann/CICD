from source.Calculator import add,subtract

def test_add():
    assert add(2,3)==5
    
def test_sub():
    assert subtract(5,3)==2