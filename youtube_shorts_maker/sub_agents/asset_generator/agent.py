from google.adk.agents import ParallelAgent
from .prompt import ASSET_GENERATOR_DESCRIPTION
from .image_generator.agent import image_generator_agent

asset_generator_agent = ParallelAgent(
    name="AssetGeneratorAgent",
    description=ASSET_GENERATOR_DESCRIPTION,
    sub_agents=[
        image_generator_agent,
    ],
)




""" deprecated 개선 코드

from google.adk.workflow import START, Workflow
from .prompt import ASSET_GENERATOR_DESCRIPTION
from .image_generator.agent import image_generator_agent

asset_generator_agent = Workflow(
    name="AssetGeneratorAgent",
    description=ASSET_GENERATOR_DESCRIPTION,
    edges=[
        (START, (image_generator_agent,)),
    ],
)
"""