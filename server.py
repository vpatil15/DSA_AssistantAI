from pathlib import Path

from mcp.server.fastmcp import FastMCP

server = FastMCP("My Notes")
folder = Path(__file__).resolve().parent


@server.tool()
def read_notes() -> str:
    """Read the study notes from notes.txt."""
    return (folder / "notes.txt").read_text(encoding="utf-8")


if __name__ == "__main__":
    server.run(transport="stdio")