from crewai import Agent
from tools import youtube_channel_tool
## creating a senior blog content creator agent
blog_researcher=Agent(
    role="senior blong Researcher from the youtube videoes",
    goal="get the relavent video content from youtube for the topic{topic} from the yt channel",
    verbose= True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning  and Gen AI"
  
    
),
tools=[youtube_channel_tool],
allow_delegation=True
)
   
## vlog writer agent
blog_writer=Agent(
    role="Writer",
    goal="Narrate compelling tech stories about the video{topic}",
    verbose=True,
    memory=True,
    backstory=(
    "With a flair for simplyfying complex topics, you crafts"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accesssible manner."),
     tools=[youtube_channel_tool],
     allow_delegation=False
    
)
