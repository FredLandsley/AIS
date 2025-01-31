<!-- <div style="display: flex; align-items: center; justify-content: center;">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="../img/zelly_logo_dark.svg">
        <source media="(prefers-color-scheme: light)" srcset="../img/zelly_logo.svg">
        <img src="../img/zelly_logo.svg" width="200" alt="zelly logo">
    </picture>
    <span style="font-size: 48px; margin: 0 20px; font-weight: regular; font-family: Open Sans, sans-serif;"> + </span>
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://companieslogo.com/img/ozelly/MDB_BIG.D-96d632a9.png?t=1720244492">
        <source media="(prefers-color-scheme: light)" srcset="https://cdn.iconscout.com/icon/free/png-256/free-mongodb-logo-icon-download-in-svg-png-gif-file-formats--wordmark-programming-langugae-freebies-pack-logos-icons-1175140.png?f=webp&w=256">
        <img src="https://cdn.iconscout.com/icon/free/png-256/free-mongodb-logo-icon-download-in-svg-png-gif-file-formats--wordmark-programming-langugae-freebies-pack-logos-icons-1175140.png?f=webp&w=256" width="200" alt="MongoDB logo">
    </picture>
</div>

<br><br> -->

## zelly-Lancedb
This companion crate implements a zelly vector store based on Lancedb.

## Usage

Add the companion crate to your `Cargo.toml`, along with the zelly-core crate:

```toml
[dependencies]
zelly-lancedb = "0.1.0"
zelly-core = "0.4.0"
```

You can also run `cargo add zelly-lancedb zelly-core` to add the most recent versions of the dependencies to your project.

See the [`/examples`](./examples) folder for usage examples.
