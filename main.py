from typing import Any
from mcp.server.fastmcp import FastMCP
import uuid

mcp = FastMCP("mcp_sample_uuid")

@mcp.tool()
async def get_uuid() -> str:
    """
    Get the UUID of the current user.
    """
    return str(uuid.uuid4())

if __name__ == "__main__":
    mcp.run(transport='stdio')