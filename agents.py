from crewai import Agent
## creating a senior blog content creator agent
blong_researcher=Agent(
    role="senior blong Researcher from the youtube videoes",
    goal="get the relavent video content from youtube for the topic{topic} from the yt channel",
    verbose= True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning  and Gen AI"
  
    
),
tools=[],
allow_delegation=True
)
    backstory=(
    "With a flair for simplyfying complex topics, you crafts"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accesssible manner.")
## vlog writer agent
blog_writer=Agent(
    
)