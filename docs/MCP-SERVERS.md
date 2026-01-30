# MCP Servers Guide

This guide provides comprehensive documentation for configuring and using MCP (Model Context Protocol) servers with the Cursor Agent Factory.

## Quick Start

### 1. Choose a Starter Pack

| Pack | Servers | Best For |
|------|---------|----------|
| **Minimal** | filesystem, git, memory | Any project |
| **Web Developer** | + github, postgresql, playwright | Web apps |
| **Data Science** | + jupyter, bigquery, pinecone | Data/ML projects |
| **AI Agent** | + langgraph, knowledge-graph, chromadb | Agent development |
| **Enterprise** | + atlassian, slack, sentry | Team projects |

### 2. Configure MCP

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    },
    "git": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-git", "--repository", "."]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

### 3. Restart Cursor

MCP servers activate on Cursor restart.

---

## Server Catalog

### Category 1: Essential/Core Tools

These servers are recommended for all projects.

#### Filesystem

Secure file read/write/search with configurable access controls.

```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project"]
  }
}
```

- **Auth**: None
- **Setup**: [templates/mcp/filesystem/setup-guide.md](../templates/mcp/filesystem/setup-guide.md)

#### Git

Git repository operations - commits, branches, diffs.

```json
{
  "git": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-git", "--repository", "."]
  }
}
```

- **Auth**: None
- **Setup**: [templates/mcp/git/setup-guide.md](../templates/mcp/git/setup-guide.md)

#### Memory

Persistent knowledge graph for cross-session context.

```json
{
  "memory": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-memory"]
  }
}
```

- **Auth**: None
- **Setup**: [templates/mcp/memory/setup-guide.md](../templates/mcp/memory/setup-guide.md)

#### Brave Search

Web search with 2,000 free queries/month.

```json
{
  "brave-search": {
    "command": "npx",
    "args": ["-y", "@anthropics/mcp-server-brave-search"],
    "env": {
      "BRAVE_API_KEY": "${BRAVE_API_KEY}"
    }
  }
}
```

