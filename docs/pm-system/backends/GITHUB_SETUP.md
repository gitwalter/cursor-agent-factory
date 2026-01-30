# GitHub Setup Guide

This guide walks you through setting up GitHub as your PM backend for the Cursor Agent Factory PM system. GitHub provides issue tracking, project boards, and milestone management integrated with your code repositories.

## Prerequisites

- **GitHub Account**: A GitHub account (free or paid)
- **Personal Access Token (PAT)**: Required for API access
- **Node.js 18+**: Required for the MCP server
- **Cursor IDE**: Installed and configured

## Step 1: Create a GitHub Personal Access Token (PAT)

### 1.1 Navigate to GitHub Settings

1. Log in to GitHub
2. Click your profile picture in the top right
3. Select **Settings**
4. Scroll down to **Developer settings** in the left sidebar
5. Click **Personal access tokens** > **Tokens (classic)**

### 1.2 Generate New Token

1. Click **Generate new token** > **Generate new token (classic)**
2. Give your token a descriptive name: `Cursor MCP GitHub PM`
3. Set expiration: Choose an appropriate expiration (90 days, 1 year, or no expiration)
4. Select required scopes:
   - ✅ **repo** - Full control of private repositories
     - ✅ **repo:status** - Access commit status
     - ✅ **repo_deployment** - Access deployment status
     - ✅ **public_repo** - Access public repositories
   - ✅ **project** - Full control of organization projects
   - ✅ **workflow** - Update GitHub Action workflows
   - ✅ **read:org** - Read org and team membership (if using organization projects)
5. Click **Generate token**
6. **Copy the token immediately** - you won't be able to see it again!

### 1.3 Store Token Securely

Save your token in a secure location. You'll need it for the next steps.

## Step 2: Install GitHub MCP Server

The GitHub MCP server is installed via npm/npx. No manual installation is required - it will be downloaded automatically when Cursor starts the MCP server.

### Verify Node.js Installation

```powershell
# Check Node.js version (should be 18+)
node --version

# Check npm version
npm --version

# Verify npx is available
npx --version
```

