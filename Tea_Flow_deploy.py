from Tea_Flow import List_Teas

List_Teas.deploy(
    "Flow Schematics", 
    base_image="python:3.7",
    python_dependencies=['pyfiglet'],
    registry_url="znicholasbrown",
    image_name="prefect_flow",
    image_tag="tea-flow",
)