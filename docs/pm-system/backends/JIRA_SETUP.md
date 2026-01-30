# Jira Setup Guide

This guide walks you through setting up Jira as your PM backend for the Cursor Agent Factory PM system. Jira provides enterprise-grade issue tracking, sprint management, and customizable workflows.

## Prerequisites

- **Atlassian Cloud Account**: A Jira Cloud account (free tier available)
- **API Token**: Required for API access
- **Node.js 18+**: Required for the MCP server (Option 1)
- **Python 3.8+**: Required for local MCP server (Option 2)
- **Cursor IDE**: Installed and configured

## Step 1: Create an Atlassian API Token

### 1.1 Navigate to Atlassian Account Settings

1. Log in to your Atlassian account at [id.atlassian.com](https://id.atlassian.com)
2. Click your profile picture in the top right
3. Select **Account settings**
4. Scroll down to **Security** section
5. Click **API tokens**

### 1.2 Generate API Token

1. Click **Create API token**
2. Give your token a label: `Cursor MCP Jira`
3. Click **Create**
4. **Copy the token immediately** - you won't be able to see it again!

### 1.3 Note Your Account Details

You'll need:
- **Email**: Your Atlassian account email
- **Domain**: Your Jira instance domain (e.g., `mycompany.atlassian.net`)

## Step 2: Choose Installation Method

You have two options for the Atlassian MCP server:

### Option 1: Remote Atlassian MCP (Rovo) - OAuth Setup

**Recommended for**: Cloud users who want OAuth-based authentication

**Pros**:
- OAuth-based authentication (more secure)
- Managed service (no local installation)
- Automatic updates

**Cons**:
- Requires OAuth application setup
- May have rate limits

### Option 2: Local mcp-atlassian - pip install

**Recommended for**: Users who want local control or have specific requirements

**Pros**:
- Full control over installation
- No external dependencies
- Can customize configuration

**Cons**:
- Requires local Python environment
- Manual updates needed

## Option 1: Remote Atlassian MCP (Rovo) Setup

### Step 1.1: Create OAuth Application

1. Log in to your Atlassian account
2. Go to [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/)
3. Click **Create** > **New app**
4. Choose **OAuth 2.0 (3LO)**
5. Fill in application details:
   - **App name**: `Cursor MCP Jira Integration`
   - **App logo**: (optional)
   - **App description**: `MCP server integration for Cursor IDE`
6. Click **Create**

### Step 1.2: Configure OAuth Scopes

1. In your app settings, go to **Permissions**
2. Add the following scopes:
   - ✅ **Read Jira issue data**
   - ✅ **Write Jira issue data**
   - ✅ **Read Jira project data**
   - ✅ **Read Jira board data**
   - ✅ **Read Jira sprint data**
   - ✅ **Write Jira sprint data**
3. Click **Save changes**

### Step 1.3: Configure Authorization

1. Go to **Authorization** in your app settings
2. Add callback URL: `http://localhost:3000/callback` (or your preferred callback)
3. Note your **Client ID** and **Client Secret**

### Step 1.4: Configure Cursor MCP Settings

Add the remote MCP server configuration:

```json
{
  "mcpServers": {
    "atlassian-cloud": {
      "url": "https://mcp.rovo.app/atlassian",
      "headers": {
        "Authorization": "Bearer ${ATLASSIAN_OAUTH_TOKEN}"
      },
      "env": {
        "ATLASSIAN_CLIENT_ID": "${ATLASSIAN_CLIENT_ID}",
        "ATLASSIAN_CLIENT_SECRET": "${ATLASSIAN_CLIENT_SECRET}",
        "ATLASSIAN_DOMAIN": "${ATLASSIAN_DOMAIN}"
      }
    }
  }
}
```

### Step 1.5: Complete OAuth Flow

1. The MCP server will initiate OAuth flow when first used
2. You'll be redirected to Atlassian to authorize the application
3. After authorization, the access token will be stored
4. Subsequent requests will use the stored token

## Option 2: Local mcp-atlassian Setup

### Step 2.1: Install Python (if not installed)

```powershell
# Check Python version (should be 3.8+)
python --version

# If not installed, download from python.org
```

### Step 2.2: Install mcp-atlassian

```powershell
# Install via pip
pip install mcp-atlassian

# Or install from source
pip install git+https://github.com/modelcontextprotocol/servers.git#subdirectory=atlassian
```

### Step 2.3: Verify Installation

```powershell
# Check if mcp-atlassian is installed
pip show mcp-atlassian

# Test import (optional)
python -c "import mcp_atlassian; print('Installation successful')"
```

### Step 2.4: Configure Environment Variables

Create or update your `.env` file:

```bash
# Atlassian API Token
ATLASSIAN_API_TOKEN=your_api_token_here

# Atlassian Domain (without https://)
ATLASSIAN_DOMAIN=mycompany.atlassian.net

# Atlassian Email
ATLASSIAN_EMAIL=your.email@example.com

# Optional: Base URL (if using self-hosted Jira)
ATLASSIAN_BASE_URL=https://mycompany.atlassian.net
```

### Step 2.5: Configure Cursor MCP Settings

Locate your MCP config file (see [GitHub Setup Guide](./GITHUB_SETUP.md#41-locate-mcp-configuration-file) for paths).

Add the local MCP server configuration:

```json
{
  "mcpServers": {
    "atlassian-local": {
      "command": "python",
      "args": ["-m", "mcp_atlassian"],
      "env": {
        "ATLASSIAN_API_TOKEN": "${ATLASSIAN_API_TOKEN}",
        "ATLASSIAN_DOMAIN": "${ATLASSIAN_DOMAIN}",
        "ATLASSIAN_EMAIL": "${ATLASSIAN_EMAIL}",
        "ATLASSIAN_BASE_URL": "${ATLASSIAN_BASE_URL}"
      }
    }
  }
}
```

**Alternative**: If installed globally and available as a command:

```json
{
  "mcpServers": {
    "atlassian-local": {
      "command": "mcp-atlassian",
      "env": {
        "ATLASSIAN_API_TOKEN": "${ATLASSIAN_API_TOKEN}",
        "ATLASSIAN_DOMAIN": "${ATLASSIAN_DOMAIN}",
        "ATLASSIAN_EMAIL": "${ATLASSIAN_EMAIL}"
      }
    }
  }
}
```

## Step 3: Test the Connection

### 3.1 Restart Cursor

1. Close Cursor completely
2. Reopen Cursor
3. The MCP server should start automatically

### 3.2 Verify MCP Server Status

1. Open the MCP panel in Cursor
2. Check that `atlassian-cloud` or `atlassian-local` appears as connected
3. Look for any error messages in the MCP logs

### 3.3 Test Jira Integration

Try using Jira-related commands in Cursor:

- List projects
- Query issues
- Create a test issue
- Access sprint boards

If commands work, your connection is successful!

## Step 4: Project Configuration

### 4.1 Configure Issue Types

Ensure your Jira project has the required issue types:

1. Go to your Jira project
2. Navigate to **Project settings** > **Issue types**
3. Ensure you have:
   - **Epic** (for epic-level tracking)
   - **Story** (for user stories)
   - **Task** (for tasks)
   - **Bug** (for bug tracking)
   - **Subtask** (for subtasks)

### 4.2 Configure Workflows

Set up workflows based on your methodology:

**For Scrum**:
- Backlog → To Do → In Progress → In Review → Done

**For Kanban**:
- Backlog → Ready → In Progress → Testing → Done

1. Go to **Project settings** > **Workflows**
2. Create or customize workflows
3. Add transitions and statuses
4. Configure automation rules (optional)

### 4.3 Set Up Custom Fields

Configure custom fields for your PM system:

1. Go to **Project settings** > **Fields**
2. Add custom fields as needed:
   - Story Points (for estimation)
   - Sprint (for sprint assignment)
   - Epic Link (for epic relationships)
3. Configure field configurations

### 4.4 Configure Boards

Create boards for your team:

1. Go to **Boards** > **Create board**
2. Choose board type:
   - **Scrum board** (for sprint-based work)
   - **Kanban board** (for continuous flow)
3. Configure columns and swimlanes
4. Set up filters and quick filters

## Step 5: Configure PM System Integration

After Jira is set up, configure the PM system:

```json
{
  "pm": {
    "enabled": true,
    "backend": {
      "type": "jira",
      "projectId": "PROJ",
      "workspace": "mycompany.atlassian.net"
    }
  }
}
```

## Troubleshooting

### MCP Server Not Connecting

**Problem**: Atlassian MCP server doesn't appear in Cursor

**Solutions**:
1. **For Option 1 (Remote)**:
   - Verify OAuth application is configured correctly
   - Check that callback URL matches
   - Verify Client ID and Secret are correct
   - Complete OAuth flow again

2. **For Option 2 (Local)**:
   - Verify Python is installed: `python --version` (should be 3.8+)
   - Check mcp-atlassian is installed: `pip show mcp-atlassian`
   - Verify environment variables are set correctly
   - Check Cursor MCP logs for Python errors

### Authentication Errors

**Problem**: "401 Unauthorized" or "403 Forbidden" errors

**Solutions**:
1. Verify API token is correct (no extra spaces)
2. Check token hasn't expired
3. Verify email matches your Atlassian account
4. Ensure domain is correct (without `https://`)
5. For OAuth: Complete authorization flow again

### Permission Errors

**Problem**: "You do not have permission" errors

**Solutions**:
1. Verify you have access to the Jira project
2. Check project permissions in Jira
3. Ensure your account has required roles
4. Verify API token has necessary scopes

### Issue Types Not Found

**Problem**: "Issue type not found" errors

**Solutions**:
1. Verify issue types exist in your project
2. Check issue type scheme configuration
3. Ensure Epic issue type is enabled
4. Verify custom issue types are configured

### Workflow Errors

**Problem**: "Invalid transition" or workflow errors

**Solutions**:
1. Verify workflow is configured correctly
2. Check transition permissions
3. Ensure status exists in workflow
4. Verify workflow scheme is assigned to project

### Domain Configuration Issues

**Problem**: "Invalid domain" or connection errors

**Solutions**:
1. Verify domain format: `mycompany.atlassian.net` (no `https://`)
2. Check domain is accessible
3. For self-hosted: Verify `ATLASSIAN_BASE_URL` is set correctly
4. Test domain in browser to ensure it's accessible

## Best Practices

### Security

1. **Use API Tokens**: Prefer API tokens over passwords
2. **Token Rotation**: Rotate tokens regularly
3. **Minimal Permissions**: Grant only necessary permissions
4. **Secure Storage**: Store credentials securely
5. **OAuth for Teams**: Use OAuth for team-wide integrations

### Organization

1. **Project Structure**: Organize projects by team/product
2. **Issue Naming**: Use consistent naming conventions
3. **Label Strategy**: Use labels for categorization
4. **Epic Organization**: Use epics to group related work
5. **Sprint Planning**: Plan sprints aligned with team capacity

### Performance

1. **JQL Optimization**: Use efficient JQL queries
2. **Batch Operations**: Group API calls when possible
3. **Caching**: Cache frequently accessed data
4. **Webhooks**: Use webhooks for real-time updates

## Next Steps

After completing Jira setup:

1. **Configure Methodology**: Set up Scrum or Kanban workflows
2. **Create Workflows**: Configure workflows that integrate with Jira
3. **Set Up Metrics**: Enable metrics tracking
4. **Team Onboarding**: Share setup instructions with your team
5. **Test Integration**: Create test issues and verify end-to-end flow

## Additional Resources

- [Jira API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [Atlassian API Tokens Guide](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)
- [Jira Workflows Guide](https://support.atlassian.com/jira-service-management-cloud/docs/create-and-edit-workflows/)
- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Cursor MCP Documentation](https://cursor.sh/docs/mcp)

## Support

If you encounter issues not covered in this guide:

1. Check the [PM System User Guide](../USER_GUIDE.md)
2. Review [Troubleshooting](#troubleshooting) section above
3. Check Cursor MCP logs for detailed error messages
4. Verify your Jira project permissions and configuration
