# pylint: disable=unused-argument
from dagster import InputDefinition, ModeDefinition, input_manager, pipeline, solid


def read_dataframe_from_table(**_kwargs):
    pass


# start_marker
@solid(input_defs=[InputDefinition("dataframe", manager_key="my_root_manager")])
def my_solid(_, dataframe):
    """Do some stuff"""


@input_manager
def table1_loader(_, _resource_config):
    return read_dataframe_from_table(name="table1")


@pipeline(mode_defs=[ModeDefinition(resource_defs={"my_root_manager": table1_loader})])
def my_pipeline():
    my_solid()


# end_marker
