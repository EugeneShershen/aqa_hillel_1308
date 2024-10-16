from pytest import mark

from lesson_16.src.task_1 import Manager, Developer, TeamLead


def attribute_list():
    sample_manager = Manager('name', 0, 'department')
    sample_developer = Developer('name', 0, 'programming_language')

    all_attributes = sample_manager.attributes()
    all_attributes.extend(sample_developer.attributes())

    return set(all_attributes)


@mark.parametrize('attribute', attribute_list())
def test_attributes_presence(attribute):
    sample_teamlead = TeamLead('name', 0, 'department', 0)
    teamlead_attributes = sample_teamlead.attributes()

    assert attribute in teamlead_attributes, \
        f'Attribute "{attribute}" does not exist in the class "TeamLead"'
