<p align="center">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="img/oxy-playgrounds-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="img/oxy-playgrounds-light.svg">
    <img src="img/oxy-playgrounds-light.svg" style="width: 40%; height: 40%;" alt="oxy logo">
</picture>
<br>
<a href="https://docs.oxy.rs"><img src="https://img.shields.io/badge/📖 docs-oxy.rs-dca282.svg" /></a> &nbsp;
<a href="https://docs.rs/oxy-core/latest/oxy/"><img src="https://img.shields.io/badge/docs-API Reference-dca282.svg" /></a> &nbsp;
<a href="https://crates.io/crates/oxy-core"><img src="https://img.shields.io/crates/v/oxy-core.svg?color=dca282" /></a>
&nbsp;
<a href="https://crates.io/crates/oxy-core"><img src="https://img.shields.io/crates/d/oxy-core.svg?color=dca282" /></a>
</br>
<a href="https://discord.gg/playgrounds"><img src="https://img.shields.io/discord/511303648119226382?color=%236d82cc&label=Discord&logo=discord&logoColor=white" /></a>
&nbsp;
<a href="https://github.com/dannyglendale/oxy"><img src="https://img.shields.io/github/stars/dannyglendale/oxy?style=social" alt="stars - oxy" /></a>
<br>
<a href=""><img src="https://img.shields.io/badge/built_with-Rust-dca282.svg?logo=rust" /></a>
&nbsp;
<a href="https://twitter.com/Playgrounds0x"><img src="https://img.shields.io/twitter/follow/Playgrounds0x"></a> &nbsp

<br>
</p>
&nbsp;


<div align="center">

[📑 Docs](https://docs.oxy.rs)
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
[🌐 Website](https://oxy.rs)
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
[🤝 Contribute](https://github.com/dannyglendale/oxy/issues/new)
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
[✍🏽 Blogs](https://docs.oxy.rs/guides)

</div>

✨ If you would like to help spread the word about oxy, please consider starring the repo!

> [!WARNING]
> Here be dragons! As we plan to ship a torrent of features in the following months, future updates **will** contain **breaking changes**. With oxy evolving, we'll annotate changes and highlight migration paths as we encounter them.


## What is oxy?
oxy is a Rust library for building scalable, modular, and ergonomic **LLM-powered** applications.

More information about this crate can be found in the [official](https://docs.oxy.rs) & [crate](https://docs.rs/oxy-core/latest/oxy/) (API Reference) documentations.

Help us improve oxy by contributing to our [Feedback form](https://bit.ly/oxy-Feeback-Form).

## Table of contents

- [What is oxy?](#what-is-oxy)
- [Table of contents](#table-of-contents)
- [High-level features](#high-level-features)
- [Get Started](#get-started)
  - [Simple example:](#simple-example)
- [Integrations](#integrations)

## High-level features
- Full support for LLM completion and embedding workflows
- Simple but powerful common abstractions over LLM providers (e.g. OpenAI, Cohere) and vector stores (e.g. MongoDB, SQlite, in-memory)
- Integrate LLMs in your app with minimal boilerplate



## Get Started
```bash
cargo add oxy-core
```

### Simple example:
```rust
use oxy::{completion::Prompt, providers::openai};

#[tokio::main]
async fn main() {
    // Create OpenAI client and model
    // This requires the `OPENAI_API_KEY` environment variable to be set.
    let openai_client = openai::Client::from_env();

    let gpt4 = openai_client.agent("gpt-4").build();

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

You can find more examples each crate's `examples` (ie. [`oxy-core/examples`](./oxy-core/examples)) directory. More detailed use cases walkthroughs are regularly published on our [Dev.to Blog](https://dev.to/0thtachi) and added to oxy's official documentation [(docs.oxy.rs)](http://docs.oxy.rs).

## Supported Integrations

| Model Providers |                                                                                                                                                                                                                                                                                                               Vector Stores                                                                                                                                                                                                                                                                                                               |
|:--------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| <br><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/1024px-ChatGPT_logo.svg.png" alt="ChatGPT logo" width="50em"> <picture><source media="(prefers-color-scheme: dark)" srcset="https://www.fahimai.com/wp-content/uploads/2024/06/Untitled-design-7.png"><source media="(prefers-color-scheme: light)" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Claude_Ai.svg/1024px-Claude_Ai.svg.png"><img src="https://www.fahimai.com/wp-content/uploads/2024/06/Untitled-design-7.png" alt="Claude Anthropic logo" width="50em"></picture> <br> <img src="https://cdn.sanity.io/images/rjtqmwfu/production/0adbf394439f4cd0ab8b5b3b6fe1da10c8099024-201x200.svg" alt="Cohere logo" width="50em"> <img src="https://logospng.org/download/google-gemini/google-gemini-1024.png" style="background-color: white; border-radius: 10px; padding: 5px 5px ; width: 3em;" alt="Gemini logo"> <br> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/XAI-Logo.svg/512px-XAI-Logo.svg.png?20240912222841" style="background-color: white; border-radius: 10px; padding: 5px 5px ; width: 3em;" alt="xAI logo"> <img src="https://github.com/user-attachments/assets/4763ae96-ddc9-4f69-ab38-23592e6c4ead" style="background-color: white; border-radius: 10px; padding: 5px 0px ; width: 4em;" alt="perplexity logo">| <br><img src="https://cdn.prod.website-files.com/6640cd28f51f13175e577c05/664e00a400e23f104ed2b6cd_3b3dd6e8-8a73-5879-84a9-a42d5b910c74.svg" alt="Mongo DB logo" width="50em"> <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/Neo4j-logo_color.png" alt="Neo4j logo" style="background-color: white; border-radius: 1em; padding: 1em 1em ; width: 4em;"><br><br><img src="https://cdn-images-1.medium.com/max/844/1*Jp6VwF0OcdeyRyW0Ln0RMQ@2x.png" width="100em" alt="Lance DB logo"> <br> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/440px-SQLite370.svg.png" style="width: 6em"> |


Vector stores are available as separate companion-crates:
- MongoDB vector store: [`oxy-mongodb`](https://github.com/dannyglendale/oxy/tree/main/oxy-mongodb)
- LanceDB vector store: [`oxy-lancedb`](https://github.com/dannyglendale/oxy/tree/main/oxy-lancedb)
- Neo4j vector store: [`oxy-neo4j`](https://github.com/dannyglendale/oxy/tree/main/oxy-neo4j)
- Qdrant vector store: [`oxy-qdrant`](https://github.com/dannyglendale/oxy/tree/main/oxy-qdrant)
- SQLite vector store: [`oxy-sqlite`](https://github.com/dannyglendale/oxy/tree/main/oxy-sqlite)


<p align="center">
<br>
<br>
<img src="img/built-by-playgrounds.svg" alt="Build by Playgrounds" width="30%">
</p>
