# CourtListener MCP Server

A Model Context Protocol (MCP) server that provides LLM-friendly access to the CourtListener legal database and the Electronic Code of Federal Regulations (eCFR) through the official CourtListener API v4. This server enables searching and retrieving legal opinions, court cases, judges, legal documents, and federal regulations for precise legal research and citation verification.

## 🎯 Purpose

The CourtListener MCP Server provides comprehensive access to **legal case data, court opinions, and federal regulations** through the extensive CourtListener and eCFR databases. CourtListener contains millions of legal opinions from federal and state courts, while eCFR provides up-to-date federal regulations.

## 📋 Key Advantages

- **Comprehensive Legal Database:**
  - Access to millions of court opinions and legal decisions
  - Federal and state court coverage
  - Real-time updates from court systems
- **Full Text Content:**
  - Complete opinion text for citation verification
  - Structured legal document organization
  - Rich metadata including judges, courts, and dates
- **Regulatory Research:**
  - Search and retrieve current federal regulations
  - Validate regulatory citations and references
- **Legal Research:**
  - Search by judge, court, case name, or content
  - Verify exact legal language and precedents
  - Validate legal citations and references

## 🛠️ Available MCP Tools

The CourtListener MCP Server provides these production-ready tools (see [app/README.md](app/README.md) for full details and parameters):

- **Opinion & Case Search:**
  - `search_opinions` — Search legal opinions and court decisions
  - `search_dockets` — Search court cases and dockets
  - `search_dockets_with_documents` — Search dockets with nested documents
  - `search_recap_documents` — Search RECAP filing documents
  - `search_audio` — Search oral argument audio
  - `search_people` — Search judges and legal professionals
  - `search_financial_disclosures` — Search judge financial disclosure reports
- **Entity Retrieval:**
  - `get_opinion`, `get_docket`, `get_audio`, `get_court`, `get_person`, `get_cluster`
  - `get_financial_disclosure` — Get judge financial disclosure details
  - `get_position` — Get judge position/appointment information
  - `get_education` — Get judge education information
  - `get_school` — Get law school information
  - `get_docket_entry` — Get specific docket entry details
  - `get_originating_court_information` — Get originating court details
- **Citation & Regulation Tools:**
  - `lookup_citation`, `batch_lookup_citations`, `verify_citation_format`, `parse_citation_with_citeurl`, `extract_citations_from_text`, `enhanced_citation_lookup`
  - `list_titles`, `list_agencies`, `search_regulations`, `list_all_corrections`, `list_corrections_by_title`, `get_search_suggestions`, `get_search_summary`, `get_title_search_counts`, `get_daily_search_counts`, `get_ancestry`, `get_title_structure`, `get_source_xml`, `get_source_json`
- **System & Health:**
  - `status`, `get_api_status`, `health_check`

See [app/README.md](app/README.md) for a full reference of all tools, parameters, and usage examples.

## 📦 Installation

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) for dependency management
- Internet connection for CourtListener API access

### Install with uv

```bash
# Clone the repository
 git clone <repository-url>
 cd CourtListener

# Install dependencies
 uv sync

# Activate the environment (optional)
 uv shell
```

### Environment Configuration

Create a `.env` file in the project root:

```bash
COURTLISTENER_BASE_URL=https://www.courtlistener.com/api/rest/v4/
COURT_LISTENER_TIMEOUT=30
LOG_LEVEL=INFO
RATE_LIMIT_REQUESTS=10
RATE_LIMIT_PERIOD=60
DEBUG=false
MCP_PORT=8765
MCP_DEV_PORT=8766
```

### Running the Server

The server now runs with streamable-http transport by default:

```bash
uv run python -m app.server
```

This will start the server at:

- **Host**: `0.0.0.0` (accessible from external connections)
- **Port**: `8000`
- **Endpoint**: `http://localhost:8000/mcp/`

Or use the VS Code task: **Run MCP Server**

## 🔌 Connecting to the Server

### Option 1: One-Click Installation (MCPB Bundle) ⚡

