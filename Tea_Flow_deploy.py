from Tea_Flow import List_Teas

List_Teas.deploy(
    "Flow Schematics", 
    base_image="python:3.7",
    python_dependencies=[],
    registry_url="docker.io/znicholasbrown",
    image_name="tea-flow",
    image_tag="tea-flow",
)