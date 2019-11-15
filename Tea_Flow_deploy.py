from Tea_Flow import List_Teas
from prefect.environments.storage import Docker

storage = Docker(
    base_image="python:3.7",
    python_dependencies=[],
    registry_url="znicholasbrown/prefect_flows",
    image_name="tea-flow",
    image_tag="tea-flow",
)


List_Teas.deploy("Flow Schematics", storage)