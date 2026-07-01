from google.adk.agents import SequentialAgent
from .prompt_builder.agent import prompt_builder_agent

image_generator_agent = SequentialAgent(
    name="ImageGeneratorAgent",
    sub_agents=[
        prompt_builder_agent,
    ],
)


""" deprecated 개선 코드
from google.adk.workflow import START, Workflow
from .prompt_builder.agent import prompt_builder_agent

image_generator_agent = Workflow(
    name="ImageGeneratorAgent",
    edges=[
        (START, prompt_builder_agent),
    ],
)

"""