- **Auth**: API Key (free at https://brave.com/search/api/)
- **Setup**: [templates/mcp/brave-search/setup-guide.md](../templates/mcp/brave-search/setup-guide.md)

#### Sequential Thinking

Structured problem-solving through reasoning sequences.

```json
{
  "sequentialthinking": {
    "url": "https://remote.mcpservers.org/sequentialthinking/mcp"
  }
}
```

- **Auth**: None (remote server)

---

### Category 2: Code, Testing, Version Control

#### GitHub

Full GitHub integration - repos, PRs, issues, Actions.

```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_TOKEN": "${GITHUB_TOKEN}"
    }
  }
}
```

- **Auth**: Personal Access Token
- **Setup**: [templates/mcp/github/setup-guide.md](../templates/mcp/github/setup-guide.md)

#### Sentry

Error tracking and performance monitoring.

```json
{
  "sentry": {
    "command": "npx",
    "args": ["-y", "@sentry/mcp-server"],
    "env": {
      "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}"
    }
  }
}
```

- **Auth**: API Token
- **Docs**: https://github.com/getsentry/sentry-mcp-server

#### Playwright

Browser automation for testing and scraping.

```json
{
  "playwright": {
    "command": "npx",
    "args": ["-y", "@playwright/mcp@latest"]
  }
}
```

- **Auth**: None
- **Docs**: https://playwright.dev/agents

---

### Category 3: Data and Databases

#### PostgreSQL

SQL database operations.

```json
{
  "postgresql": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres"],
    "env": {
      "DATABASE_URL": "${DATABASE_URL}"
    }
  }
}
```

- **Auth**: Connection string
- **Docs**: https://github.com/modelcontextprotocol/servers

#### MongoDB

Document database and Atlas management.

```json
{
  "mongodb": {
    "command": "npx",
    "args": ["-y", "@mongodb/mcp-server"],
    "env": {
      "MONGODB_URI": "${MONGODB_URI}"
    }
  }
}
```

- **Auth**: Connection string or API key
- **Docs**: https://www.mongodb.com/docs/mcp-server/

#### Pinecone

Managed vector database for RAG.

```json
{
  "pinecone": {
    "command": "npx",
    "args": ["-y", "@pinecone/mcp-server"],
    "env": {
      "PINECONE_API_KEY": "${PINECONE_API_KEY}"
    }
  }
}
```

- **Auth**: API Key
- **Docs**: https://docs.pinecone.io/guides/operations/mcp-server

#### ChromaDB

Local embedding database.

```json
{
  "chromadb": {
    "command": "npx",
    "args": ["-y", "chroma-mcp-server"]
  }
}
```

- **Auth**: None
- **Docs**: https://github.com/chroma-core/chroma-mcp

---

### Category 4: Cloud and DevOps

#### Docker

Container management.

```json
{
  "docker": {
    "command": "npx",
    "args": ["-y", "@docker/mcp-server"]
  }
}
```

- **Auth**: None (requires Docker running)
- **Docs**: https://github.com/docker/mcp-servers

#### AWS Terraform

Infrastructure as Code with security scanning.

```json
{
  "terraform": {
    "command": "uvx",
    "args": ["awslabs.terraform-mcp-server"],
    "env": {
      "AWS_REGION": "${AWS_REGION:-us-east-1}"
    }
  }
}
```

- **Auth**: AWS credentials
- **Docs**: https://awslabs.github.io/mcp/servers/terraform-mcp-server

---

### Category 5: Collaboration

#### Atlassian (Jira/Confluence)

```json
{
  "atlassian": {
    "url": "https://mcp.atlassian.com/v1/sse"
  }
}
```

- **Auth**: OAuth (browser popup)
- **Docs**: https://mcp.atlassian.com

#### Slack

```json
{
  "slack": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-slack"],
    "env": {
      "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}"
    }
  }
}
```

- **Auth**: Bot token
- **Docs**: https://docs.slack.dev/ai/mcp-server/

#### Notion

```json
{
  "notion": {
    "url": "https://mcp.notion.so/mcp"
  }
}
```

- **Auth**: OAuth
- **Docs**: https://mcp.notion.so

---

### Category 6: AI/ML and Agent Development

#### Hugging Face

Models, datasets, and Spaces.

```json
{
  "huggingface": {
    "url": "https://huggingface.co/mcp",
    "env": {
      "HF_TOKEN": "${HF_TOKEN}"
    }
  }
}
```

- **Auth**: API token
- **Docs**: https://huggingface.co/docs/hub/en/hf-mcp-server

#### MLflow

Experiment tracking and model registry.

```json
{
  "mlflow": {
    "command": "mlflow-mcp-server",
    "env": {
      "MLFLOW_TRACKING_URI": "${MLFLOW_TRACKING_URI}"
    }
  }
}
```

- **Auth**: Tracking server credentials
- **Docs**: https://mlflow.org/docs/latest/genai/mcp/

#### LangGraph Platform

Agent orchestration.

```json
{
  "langgraph": {
    "url": "https://your-deployment.langchain.app/mcp",
    "env": {
      "LANGCHAIN_API_KEY": "${LANGCHAIN_API_KEY}"
    }
  }
}
```

- **Auth**: API key
- **Docs**: https://docs.langchain.com/langgraph-platform/server-mcp

#### Ollama

Local LLM serving.

```json
{
  "ollama": {
    "command": "npx",
    "args": ["-y", "ollama-mcp"],
    "env": {
      "OLLAMA_HOST": "${OLLAMA_HOST:-http://localhost:11434}"
    }
  }
}
```

- **Auth**: None (requires Ollama running)
- **Docs**: https://github.com/nighttrek/ollama-mcp

---

## Authentication Guide

### No Authentication Required

These servers work out of the box:
- filesystem, git, memory, time, fetch
- sequentialthinking, playwright, puppeteer
- docker, chromadb, sqlite

### API Key Authentication

1. Sign up for the service
2. Generate an API key
3. Set as environment variable
4. Add to MCP config

Example services: Brave Search, Sentry, Pinecone, Hugging Face, MLflow, W&B

### OAuth Authentication

1. Add server URL to MCP config
2. Restart Cursor
3. Complete OAuth flow in browser when prompted

Example services: Atlassian, Linear, Notion, Figma, Google services

### Personal Access Token (PAT)

1. Go to service settings
2. Generate PAT with required scopes
3. Set as environment variable

Example services: GitHub, GitLab

---

## Custom/Local Servers

### Adding a Custom Server

```json
{
  "mcpServers": {
    "my-custom-server": {
      "command": "python",
      "args": ["-m", "my_mcp_server"],
      "env": {
        "MY_API_KEY": "${MY_API_KEY}"
      }
    }
  }
}
```

### Building Custom Servers

See the MCP SDK documentation:
- Python: https://github.com/modelcontextprotocol/python-sdk
- TypeScript: https://github.com/modelcontextprotocol/typescript-sdk

---

## Troubleshooting

### Server Not Responding

1. Check if command exists: `npx --version`, `node --version`
2. Verify environment variables are set
3. Check Cursor logs for errors
4. Restart Cursor

### Authentication Failed

1. Verify API key/token is correct
2. Check token hasn't expired
3. Ensure required scopes are granted
4. Check rate limits

### Permission Denied

1. Verify file/directory permissions
2. Check network access for remote servers
3. Ensure Docker/services are running

---

## Resources

- **Official MCP Servers**: https://github.com/modelcontextprotocol/servers
- **MCP Documentation**: https://modelcontextprotocol.io
- **Community Servers**: https://mcpservers.org
- **Docker MCP Catalog**: https://hub.docker.com/mcp

---

## AISuite Integration

For multi-provider LLM access with MCP support, see:
- [knowledge/aisuite-integration.json](../knowledge/aisuite-integration.json)
- GitHub: https://github.com/andrewyng/aisuite