If Node.js is not installed, download it from [nodejs.org](https://nodejs.org/).

## Step 3: Configure Environment Variables

Create or update your `.env` file in your project root:

```bash
# GitHub Personal Access Token
GITHUB_TOKEN=ghp_your_token_here
```

**Security Note**: 
- Never commit `.env` files to version control
- Add `.env` to your `.gitignore`
- Use environment variables or secure credential storage in production

## Step 4: Configure Cursor MCP Settings

### 4.1 Locate MCP Configuration File

The MCP configuration file location depends on your operating system:

- **Windows**: `%APPDATA%\Cursor\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`
- **macOS**: `~/Library/Application Support/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
- **Linux**: `~/.config/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

### 4.2 Edit MCP Configuration

1. Open Cursor Settings (Ctrl+, or Cmd+,)
2. Navigate to **Features** > **Model Context Protocol**
3. Click **Edit Config** or manually open the file location above
4. Add or update the GitHub MCP server configuration:

```json
{
  "mcpServers": {
    "github-pm": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Note**: Replace `${GITHUB_TOKEN}` with your actual token, or ensure the `GITHUB_TOKEN` environment variable is set in your system.

### 4.3 Alternative: Direct Token Configuration

If you prefer to set the token directly (not recommended for shared configs):

```json
{
  "mcpServers": {
    "github-pm": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_actual_token_here"
      }
    }
  }
}
```

## Step 5: Test the Connection

### 5.1 Restart Cursor

1. Close Cursor completely
2. Reopen Cursor
3. The MCP server should start automatically

### 5.2 Verify MCP Server Status

1. Open the MCP panel in Cursor (if available)
2. Check that `github-pm` appears as connected
3. Look for any error messages in the MCP logs

### 5.3 Test GitHub Integration

Try using GitHub-related commands in Cursor:

- List repositories
- Query issues
- Create a test issue
- Access project boards

If commands work, your connection is successful!

## Step 6: GitHub Projects v2 Setup

GitHub Projects v2 provides enhanced project management capabilities.

### 6.1 Enable Projects v2

1. Navigate to your repository on GitHub
2. Click the **Projects** tab
3. If you see "New project", click it to create a Projects v2 board
4. If Projects v2 is not available, ensure your account/organization has access

### 6.2 Configure Project Board

1. Create a new project or select an existing one
2. Configure columns based on your methodology:
   - **Scrum**: Backlog → To Do → In Progress → Review → Done
   - **Kanban**: Backlog → Ready → In Progress → Testing → Done
3. Set up automation rules (optional):
   - Auto-move issues when status changes
   - Auto-assign labels
   - Link PRs to issues

### 6.3 Link Repository to Project

1. In your project board, click **Add** > **Repository**
2. Select your repository
3. Issues and PRs from the repository will appear in the project

### 6.4 Configure Milestones

For sprint-based methodologies:

1. Go to your repository
2. Click **Milestones** under **Issues**
3. Create milestones for sprints (e.g., "Sprint 1", "Sprint 2")
4. Link issues to milestones

## Step 7: Configure PM System Integration

After GitHub is set up, configure the PM system to use GitHub:

```json
{
  "pm": {
    "enabled": true,
    "backend": {
      "type": "github",
      "projectId": "your-org/your-repo",
      "workspace": "your-github-username"
    }
  }
}
```

## Troubleshooting

### MCP Server Not Connecting

**Problem**: GitHub MCP server doesn't appear in Cursor

**Solutions**:
1. Verify Node.js is installed: `node --version` (should be 18+)
2. Check that `npx` is available: `npx --version`
3. Verify your token is correct and has required scopes
4. Check Cursor MCP logs for error messages
5. Ensure the MCP config file path is correct
6. Restart Cursor completely

### Authentication Errors

**Problem**: "Bad credentials" or "401 Unauthorized" errors

**Solutions**:
1. Verify your PAT is correct (no extra spaces or characters)
2. Check token expiration - generate a new token if expired
3. Ensure token has required scopes (repo, project, workflow)
4. Verify environment variable is set correctly
5. Try using the token directly in config (temporarily) to test

### Permission Errors

**Problem**: "403 Forbidden" or "Resource not accessible" errors

**Solutions**:
1. Verify token has `repo` scope for private repositories
2. Check organization permissions if using org projects
3. Ensure token has `project` scope for project boards
4. Verify you have access to the repository/project

### Projects v2 Not Available

**Problem**: Can't create or access Projects v2

**Solutions**:
1. Projects v2 may require GitHub Pro/Team/Enterprise
2. Check your GitHub plan and upgrade if needed
3. For organizations, ensure Projects v2 is enabled
4. Try using classic Projects as a fallback

### Environment Variable Not Found

**Problem**: `${GITHUB_TOKEN}` not resolving

**Solutions**:
1. Set environment variable in your system:
   - **Windows**: `$env:GITHUB_TOKEN = "your_token"`
   - **macOS/Linux**: `export GITHUB_TOKEN="your_token"`
2. Or use the token directly in config (less secure)
3. Ensure `.env` file is in the correct location
4. Restart Cursor after setting environment variables

### Rate Limiting

**Problem**: "API rate limit exceeded" errors

**Solutions**:
1. GitHub API has rate limits (5,000 requests/hour for authenticated users)
2. Implement request caching if making many calls
3. Use webhooks instead of polling when possible
4. Consider using a GitHub App instead of PAT for higher limits

## Best Practices

### Security

1. **Use Environment Variables**: Never hardcode tokens in config files
2. **Token Rotation**: Rotate tokens regularly (every 90 days recommended)
3. **Minimal Scopes**: Only grant necessary scopes to your token
4. **Separate Tokens**: Use different tokens for different purposes
5. **Secure Storage**: Store tokens in secure credential managers

### Organization

1. **Project Structure**: Organize projects by team/product/initiative
2. **Label Strategy**: Use consistent labels across repositories
3. **Milestone Planning**: Create milestones aligned with sprints/releases
4. **Template Issues**: Use issue templates for consistency
5. **Automation**: Leverage GitHub Actions for workflow automation

### Performance

1. **Batch Operations**: Group API calls when possible
2. **Webhooks**: Use webhooks instead of polling for real-time updates
3. **Caching**: Cache frequently accessed data
4. **Rate Limiting**: Monitor and respect API rate limits

## Next Steps

After completing GitHub setup:

1. **Configure Methodology**: Set up your development methodology (Scrum, Kanban, etc.)
2. **Create Workflows**: Configure workflows that integrate with GitHub
3. **Set Up Metrics**: Enable metrics tracking for your PM system
4. **Team Onboarding**: Share setup instructions with your team
5. **Test Integration**: Create test issues and verify end-to-end flow

## Additional Resources

- [GitHub API Documentation](https://docs.github.com/en/rest)
- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GitHub Personal Access Tokens Guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Cursor MCP Documentation](https://cursor.sh/docs/mcp)

## Support

If you encounter issues not covered in this guide:

1. Check the [PM System User Guide](../USER_GUIDE.md)
2. Review [Troubleshooting](#troubleshooting) section above
3. Check Cursor MCP logs for detailed error messages
4. Verify your GitHub account permissions and token scopes
