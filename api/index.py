
import hashlib

from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_request

EMAIL = "24f3001196@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("Live MCP Exam Server")


@mcp.tool()
def solve_challenge() -> str:
    """Calculate the required hash from the current HTTP challenge header."""

    request = get_http_request()
    challenge = request.headers.get("X-Exam-Challenge")

    if not challenge:
        raise ValueError("Missing X-Exam-Challenge header")

    message = f"{challenge}:{EMAIL}"

    answer = hashlib.sha256(
        message.encode("utf-8")
    ).hexdigest()[:16]

    return answer


# Expose the MCP Streamable HTTP application to Vercel.
app = mcp.http_app(path="/", stateless_http=True)

