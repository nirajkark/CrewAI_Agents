from crewai import Task
from tools import youtube_channel_tool
from agents import blog_researcher, blog_writer
research_task= Task(
    description=("Identify the video{topic}."
                 "Get detailed information about the video from the channel"),
    expected_output="A comprehensice 3 paragraphs long report based on the {topic} of video",
    tools=[youtube_channel_tool],
    agents=blog_researcher,
)
writing_task= Task(
    description=("get theinfro from the youtbechanel onthe topc {topic} and write a blog post about it"),
    expected_output="Smmaize the info from the youtube channel videoon the topic {topic} and create the content for the blog",
    tools=[youtube_channel_tool],
    agents=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md',
)