**Download:** [`courtlistener-mcp-1.0.0.mcpb`](https://github.com/roycedamien/court-listener-mcp/releases/latest/download/courtlistener-mcp-1.0.0.mcpb)

This server is packaged as an [MCPB (MCP Bundle)](https://github.com/modelcontextprotocol/mcpb) for one-click installation:

- **Claude Desktop (macOS/Windows):** Double-click the `.mcpb` file to install
- **109KB download** - Dependencies installed automatically via `uv`
- **Auto-updates** when new versions are released
- **Easy configuration** - API key can be set in Claude Desktop settings

MCPB bundles are like browser extensions for MCP servers - simply download and open the file!

**Requirements:**

- Python 3.12+ must be installed on your system
- `uv` package manager (bundled with Claude Desktop, or install via `curl -LsSf https://astral.sh/uv/install.sh | sh`)

**Note:** After first launch, `uv` will automatically install all Python dependencies. This may take a minute.

### Option 2: Claude Desktop (Manual Configuration)

Claude Desktop supports MCP servers via the `streamable-http` transport. Add this configuration to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "courtlistener": {
      "transport": {
        "type": "streamable-http",
        "url": "http://localhost:8000/mcp/"
      },
      "env": {
        "COURT_LISTENER_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Important Notes:**

- Start the MCP server first: `uv run python -m app.server`
- The server must be running before starting Claude Desktop
- Restart Claude Desktop after adding the configuration
- The API key is optional for public endpoints but recommended for higher rate limits

After restarting Claude Desktop, you'll see the CourtListener tools available in your conversation. You can ask Claude to:

- "Search for recent Supreme Court opinions on privacy"
- "Look up citation 410 U.S. 113"
- "Find financial disclosures for judges in the 9th Circuit"

### Option 3: Perplexity (via Connectors - Coming Soon)

Perplexity uses a "Connectors" system for integrating external data sources. While Perplexity doesn't currently support custom MCP server connections in the same way as Claude Desktop, they have announced plans for expanded connector capabilities.

**Current Status:** Perplexity connectors are primarily for built-in integrations (Google Drive, Slack, etc.)

**Future Integration:** As Perplexity expands their connector ecosystem to support MCP or custom APIs, this server could be integrated. Monitor [Perplexity's documentation](https://docs.perplexity.ai) for updates on custom connector support.

**Alternative:** Use the CourtListener MCP server with other MCP-compatible clients (Claude Desktop, VS Code, Cursor) and reference those results in Perplexity conversations.

### Option 4: VS Code with Cline/Continue

For VS Code extensions like [Cline](https://github.com/cline/cline) or [Continue](https://continue.dev/), add to your MCP settings:

**Cline**: Settings → MCP Servers → Add Server

```json
{
  "mcpServers": {
    "courtlistener": {
      "transport": {
        "type": "streamable-http",
        "url": "http://localhost:8000/mcp/"
      },
      "env": {
        "COURT_LISTENER_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Continue**: `.continue/config.json` in your project or `~/.continue/config.json`

```json
{
  "mcpServers": [
    {
      "name": "courtlistener",
      "transport": {
        "type": "streamable-http",
        "url": "http://localhost:8000/mcp/"
      },
      "env": {
        "COURT_LISTENER_API_KEY": "your_api_key_here"
      }
    }
  ]
}
```

### Option 5: Direct Python Client

When using the streamable-http transport, clients can connect to the server using:

```python
from fastmcp import Client

async with Client("http://localhost:8000/mcp/") as client:
    result = await client.call_tool("status")
    print(result)
```

### Getting a CourtListener API Key

1. Visit [CourtListener](https://www.courtlistener.com/)
2. Create a free account
3. Navigate to your profile settings
4. Generate an API key
5. Add it to your `.env` file or MCP client configuration

**Note**: The API key is optional for read-only public endpoints, but recommended to avoid rate limiting.

## 💡 Usage Examples

See [app/README.md](app/README.md) for detailed tool usage and examples, including search, citation, and regulatory queries.

## 🐳 Docker Setup

```bash
# Production
 docker-compose up -d
# Development with hot reload
 docker-compose --profile dev up --build
```

## 🧪 Testing

```bash
uv run pytest
uv run pytest --cov=app --cov-report=term-missing
```

See [tests/README.md](tests/README.md) for test suite details, coverage, and troubleshooting.

## 🔧 Development

```bash
uv run ruff format .
uv run ruff check .
uv run mypy app/
uv run pip-audit
```

## 🚨 Troubleshooting

See [app/README.md](app/README.md) and [tests/README.md](tests/README.md) for troubleshooting and advanced usage.

## 📚 Documentation

- [Source Code Documentation](app/README.md)
- [Test Documentation](tests/README.md)
- [Pro Se Medical Malpractice Research Guide](docs/PRO_SE_GUIDE.md) ⚖️ **NEW**
- [Project Context](context.json)
- [CourtListener API Documentation](https://www.courtlistener.com/api/rest/v4/)
- [eCFR API Documentation](https://www.ecfr.gov/developers/documentation/api/v1)
- [FastMCP Framework](https://github.com/jlowin/fastmcp)
- [Model Context Protocol](https://spec.modelcontextprotocol.io/)

---

**Ready to use!** The CourtListener MCP Server provides production-ready access to federal regulations and legal data through 20+ comprehensive MCP tools.
