use AIS::providers::xai; // Import xAI provider
use AIS::Embed; // Import embedding functionality

#[derive(Embed, Debug)]
struct Greetings {
    #[embed]
    message: String, // Field to be embedded
}

#[tokio::main]
async fn main() -> Result<(), anyhow::Error> {
    // Initialize xAI client from environment variables
    let client = xai::Client::from_env();

    // Create embeddings for the provided messages
    let embeddings = client
        .embeddings(xai::embedding::EMBEDDING_V1)
        .document(Greetings {
            message: "Hello, world!".to_string(),
        })?
        .document(Greetings {
            message: "Goodbye, world!".to_string(),
        })?
        .build()
        .await
        .expect("Failed to embed documents");

    // Output the embeddings
    println!("{:?}", embeddings);

    Ok(())
}
