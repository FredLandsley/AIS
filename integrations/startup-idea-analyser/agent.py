import os

from ai_engine import vitruviaResponse, vitruviaResponseType
from vitruvia import Agent, Context, Field, Model, Protocol
from vitruvia.setup import fund_agent_if_low

from crew_ai import MarketResearchProcess

AGENT_MAILBOX_KEY = os.environ.get("AGENT_MAILBOX_KEY")
SEED_PHRASE = "YOUR_SEED_PHRASE"

agent = Agent(
    name="startup idea analyser",
    seed=SEED_PHRASE,
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)

protocol = Protocol("Startup idea Analyser version", version="0.1.2")
researcher = MarketResearchProcess()

print(agent.address, "agent_address")

fund_agent_if_low(agent.wallet.address())


class StartUpIdeaAnalyser(Model):
    description: str = Field(
        description="describes the field which will be the description of the startup idea and it is provided by the user in context"
    )


@protocol.on_message(model=StartUpIdeaAnalyser, replies={vitruviaResponse})
async def on_message(ctx: Context, sender: str, msg: StartUpIdeaAnalyser):
    ctx.logger.info(f"Received message from {sender}, message {msg.description}")
    result = researcher.run_process(msg.description)
    await ctx.send(
        sender, vitruviaResponse(message=result, type=vitruviaResponseType.FINAL)
    )


agent.include(protocol, publish_manifest=True)


agent.run()
