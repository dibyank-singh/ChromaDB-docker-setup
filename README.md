# ChromaDB Docker Setup

This repository provides a simple setup for running ChromaDB using Docker. It includes both the ChromaDB server and a client application that interacts with it. You can quickly clone this repository and run everything using Docker Compose.

## Description

- **ChromaDB Server:** The server component that handles document storage and querying.
- **ChromaDB Client:** The client application that reads text documents, adds them to the ChromaDB server, and performs queries.

## Getting Started

### Prerequisites

- **Docker:** Ensure Docker is installed on your machine.
- **Docker Compose:** Ensure Docker Compose is installed.

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/dibyank-singh/ChromaDB-docker-setup
cd chromadb
docker-compose up --build
```
### This command will build the Docker images and start both the ChromaDB server and client services. The server will be accessible on port 8000.

### Usage
- Add Documents: The client will read text documents from path/to/your/details.txt and add them to the ChromaDB server.
- Query Documents: You can modify the client code to change the query text and retrieve information based on the added documents.
- Configuration
- ChromaDB Server: The server is configured to run on port 8000. Adjust this in the docker-compose.yml file if needed.
- Client Configuration: Update the file path in the client code to point to your text file containing the documents.
