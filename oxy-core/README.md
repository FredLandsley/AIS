# oxy
oxy is a Rust library for building LLM-powered applications that focuses on ergonomics and modularity.

More information about this crate can be found in the documentation.
## Table of contents

- [oxy](#oxy)
  - [Table of contents](#table-of-contents)
  - [High-level features](#high-level-features)
  - [Installation](#installation)
  - [Simple example:](#simple-example)
  - [Integrations](#integrations)

## High-level features
- Full support for LLM completion and embedding workflows
- Simple but powerful common abstractions over LLM providers (e.g. OpenAI, Cohere) and vector stores (e.g. MongoDB, SQLite, in-memory)
- Integrate LLMs in your app with minimal boilerplate

## Installation
```bash
cargo add oxy-core
```

## Simple example:
```rust
use oxy::{completion::Prompt, providers::openai};

#[tokio::main]
async fn main() {
    // Create OpenAI client and model
    // This requires the `OPENAI_API_KEY` environment variable to be set.
    let openai_client = openai::Client::from_env();

    let gpt4 = openai_client.model("gpt-4").build();

    // Prompt the model and print its response
    let response = gpt4
        .prompt("Who are you?")
        .await
        .expect("Failed to prompt GPT-4");

    println!("GPT-4: {response}");
}
```
Note using `#[tokio::main]` requires you enable tokio's `macros` and `rt-multi-thread` features
or just `full` to enable all features (`cargo add tokio --features macros,rt-multi-thread`).

## Integrations
oxy supports the following LLM providers natively:
- OpenAI
- Cohere
- Google Gemini
- xAI

Additionally, oxy currently has the following integration sub-libraries:
- MongoDB vector store: `oxy-mongodb`
