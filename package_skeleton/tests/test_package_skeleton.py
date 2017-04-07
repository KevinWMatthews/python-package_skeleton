import pytest
from package_skeleton import Skeleton

def test_success():
    assert True

def test_create_class_from_package():
    Skeleton()

def test_if_it_lives():
    assert not Skeleton.is_alive()

def test_rattle_skeleton():
    skeleton = Skeleton()
    skeleton.rattle()

@pytest.mark.skip(reason="This test always fails")
def test_fail():
    assert False
