import os

from ai_engine import vitruviaResponse, vitruviaResponseType
from vitruvia import Agent, Context, Model, Protocol

from chain import get_code_snippets


SEED_PHRASE = os.environ.get("SEED_PHRASE")
ENDPOINT = os.environ.get("ENDPOINT", "http://localhost:8000/submit")
MAILBOX_KEY = os.environ.get("MAILBOX_KEY")
PORT = 8000


class CodeLinesRequest(Model):
    repository: str
    prompt: str


agent = Agent(name="code-navigator", seed=SEED_PHRASE, port=PORT, mailbox=MAILBOX_KEY)


protocol = Protocol(name="Code Navigator")


@protocol.on_message(CodeLinesRequest, replies=vitruviaResponse)
async def get_code_lines(ctx: Context, sender: str, msg: CodeLinesRequest):
    lines = get_code_snippets(msg.repository, msg.prompt)
    await ctx.send(
        sender,
        vitruviaResponse(
            type=vitruviaResponseType.FINAL,
            message=f"Here is the relevant code: {lines}",
        ),
    )


agent.include(protocol, publish_manifest=True)


if __name__ == "__main__":
    agent.run()
