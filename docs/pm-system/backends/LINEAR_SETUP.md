# Linear Setup Guide

This guide walks you through setting up Linear as your PM backend for the Cursor Agent Factory PM system. Linear provides modern issue tracking, cycles (sprints), projects, and roadmaps with a developer-friendly interface.

## Prerequisites

- **Linear Account**: A Linear account (free tier available)
- **API Key**: Required for API access
- **Node.js 18+**: Required for the MCP server (if using local server)
- **Cursor IDE**: Installed and configured

## Step 1: Create a Linear API Key

Linear uses API keys for authentication. You can generate one through Linear's web interface.

### 1.1 Navigate to Linear Settings

1. Log in to [Linear](https://linear.app)
2. Click your profile picture in the top right
3. Select **Settings**
4. Navigate to **API** section

### 1.2 Generate Personal API Key (Recommended)

1. Scroll to **Personal API keys**
2. Click **Create API key**
3. Give your key a name: `Cursor MCP Linear`
4. Select the scopes/permissions you need:
   - ✅ **Read**: View issues, projects, teams, cycles
   - ✅ **Write**: Create and update issues, comments
   - ✅ **Admin**: Full access (use with caution)
5. Click **Create**
6. **Copy the API key immediately** - you won't be able to see it again!

**Note**: Linear API keys start with `lin_api_` prefix.

### 1.3 Alternative: OAuth Application (For Team/Organization Use)

If you need OAuth-based authentication for team-wide access:

1. Go to **Settings** > **Applications**
2. Click **Create application**
3. Fill in application details:
   - **Name**: `Cursor MCP Integration`
   - **Description**: `MCP server integration for Cursor IDE`
   - **Redirect URLs**: Not required for MCP server
4. After creating, go to the **API** tab
5. Generate an API key from the application
6. Copy the API key

## Step 2: Choose Installation Method

You have two options for the Linear MCP server:

### Option 1: Remote MCP Server (Recommended)

**Recommended for**: Most users who want a managed service

**Pros**:
- No local installation required
- Automatic updates
- Managed service

**Cons**:
- Requires internet connection
- May have rate limits

### Option 2: Local MCP Server

**Recommended for**: Users who want local control

**Pros**:
- Full control over installation
- No external dependencies
- Can customize configuration

**Cons**:
- Requires local Node.js environment
- Manual updates needed

## Option 1: Remote MCP Server Setup

### Step 1.1: Configure Remote MCP Server

The Linear remote MCP server is available at `https://mcp.linear.app/mcp`.

Configure Cursor MCP settings:

```json
{
  "mcpServers": {
    "linear": {
      "url": "https://mcp.linear.app/mcp",
      "headers": {
        "Authorization": "Bearer ${LINEAR_API_KEY}"
      }
    }
  }
}
```

### Step 1.2: Configure Environment Variables

Create or update your `.env` file:

```bash
# Linear API Key
LINEAR_API_KEY=lin_api_your_api_key_here
```

### Step 1.3: Complete OAuth Authorization (if using OAuth)

If using OAuth instead of API key:

1. The MCP server will initiate the OAuth flow when first used
2. You'll be redirected to Linear to authorize the application
3. After authorization, the access token will be stored
4. Subsequent requests will use the stored token

## Option 2: Local MCP Server Setup

### Step 2.1: Install Linear MCP Server

The Linear MCP server is installed via npm/npx. No manual installation is required - it will be downloaded automatically when Cursor starts the MCP server.

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

### Step 2.2: Configure Environment Variables

Create or update your `.env` file:

```bash
# Linear API Key
LINEAR_API_KEY=lin_api_your_api_key_here
```

**Security Note**: 
- Never commit `.env` files to version control
- Add `.env` to your `.gitignore`
- Use environment variables or secure credential storage in production

### Step 2.3: Configure Cursor MCP Settings

Locate your MCP configuration file (see [GitHub Setup Guide](./GITHUB_SETUP.md#41-locate-mcp-configuration-file) for paths).

Add the Linear MCP server configuration:

```json
{
  "mcpServers": {
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

**Note**: Replace `${LINEAR_API_KEY}` with your actual API key, or ensure the `LINEAR_API_KEY` environment variable is set in your system.

### Step 2.4: Alternative Direct Configuration

If you prefer to set the API key directly (not recommended for shared configs):

```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-linear"],
      "env": {
        "LINEAR_API_KEY": "lin_api_your_actual_key_here"
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

1. Open the MCP panel in Cursor (if available)
2. Check that `linear` appears as connected
3. Look for any error messages in the MCP logs

### 3.3 Test Linear Integration

Try using Linear-related commands in Cursor:

- List teams
- Query issues
- Create a test issue
- Access cycles and projects

If commands work, your connection is successful!

## Step 4: Team and Project Setup

### 4.1 Create or Select Team

1. Go to [Linear](https://linear.app)
2. Click **Teams** in the sidebar
3. Create a new team or select an existing one:
   - Click **New Team**
   - Fill in team details:
     - **Name**: Your team name
     - **Key**: Team key (e.g., `ENG`, `PROD`)
     - **Description**: Team description (optional)
   - Click **Create**

### 4.2 Configure Team Settings

1. Go to **Team Settings**
2. Configure team preferences:
   - **Issue numbering**: Set issue number format
   - **Labels**: Create team-specific labels
   - **States**: Configure workflow states
   - **Priorities**: Set priority levels

### 4.3 Set Up Projects

1. Go to **Projects** in Linear
2. Create a new project:
   - Click **New Project**
   - Fill in project details:
     - **Name**: Project name
     - **Description**: Project description
     - **Team**: Assign to team
     - **Target Date**: Project deadline (optional)
   - Click **Create**

### 4.4 Configure Cycles (Sprints)

For sprint-based methodologies:

1. Go to **Cycles** in Linear
2. Create a new cycle:
   - Click **New Cycle**
   - Fill in cycle details:
     - **Name**: Cycle name (e.g., "Sprint 1")
     - **Team**: Assign to team
     - **Start Date**: Cycle start date
     - **End Date**: Cycle end date
   - Click **Create**

### 4.5 Set Up Workflow States

Configure workflow states based on your methodology:

**For Scrum**:
- Backlog → Todo → In Progress → In Review → Done

**For Kanban**:
- Backlog → Ready → In Progress → Testing → Done

1. Go to **Team Settings** > **Workflow**
2. Customize states:
   - Add/remove states
   - Set state types (unstarted, started, completed, canceled)
   - Configure state transitions
   - Set default states

## Step 5: Configure PM System Integration

After Linear is set up, configure the PM system:

```json
{
  "pm": {
    "enabled": true,
    "backend": {
      "type": "linear",
      "projectId": "team-id",
      "workspace": "my-workspace"
    }
  }
}
```

## Troubleshooting

### MCP Server Not Connecting

**Problem**: Linear MCP server doesn't appear in Cursor

**Solutions**:
1. **For Remote Server**:
   - Verify API key is correct
   - Check internet connection
   - Verify Linear service is accessible

2. **For Local Server**:
   - Verify Node.js is installed: `node --version` (should be 18+)
   - Check that `npx` is available: `npx --version`
   - Verify your API key is correct
   - Check Cursor MCP logs for error messages
   - Ensure the MCP config file path is correct
   - Restart Cursor completely

### Authentication Errors

**Problem**: "401 Unauthorized" or "Invalid API key" errors

**Solutions**:
1. Verify your API key is correct (starts with `lin_api_`)
2. Check API key hasn't been revoked
3. Ensure API key has required scopes (Read, Write)
4. Verify environment variable is set correctly
5. Try using the API key directly in config (temporarily) to test

### Permission Errors

**Problem**: "403 Forbidden" or "Access denied" errors

**Solutions**:
1. Verify you have access to the team/project
2. Check team permissions in Linear
3. Ensure API key has required scopes
4. Verify you're a member of the team
5. Check workspace permissions

### Team Not Found

**Problem**: "Team not found" errors

**Solutions**:
1. Verify team key/ID is correct (case-sensitive)
2. Check you have access to the team
3. Verify team exists in Linear
4. Ensure team is active (not archived)

### Issue Creation Errors

**Problem**: "Cannot create issue" errors

**Solutions**:
1. Verify you have write permissions in the team
2. Check team permissions
3. Verify required fields are provided
4. Check issue type is valid for the team

### Environment Variable Not Found

**Problem**: `${LINEAR_API_KEY}` not resolving

**Solutions**:
1. Set environment variable in your system:
   - **Windows**: `$env:LINEAR_API_KEY = "lin_api_your_key"`
   - **macOS/Linux**: `export LINEAR_API_KEY="lin_api_your_key"`
2. Or use the API key directly in config (less secure)
3. Ensure `.env` file is in the correct location
4. Restart Cursor after setting environment variables

### Rate Limiting

**Problem**: "Rate limit exceeded" errors

**Solutions**:
1. Linear API has rate limits (varies by plan)
2. Implement request caching if making many calls
3. Use webhooks instead of polling when possible
4. Consider upgrading Linear plan for higher limits

## Best Practices

### Security

1. **Use API Keys**: Prefer API keys over OAuth for simple integrations
2. **Key Rotation**: Rotate API keys regularly
3. **Minimal Scopes**: Only grant necessary scopes to your API key
4. **Separate Keys**: Use different keys for different purposes
5. **Secure Storage**: Store API keys in secure credential managers

### Organization

1. **Team Structure**: Organize teams by product/feature/initiative
2. **Project Organization**: Use projects to group related work
3. **Label Strategy**: Use consistent labels across teams
4. **Cycle Planning**: Plan cycles aligned with sprints/releases
5. **Issue Templates**: Use issue templates for consistency

### Performance

1. **Batch Operations**: Group API calls when possible
2. **Query Optimization**: Use efficient GraphQL queries
3. **Caching**: Cache frequently accessed data
4. **Webhooks**: Use webhooks for real-time updates

## Next Steps

After completing Linear setup:

1. **Configure Methodology**: Set up your development methodology (Scrum, Kanban, etc.)
2. **Create Workflows**: Configure workflows that integrate with Linear
3. **Set Up Metrics**: Enable metrics tracking for your PM system
4. **Team Onboarding**: Share setup instructions with your team
5. **Test Integration**: Create test issues and verify end-to-end flow

## Additional Resources

- [Linear API Documentation](https://developers.linear.app/docs)
- [Linear GraphQL API](https://developers.linear.app/docs/graphql/working-with-the-graphql-api)
- [Linear API Keys Guide](https://linear.app/docs/api)
- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Cursor MCP Documentation](https://cursor.sh/docs/mcp)

## Support

If you encounter issues not covered in this guide:

1. Check the [PM System User Guide](../USER_GUIDE.md)
2. Review [Troubleshooting](#troubleshooting) section above
3. Check Cursor MCP logs for detailed error messages
4. Verify your Linear workspace permissions and team configuration
