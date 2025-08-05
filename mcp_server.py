from fastmcp import FastMCP, Context
import argparse
import os

mcp = FastMCP("SQL Analysis Server")

sql_path_from_args: str | None = None

@mcp.tool()
def read_sql_file(filename: str) -> str:
    """Reads a SQL file from a pre-configured directory.

    The path to the directory containing SQL files is specified by the `--sql_path` command-line argument when starting the server.
    """
    if sql_path_from_args is None:
        raise ValueError("The `--sql_path` command-line argument must be provided to use this tool.")
    
    full_path = os.path.join(sql_path_from_args, filename)
    with open(full_path) as f:
        return f.read()

@mcp.tool()
async def analyze_sql_for_mapping(sql: str, ctx: Context) -> str:
    """Prompts the LLM to analyze a single SQL statement and return the columns and tables."""
    prompt = f"Analyze the following SQL statement and return the columns and tables it uses:\n\n```sql\n{sql}\n```"
    response = await ctx.sample(prompt)

    if response.type == 'text':
        return response.text

    raise TypeError(f"Expected text content, but got a '{response.type}' content block.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SQL Analysis Server")
    parser.add_argument("--sql_path", type=str, help="Path to the directory containing SQL files.")
    args, unknown = parser.parse_known_args()
    sql_path_from_args = args.sql_path
    mcp.run()