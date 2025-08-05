from fastmcp import FastMCP, Context

mcp = FastMCP("SQL Analysis Server")

@mcp.tool()
async def analyze_sql_for_mapping(sql: str, ctx: Context) -> str:
    """Prompts the LLM to analyze a single SQL statement and return the columns and tables."""
    prompt = f"Analyze the following SQL statement and return the columns and tables it uses:\n\n```sql\n{sql}\n```"
    response = await ctx.sample(prompt)

    if response.type == 'text':
        return response.text

    raise TypeError(f"Expected text content, but got a '{response.type}' content block.")

if __name__ == "__main__":
    mcp.run()