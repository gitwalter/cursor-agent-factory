# Multi-Backend Setup Guide

This guide walks you through setting up multiple PM backends simultaneously for the Cursor Agent Factory PM system. Combining backends allows you to leverage the strengths of different tools in your workflow.

## Overview

Multi-backend configuration enables you to use multiple PM systems together, such as:
- **Jira + Confluence + GitHub**: Enterprise setup with code integration
- **GitHub + Linear**: Modern development workflow
- **Azure DevOps + GitHub**: Microsoft ecosystem integration
- **Custom combinations**: Mix and match based on your needs

## Common Use Cases

### Enterprise Setup: Jira + Confluence + GitHub

**Best for**: Large teams needing formal processes with code integration

**Benefits**:
- Jira for issue tracking and sprint management
- Confluence for documentation and requirements
- GitHub for code repositories and PR tracking
- Bi-directional linking between all three

**Workflow**:
1. Create Epic in Jira
2. Link requirements page in Confluence
3. Create GitHub issues from Jira stories
4. Link PRs back to Jira issues
5. Update Confluence with architecture decisions

### Modern Development: GitHub + Linear

**Best for**: Software teams wanting speed and simplicity

**Benefits**:
- Linear for fast issue tracking
- GitHub for code and PRs
- Simple integration between tools

**Workflow**:
1. Create issue in Linear
2. Link to GitHub PR
3. Auto-update Linear when PR merges
4. Track cycle progress in Linear

### Microsoft Ecosystem: Azure DevOps + GitHub

**Best for**: Teams using Microsoft tools

**Benefits**:
- Azure DevOps for work tracking
- GitHub for code (or Azure Repos)
- Full ALM integration

**Workflow**:
1. Create work item in Azure DevOps
2. Link to GitHub PR
3. Track sprint progress in Azure Boards
4. Use Azure Pipelines for CI/CD

## Prerequisites

Before setting up multiple backends, ensure you have:

- **Accounts**: Active accounts for all backends you want to use
- **API Tokens**: Tokens/keys for each backend
- **Node.js 18+**: Required for MCP servers
- **Cursor IDE**: Installed and configured

## Step 1: Gather All Required Credentials

Collect credentials for each backend you want to use:

### GitHub
- Personal Access Token (PAT)
- See [GitHub Setup Guide](./GITHUB_SETUP.md) for details

### Atlassian (Jira/Confluence)
- API Token
- Domain name
- Email address
- See [Jira Setup Guide](./JIRA_SETUP.md) and [Confluence Setup Guide](./CONFLUENCE_SETUP.md) for details

### Azure DevOps
- Personal Access Token (PAT)
- Organization name
- Project name
- See [Azure DevOps Setup Guide](./AZURE_DEVOPS_SETUP.md) for details

### Linear
- API Key
- See [Linear Setup Guide](./LINEAR_SETUP.md) for details

## Step 2: Configure Environment Variables

Create a comprehensive `.env` file with all your credentials:

```bash
# GitHub
GITHUB_TOKEN=ghp_your_github_token_here

# Atlassian (Jira/Confluence)
ATLASSIAN_DOMAIN=mycompany
ATLASSIAN_EMAIL=your.email@example.com
ATLASSIAN_API_TOKEN=your_atlassian_token_here

# Azure DevOps
AZURE_DEVOPS_PAT=your_azure_devops_pat_here
AZURE_DEVOPS_ORG=yourorganization
AZURE_DEVOPS_PROJECT=yourproject

# Linear
LINEAR_API_KEY=lin_api_your_linear_key_here
```

**Security Note**: Never commit this file to version control. Add `.env` to your `.gitignore`.

## Step 3: Configure Combined MCP Settings

### 3.1 Locate MCP Configuration File

The MCP configuration file location depends on your operating system:

- **Windows**: `%APPDATA%\Cursor\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`
- **macOS**: `~/Library/Application Support/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
- **Linux**: `~/.config/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

### 3.2 Edit MCP Configuration

1. Open Cursor Settings (Ctrl+, or Cmd+,)
2. Navigate to **Features** > **Model Context Protocol**
3. Click **Edit Config** or manually open the file location above
4. Add all MCP servers you want to use:

#### Example: Jira + Confluence + GitHub

