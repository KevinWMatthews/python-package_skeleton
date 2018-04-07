import pytest
from package_skeleton import Skeleton

def test_success():
    assert True

@pytest.mark.skip(reason="This test always fails")
def test_skip_this():
    assert False

class TestExamples(object):
    def test_group_tests_in_a_class(self):
        assert not False

class TestSkeleton(object):
    def test_create_class_from_package(self):
        Skeleton()

    def test_is_not_alive(self):
        assert not Skeleton.is_alive()

    def test_rattle_skeleton(self):
        skeleton = Skeleton()
        assert 'Rattle rattle!' == skeleton.rattle()
