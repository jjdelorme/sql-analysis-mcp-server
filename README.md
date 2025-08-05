# Model Context Protocol (MCP) Server

This project is a simple example of a server that implements the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/), which tests using "sampling" where available on the MCP client.

## Prerequisites

*   Python 3.x
*   [uv](https://github.com/astral-sh/uv): A fast Python package installer and resolver.
*   [fastmcp](https://pypi.org/project/fastmcp/): A library for building MCP servers and clients.
*   [Node.js](https://nodejs.org/) and npm (to use `npx`).

## Installation

1.  **Install dependencies:**

    Use `uv` to sync the project's dependencies from `pyproject.toml` and `uv.lock`. This will install `fastmcp` and other necessary packages.
    ```bash
    uv sync
    ```

## Running the Server in Development

To run the server and inspect it with the MCP Inspector tool, execute the following command in your terminal. You can find more information about the inspector tool in the [official documentation](https://modelcontextprotocol.io/legacy/tools/inspector#python).

```bash
npx @modelcontextprotocol/inspector uv run mcp_server.py
```

This command does the following:
-   `npx @modelcontextprotocol/inspector`: Downloads and runs the official MCP Inspector.
-   `uv run mcp_server.py`: The inspector then uses `uv` to execute the `mcp_server.py` script within the project's managed virtual environment.

The inspector will launch in your web browser, providing a user interface to interact with the running MCP server.

## Running the Server in Production

In a production environment, an MCP client would connect to the server. The client needs a configuration that tells it how to start and communicate with the server. This is typically done with a JSON configuration file.

You can generate the JSON configuration for this server using the `fastmcp` command-line tool:

```bash
fastmcp install mcp-json mcp_server.py
```

This will output a JSON object that you can use to configure an MCP client. The generated configuration for this server will look like this:

```json
{
  "mcpServers": {
    "sql-analysis-server": {
      "command": "uv",
      "args": ["run", "mcp_server.py"],
      "cwd": "/home/your-dev-folder/sql-analysis-mcp-server"
    }
  }
}

```

This configuration tells the client to start the "sql-analysis-server" by running the command `uv run mcp_server.py` and to communicate with it using the standard input/output (`stdio`) transport.