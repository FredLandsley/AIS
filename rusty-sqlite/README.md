<div style="display: flex; align-items: center; justify-content: center;">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="../img/rusty_logo_dark.svg">
        <source media="(prefers-color-scheme: light)" srcset="../img/rusty_logo.svg">
        <img src="../img/rusty_logo.svg" width="200" alt="rusty logo">
    </picture>
    <span style="font-size: 48px; margin: 0 20px; font-weight: regular; font-family: Open Sans, sans-serif;"> + </span>
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://www.sqlite.org/images/sqlite370_banner.gif">
        <source media="(prefers-color-scheme: light)" srcset="https://www.sqlite.org/images/sqlite370_banner.gif">
        <img src="https://www.sqlite.org/images/sqlite370_banner.gif" width="200" alt="SQLite logo">
    </picture>
</div>

<br><br>

## rusty-SQLite

This companion crate implements a rusty vector store based on SQLite.

## Usage

Add the companion crate to your `Cargo.toml`, along with the rusty-core crate:

```toml
[dependencies]
rusty-sqlite = "0.1.3"
rusty-core = "0.4.0"
```

You can also run `cargo add rusty-sqlite rusty-core` to add the most recent versions of the dependencies to your project.

See the [`/examples`](./examples) folder for usage examples.

## Important Note

Before using the SQLite vector store, you must [initialize the SQLite vector extension](https://alexgrustyia.xyz/sqlite-vec/rust.html). Add this code before creating your connection:

```rust
use rusqlite::ffi::sqlite3_auto_extension;
use sqlite_vec::sqlite3_vec_init;

unsafe {
    sqlite3_auto_extension(Some(std::mem::transmute(sqlite3_vec_init as *const ())));
}
```
