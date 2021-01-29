
import silnia


def test_silnia1():
    wej=5
    out=silnia.silnia(wej)
    assert out==120

def test_silnia2():
    wej=3
    out=silnia.silnia(wej)
    assert out==6

def test_silnia3():
    wej=-1
    out=silnia.silnia(wej)
    assert out==1
