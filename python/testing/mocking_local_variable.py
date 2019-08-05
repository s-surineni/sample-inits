from unittest.mock import patch
from unittest.mock import Mock
import time

def keep_trying():
    print(time.time())          # Here local variable in time has been modified to use the mock value

@patch.object(time, 'time')
def test_keep_trying(mock_time):
    mock_time.side_effect = iter([100, 200, 300, 400, 500, 600, 700, 800])
    for i in range(5):
        keep_trying()

# test_keep_trying()

@patch('__main__.time')
def test_changing_time_object(mock_time):
    mock_time.time.side_effect = iter([100, 200, 300, 500, 600])
    for i in range(5):
        keep_trying()


# test_changing_time_object()

class Hi:
    def sayHi(self):
        print(Hi)


def use_hi():
    hi = Hi()
    print(hi)
    print(hi.sayHi())


@patch('__main__.Hi')
def test_use_hi(mock_hi):
    # mock_hi.sayHi = Mock(return_value='Mock hey')
    mock_hi.sayHi.return_value = 'mock_hei'
    use_hi()
    print(mock_hi.sayHi())
    assert mock_hi.called

test_use_hi()