```json
{
  "mcpServers": {
    "github-pm": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "atlassian-cloud": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-atlassian"],
      "env": {
        "ATLASSIAN_API_TOKEN": "${ATLASSIAN_API_TOKEN}",
        "ATLASSIAN_DOMAIN": "${ATLASSIAN_DOMAIN}",
        "ATLASSIAN_EMAIL": "${ATLASSIAN_EMAIL}"
      }
    }
  }
}
```

#### Example: GitHub + Linear

```json
{
  "mcpServers": {
    "github-pm": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "linear": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-linear"],
      "env": {
        "LINEAR_API_KEY": "${LINEAR_API_KEY}"
      }
    }
  }
}
```

#### Example: Azure DevOps + GitHub

```json
{
  "mcpServers": {
    "github-pm": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "azure-devops": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-azure-devops"],
      "env": {
        "AZURE_DEVOPS_PAT": "${AZURE_DEVOPS_PAT}",
        "AZURE_DEVOPS_ORG": "${AZURE_DEVOPS_ORG}",
        "AZURE_DEVOPS_PROJECT": "${AZURE_DEVOPS_PROJECT}"
      }
    }
  }
}
```

#### Example: Full Stack (All Backends)

```json
{
  "mcpServers": {
    "github-pm": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "atlassian-cloud": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-atlassian"],
      "env": {
        "ATLASSIAN_API_TOKEN": "${ATLASSIAN_API_TOKEN}",
        "ATLASSIAN_DOMAIN": "${ATLASSIAN_DOMAIN}",
        "ATLASSIAN_EMAIL": "${ATLASSIAN_EMAIL}"
      }
    },
    "azure-devops": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-azure-devops"],
      "env": {
        "AZURE_DEVOPS_PAT": "${AZURE_DEVOPS_PAT}",
        "AZURE_DEVOPS_ORG": "${AZURE_DEVOPS_ORG}",
        "AZURE_DEVOPS_PROJECT": "${AZURE_DEVOPS_PROJECT}"
      }
    },
    "linear": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-linear"],
      "env": {
        "LINEAR_API_KEY": "${LINEAR_API_KEY}"
      }
    }
  }
}
```

## Step 4: Verify Installation

### 4.1 Restart Cursor

1. Close Cursor completely
2. Reopen Cursor
3. All configured MCP servers should start automatically

### 4.2 Verify MCP Server Status

1. Open the MCP panel in Cursor
2. All configured servers should appear as connected
3. Look for any error messages in the MCP logs

### 4.3 Test Each Backend

Test each backend individually:

- **GitHub**: List repositories, query issues
- **Jira**: List projects, query issues
- **Confluence**: List spaces, query pages
- **Azure DevOps**: List projects, query work items
- **Linear**: List teams, query issues

If all commands work, your multi-backend setup is successful!

## Step 5: Configure PM System Integration

After all backends are set up, configure the PM system to use multiple backends:

```json
{
  "pm": {
    "enabled": true,
    "backends": [
      {
        "type": "jira",
        "projectId": "PROJ",
        "workspace": "mycompany.atlassian.net",
        "primary": true
      },
      {
        "type": "confluence",
        "spaceKey": "PM",
        "workspace": "mycompany.atlassian.net"
      },
      {
        "type": "github",
        "projectId": "my-org/my-repo",
        "workspace": "my-github-username"
      }
    ]
  }
}
```

## Step 6: Data Flow Between Backends

### 6.1 Bi-Directional Linking

Configure how data flows between backends:

**Jira ↔ GitHub**:
- Create GitHub issue from Jira story
- Link PR to Jira issue
- Auto-close Jira issue when PR merges

**Jira ↔ Confluence**:
- Link Confluence page to Jira Epic
- Embed Jira board in Confluence page
- Update Confluence when Jira issue changes

**GitHub ↔ Linear**:
- Create Linear issue from GitHub issue
- Link PR to Linear issue
- Update Linear when PR merges

### 6.2 Synchronization Rules

Define synchronization rules:

```json
{
  "pm": {
    "sync": {
      "jira-github": {
        "enabled": true,
        "direction": "bidirectional",
        "rules": [
          {
            "trigger": "jira.issue.created",
            "action": "github.issue.create",
            "mapping": {
              "title": "summary",
              "body": "description",
              "labels": "labels"
            }
          }
        ]
      }
    }
  }
}
```

## Best Practices

### Security

1. **Separate Credentials**: Use different tokens for different backends
2. **Minimal Permissions**: Grant only necessary permissions to each token
3. **Token Rotation**: Rotate tokens regularly
4. **Secure Storage**: Store credentials securely
5. **Environment Variables**: Use environment variables, not hardcoded values

