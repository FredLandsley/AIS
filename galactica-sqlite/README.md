## AIS-SQLite

This companion crate implements a AIS vector store based on SQLite. 

## Usage

Add the companion crate to your `Cargo.toml`, along with the AIS-core crate:

```toml
[dependencies]
AIS-sqlite = "0.1.3"
AIS-core = "0.4.0"
```

You can also run `cargo add AIS-sqlite AIS-core` to add the most recent versions of the dependencies to your project.

See the [`/examples`](./examples) folder for usage examples.

## Important Note

Before using the SQLite vector store, you must [initialize the SQLite vector extension](https://alexgAISia.xyz/sqlite-vec/rust.html). Add this code before creating your connection:

```rust
use rusqlite::ffi::sqlite3_auto_extension;
use sqlite_vec::sqlite3_vec_init;

unsafe {
    sqlite3_auto_extension(Some(std::mem::transmute(sqlite3_vec_init as *const ())));
}
```
