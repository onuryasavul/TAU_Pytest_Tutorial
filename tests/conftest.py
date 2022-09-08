import pytest
from stuff.accum import Accumulator

@pytest.fixture
def fixture_sample():
    print("New test is starting...")


@pytest.fixture
def accum():
    return Accumulator()


@pytest.fixture
def accum_one():
    print("Set up!")
    yield Accumulator(1)
    print("Clean up!")