### Organization

1. **Primary Backend**: Designate one backend as primary for issue creation
2. **Consistent Naming**: Use consistent naming conventions across backends
3. **Label Strategy**: Align labels/tags across backends
4. **Documentation**: Document your multi-backend setup
5. **Team Alignment**: Ensure team understands which backend to use for what

### Performance

1. **Selective Sync**: Only sync what you need
2. **Batch Operations**: Group API calls when possible
3. **Caching**: Cache frequently accessed data
4. **Webhooks**: Use webhooks instead of polling
5. **Rate Limiting**: Monitor and respect API rate limits

### Data Consistency

1. **Single Source of Truth**: Define which backend is authoritative for each data type
2. **Conflict Resolution**: Define how to handle conflicts
3. **Validation**: Validate data before syncing
4. **Error Handling**: Handle sync errors gracefully
5. **Audit Trail**: Log sync operations for debugging

## Troubleshooting

### Individual Server Issues

If one server fails to connect:

1. Check that server's specific configuration
2. Verify its credentials are correct
3. Review that server's setup guide for troubleshooting
4. Check Cursor's MCP logs for specific error messages
5. Test that server independently

### Environment Variable Issues

- Ensure all variables are set in your `.env` file
- Verify variable names match exactly (case-sensitive)
- Check that your `.env` file is in the correct location
- Some systems may require restarting Cursor after changing `.env`

### Performance Considerations

- Running multiple MCP servers may increase resource usage
- Each server runs as a separate process
- Monitor system resources if experiencing slowdowns
- Consider disabling unused servers to improve performance

### Conflicting Server Names

If you need multiple instances of the same service (e.g., two GitHub accounts):

1. Use unique server names:

```json
{
  "mcpServers": {
    "github-personal": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_TOKEN}"
      }
    },
    "github-work": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_WORK_TOKEN}"
      }
    }
  }
}
```

2. Use different environment variables for each instance

### Sync Conflicts

If data conflicts occur between backends:

1. Define conflict resolution strategy
2. Use timestamps to determine latest data
3. Prefer primary backend in conflicts
4. Log conflicts for review
5. Notify team of conflicts

## Common Combinations

### Jira + Confluence + GitHub

**Configuration**:
- Jira: Primary issue tracking
- Confluence: Documentation and requirements
- GitHub: Code repositories and PRs

**Workflow**:
1. Create Epic in Jira
2. Create requirements page in Confluence
3. Create stories in Jira
4. Create GitHub issues from Jira stories
5. Link PRs to Jira issues
6. Update Confluence with decisions

### GitHub + Linear

**Configuration**:
- Linear: Primary issue tracking
- GitHub: Code repositories

**Workflow**:
1. Create issue in Linear
2. Create PR in GitHub
3. Link PR to Linear issue
4. Auto-update Linear when PR merges

### Azure DevOps + GitHub

**Configuration**:
- Azure DevOps: Work tracking and boards
- GitHub: Code repositories

**Workflow**:
1. Create work item in Azure DevOps
2. Create PR in GitHub
3. Link PR to work item
4. Track sprint progress in Azure Boards

## Next Steps

After completing multi-backend setup:

1. **Configure Workflows**: Set up workflows that span multiple backends
2. **Set Up Sync Rules**: Define how data flows between backends
3. **Team Onboarding**: Share setup instructions with your team
4. **Test Integration**: Create test items and verify end-to-end flow
5. **Monitor Performance**: Watch for performance issues and optimize

## Additional Resources

- Individual backend setup guides:
  - [GitHub Setup Guide](./GITHUB_SETUP.md)
  - [Jira Setup Guide](./JIRA_SETUP.md)
  - [Confluence Setup Guide](./CONFLUENCE_SETUP.md)
  - [Azure DevOps Setup Guide](./AZURE_DEVOPS_SETUP.md)
  - [Linear Setup Guide](./LINEAR_SETUP.md)
- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Cursor MCP Documentation](https://cursor.sh/docs/mcp)
- [PM System User Guide](../USER_GUIDE.md)

## Support

If you encounter issues not covered in this guide:

1. Check individual backend setup guides
2. Review [Troubleshooting](#troubleshooting) section above
3. Check Cursor MCP logs for detailed error messages
4. Test each backend independently to isolate issues
