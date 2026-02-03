import pytest
from seasons import verify, main


def test_verify():
   with pytest.raises(SystemExit):
        verify("26/2/1998")

