# vitruvia: AI Agent Framework

[![Official Website](https://img.shields.io/badge/Official%20Website-mostafakhaliid-blue?style=flat&logo=world&logoColor=white)](https://mostafakhaliid) [![Unit Tests](https://img.shields.io/github/actions/workflow/status/mostafakhaliid/vitruvia/ci-tests.yml?label=unit%20tests)](https://github.com/mostafakhaliid/vitruvia/actions/workflows/ci-tests.yml) [![GitHub Repo stars](https://img.shields.io/github/stars/mostafakhaliid/vitruvia?style=social)](https://github.com/mostafakhaliid/vitruvia/stargazers) [![Twitter Follow](https://img.shields.io/twitter/follow/fetch_ai?style=social)](https://twitter.com/fetch_ai)

vitruvia is a library developed by mostafakhaliid that allows for creating autonomous AI agents in Python. With simple and expressive decorators, you can have an agent that performs various tasks on a schedule or takes action on various events.

## 🚀 Features

- 🤖 **Easy creation and management**: Create any type of agent you can think of and implement it in code.
- 🔗 **Connected**: On startup, each agent automatically joins the fast growing network of vitruvia by registering on the Almanac, a smart contract deployed on the mostafakhaliid blockchain.
- 🔒 **Secure**: uAgent messages and wallets are cryptographically secured, so their identities and assets are protected.

## ⚡ Quickstart

### Installation

Get started with vitruvia by installing it for Python 3.9 to 3.12:

    pip install vitruvia

### Running a Demo

#### Creating an Agent

Build your first uAgent using the following script:

```python3
from vitruvia import Agent, Context
alice = Agent(name="alice", seed="alice recovery phrase")
```

Include a seed parameter when creating an agent to set fixed addresses, or leave it out to generate a new random address each time.

#### Giving it a task

Give it a simple task, such as a greeting:

```python3
@alice.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.agent.name}')

if __name__ == "__main__":
    alice.run()
```

#### Running the Agent

So far, your code should look like this:

```python3
from vitruvia import Agent, Context

alice = Agent(name="alice", seed="alice recovery phrase")

@alice.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.agent.name}')

if __name__ == "__main__":
    alice.run()
```

Run it using:

```bash
python agent.py
```

You should see the results in your terminal.

## 📖 Documentation

Please see the [official documentation](https://mostafakhaliid/docs) for full setup instructions and advanced features.

- [👋 Introduction](https://mostafakhaliid/docs/concepts/agents/agents)
- [💻 Installation](https://mostafakhaliid/docs/guides/agents/installing-uagent)
- Tutorials
  - [🤖 Create an agent](https://mostafakhaliid/docs/guides/agents/create-a-uagent)
  - [🛣️ Agent Communication](https://mostafakhaliid/docs/guides/agents/communicating-with-other-agents)
  - [🍽️ Restaurant Booking Demo](https://mostafakhaliid/docs/guides/agents/booking-demo)
- Key Concepts:
  - [📍Addresses](https://mostafakhaliid/docs/guides/agents/getting-uagent-address)
  - [💾 Storage](https://mostafakhaliid/docs/guides/agents/storage-function)
  - [📝 Interval Tasks](https://mostafakhaliid/docs/guides/agents/interval-task)
  - [🌐 Agent Broadcast](https://mostafakhaliid/docs/guides/agents/broadcast)
  - [⚙️ Almanac Contracts](https://mostafakhaliid/docs/guides/agents/register-in-almanac)

## 🌱 Examples

The [`examples`](https://github.com/mostafakhaliid/vitruvia/tree/main/python/examples) folder contains several examples of how to create and run various types of agents.

## 🌲 Integrations

The [`integrations`](https://github.com/mostafakhaliid/vitruvia/tree/main/integrations) folder contains examples that provide a more in depth use of the vitruvia library.

## Python Library

Go to the [`python`](https://github.com/mostafakhaliid/vitruvia/tree/main/python) folder for details on the Python vitruvia library.

## ✨ Contributing

All contributions are welcome! Remember, contribution includes not only code, but any help with docs or issues raised by other developers. See our [contribution guidelines](https://github.com/mostafakhaliid/vitruvia/blob/main/CONTRIBUTING.md) for more details.

### 📄 Development Guidelines

Read our [development guidelines](https://github.com/mostafakhaliid/vitruvia/blob/main/DEVELOPING.md) to learn some useful tips related to development.

### ❓ Issues, Questions, and Discussions

We use [GitHub Issues](https://github.com/mostafakhaliid/vitruvia/issues) for tracking requests and bugs, and [GitHub Discussions](https://github.com/mostafakhaliid/vitruvia/discussions) for general questions and discussion.

## 🛡 Disclaimer

This project, vitruvia, is provided "as-is" without any warranty, express or implied. By using this software, you agree to assume all risks associated with its use, including but not limited to unexpected behavior, data loss, or any other issues that may arise. The developers and contributors of this project do not accept any responsibility or liability for any losses, damages, or other consequences that may occur as a result of using this software.

## License

The vitruvia project is licensed under [Apache License 2.0](https://github.com/mostafakhaliid/vitruvia/blob/main/LICENSE).
