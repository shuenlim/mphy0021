import yaml
import os
from ..laboratory import Laboratory
import pytest

with open(os.path.join(os.path.dirname(__file__),
                       'fixtures.yml')) as fixtures_file:
    fixtures = yaml.load(fixtures_file)
empty_lab = {'lower': [], 'upper': []}


@pytest.mark.parametrize("fixture", fixtures['can_react'])
def test_can_react(fixture):
    result = fixture.pop('result')
    assert Laboratory(empty_lab).can_react(**fixture) == result


@pytest.mark.parametrize("fixture", fixtures['antianti'])
def test_antianti(fixture):
    with pytest.raises(TypeError, message="antianti products not permitted!"):
        Laboratory(empty_lab).can_react(**fixture)
        pass


@pytest.mark.parametrize("fixture", fixtures['update_shelves'])
def test_update_shelves(fixture):
    shelf1_result = fixture.pop('shelf1_result')
    shelf2_result = fixture.pop('shelf2_result')
    assert Laboratory(empty_lab).update_shelves(**fixture) == (
            shelf1_result, shelf2_result)


@pytest.mark.parametrize("fixture", fixtures['do_a_reaction'])
def test_do_a_reaction(fixture):
    shelf1_result = fixture.pop('shelf1_result')
    shelf2_result = fixture.pop('shelf2_result')
    assert (Laboratory(fixture).do_a_reaction()[0] in
            shelf1_result) and (Laboratory(fixture).do_a_reaction()[1]
                                in shelf2_result)


@pytest.mark.parametrize("fixture", fixtures['run_full_experiment'])
def test_run_full_experiment(fixture):
    shelf1_result = fixture.pop('shelf1_result')
    shelf2_result = fixture.pop('shelf2_result')
    reactions = fixture.pop('reactions')
    answer = Laboratory(fixture).run_full_experiment()
    assert (answer[0] in shelf1_result) and (answer[1] in
                                             shelf2_result) and (answer[2] in
                                                                 reactions)


@pytest.mark.parametrize("fixture", fixtures['three_shelves'])
def test_three_shelves(fixture):
    with pytest.raises(TypeError, message="Too many shelves!"):
        Laboratory(fixture).run_full_experiment()
        pass
