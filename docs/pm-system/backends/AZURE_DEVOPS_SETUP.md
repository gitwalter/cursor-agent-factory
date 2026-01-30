# Azure DevOps Setup Guide

This guide walks you through setting up Azure DevOps as your PM backend for the Cursor Agent Factory PM system. Azure DevOps provides work item tracking, boards, sprints, and full ALM (Application Lifecycle Management) capabilities.

## Prerequisites

- **Azure DevOps Organization**: An Azure DevOps organization account (free tier available)
- **Personal Access Token (PAT)**: Required for API access
- **Node.js 18+**: Required for the MCP server
- **Cursor IDE**: Installed and configured

## Step 1: Create an Azure DevOps Personal Access Token (PAT)

### 1.1 Navigate to Azure DevOps

1. Log in to [Azure DevOps](https://dev.azure.com)
2. Click your profile picture in the top right
3. Select **Security** (or go to [User Settings > Personal Access Tokens](https://dev.azure.com/_usersSettings/tokens))

### 1.2 Generate New Token

1. Click **+ New Token**
2. Fill in token details:
   - **Name**: `Cursor MCP Azure DevOps`
   - **Organization**: Select your organization
   - **Expiration**: Choose expiration (90 days, 1 year, or custom)
   - **Scopes**: Select required scopes:
     - ✅ **Work Items**: Read & write
     - ✅ **Code**: Read (if integrating with repos)
     - ✅ **Project and Team**: Read & write
     - ✅ **Boards**: Read & write
     - ✅ **Sprints**: Read & write
3. Click **Create**
4. **Copy the token immediately** - you won't be able to see it again!

### 1.3 Note Your Organization Details

You'll need:
- **Organization Name**: Your Azure DevOps organization name (e.g., `mycompany`)
- **Project Name**: Your project name (e.g., `MyProject`)

## Step 2: Install Azure DevOps MCP Server

The Azure DevOps MCP server is installed via npm/npx. No manual installation is required - it will be downloaded automatically when Cursor starts the MCP server.

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
# Azure DevOps Personal Access Token
AZURE_DEVOPS_PAT=your_pat_here

# Azure DevOps Organization
AZURE_DEVOPS_ORG=mycompany

# Azure DevOps Project (optional, can be set per operation)
AZURE_DEVOPS_PROJECT=MyProject
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
4. Add or update the Azure DevOps MCP server configuration:

```json
{
  "mcpServers": {
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

**Note**: Replace `${AZURE_DEVOPS_PAT}`, `${AZURE_DEVOPS_ORG}`, and `${AZURE_DEVOPS_PROJECT}` with your actual values, or ensure these environment variables are set in your system.

### 4.3 Alternative: Direct Configuration

If you prefer to set values directly (not recommended for shared configs):

```json
{
  "mcpServers": {
    "azure-devops": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-azure-devops"],
      "env": {
        "AZURE_DEVOPS_PAT": "your_pat_here",
        "AZURE_DEVOPS_ORG": "mycompany",
        "AZURE_DEVOPS_PROJECT": "MyProject"
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
2. Check that `azure-devops` appears as connected
3. Look for any error messages in the MCP logs

### 5.3 Test Azure DevOps Integration

Try using Azure DevOps-related commands in Cursor:

- List projects
- Query work items
- Create a test work item
- Access boards and sprints

If commands work, your connection is successful!

## Step 6: Project and Board Setup

### 6.1 Create or Select Project

1. Go to [Azure DevOps](https://dev.azure.com)
2. Select your organization
3. Create a new project or select an existing one:
   - Click **New project**
   - Fill in project details:
     - **Project name**: Your project name
     - **Visibility**: Private or Public
     - **Version control**: Git or TFVC
     - **Work item process**: Agile, Scrum, or Basic
   - Click **Create**

### 6.2 Configure Work Item Types

Azure DevOps comes with predefined work item types based on your process template:

**Agile Process**:
- Epic
- Feature
- User Story
- Task
- Bug
- Issue

**Scrum Process**:
- Epic
- Feature
- Product Backlog Item
- Task
- Bug
- Impediment

**Basic Process**:
- Epic
- Issue
- Task

Ensure your project has the work item types you need.

### 6.3 Set Up Boards

#### Create Team Board

1. Go to **Boards** > **Boards**
2. Select your team
3. Configure columns based on your methodology:

**For Scrum**:
- New → Active → Resolved → Closed

**For Kanban**:
- New → Approved → Committed → Done

#### Configure Board Columns

1. Click **Column options**
2. Add or remove columns as needed
3. Set up column limits (WIP limits for Kanban)
4. Configure column rules (auto-assign, notifications)

### 6.4 Configure Sprints

For sprint-based methodologies:

1. Go to **Boards** > **Sprints**
2. Click **Configure team settings**
3. Set up sprint schedule:
   - Sprint duration (typically 1-4 weeks)
   - Sprint start day
   - Sprint naming pattern
4. Create sprints:
   - Click **New sprint**
   - Set sprint dates
   - Assign work items to sprint

### 6.5 Set Up Areas and Iterations

1. Go to **Project settings** > **Boards**
2. Configure **Areas**:
   - Create area paths (e.g., `\Product\Feature1`)
   - Assign teams to areas
3. Configure **Iterations**:
   - Create iteration paths (e.g., `\Sprint 1`, `\Sprint 2`)
   - Set iteration dates
   - Assign teams to iterations

## Step 7: Configure PM System Integration

After Azure DevOps is set up, configure the PM system:

```json
{
  "pm": {
    "enabled": true,
    "backend": {
      "type": "azure-devops",
      "projectId": "MyProject",
      "workspace": "mycompany"
    }
  }
}
```

## Troubleshooting

### MCP Server Not Connecting

**Problem**: Azure DevOps MCP server doesn't appear in Cursor

**Solutions**:
1. Verify Node.js is installed: `node --version` (should be 18+)
2. Check that `npx` is available: `npx --version`
3. Verify your PAT is correct and has required scopes
4. Check Cursor MCP logs for error messages
5. Ensure the MCP config file path is correct
6. Restart Cursor completely

### Authentication Errors

**Problem**: "401 Unauthorized" or "Bad credentials" errors

**Solutions**:
1. Verify your PAT is correct (no extra spaces or characters)
2. Check token expiration - generate a new token if expired
3. Ensure token has required scopes (Work Items, Boards, Sprints)
4. Verify organization name is correct (case-sensitive)
5. Try using the token directly in config (temporarily) to test

### Permission Errors

**Problem**: "403 Forbidden" or "Access denied" errors

**Solutions**:
1. Verify you have access to the organization and project
2. Check project permissions in Azure DevOps
3. Ensure PAT has required scopes
4. Verify you're a member of the project team
5. Check organization security policies

### Project Not Found

**Problem**: "Project not found" errors

**Solutions**:
1. Verify project name is correct (case-sensitive)
2. Check you have access to the project
3. Verify organization name is correct
4. Ensure project exists in Azure DevOps
5. Try listing projects to verify access

### Work Item Type Errors

**Problem**: "Work item type not found" errors

**Solutions**:
1. Verify work item type exists in your process template
2. Check process template (Agile, Scrum, Basic)
3. Ensure work item type is enabled
4. Verify you're using the correct type name

### Board Configuration Issues

**Problem**: Board not displaying correctly or missing columns

**Solutions**:
1. Verify board is configured for your team
2. Check column configuration in board settings
3. Ensure work item states match board columns
4. Verify team is assigned to the board
5. Check process template matches board configuration

### Environment Variable Not Found

**Problem**: `${AZURE_DEVOPS_PAT}` not resolving

**Solutions**:
1. Set environment variable in your system:
   - **Windows**: `$env:AZURE_DEVOPS_PAT = "your_token"`
   - **macOS/Linux**: `export AZURE_DEVOPS_PAT="your_token"`
2. Or use values directly in config (less secure)
3. Ensure `.env` file is in the correct location
4. Restart Cursor after setting environment variables

## Best Practices

### Security

1. **Use PATs**: Use Personal Access Tokens instead of passwords
2. **Token Rotation**: Rotate tokens regularly (every 90 days recommended)
3. **Minimal Scopes**: Only grant necessary scopes to your token
4. **Separate Tokens**: Use different tokens for different purposes
5. **Secure Storage**: Store tokens in secure credential managers

### Organization

1. **Project Structure**: Organize projects by team/product/initiative
2. **Area Paths**: Use area paths to organize work
3. **Iteration Planning**: Plan iterations aligned with sprints/releases
4. **Work Item Naming**: Use consistent naming conventions
5. **Tags**: Use tags for categorization and filtering

### Performance

1. **Batch Operations**: Group API calls when possible
2. **Query Optimization**: Use efficient work item queries
3. **Caching**: Cache frequently accessed data
4. **Webhooks**: Use webhooks for real-time updates

## Next Steps

After completing Azure DevOps setup:

1. **Configure Methodology**: Set up your development methodology (Scrum, Kanban, etc.)
2. **Create Workflows**: Configure workflows that integrate with Azure DevOps
3. **Set Up Metrics**: Enable metrics tracking for your PM system
4. **Team Onboarding**: Share setup instructions with your team
5. **Test Integration**: Create test work items and verify end-to-end flow

## Additional Resources

- [Azure DevOps REST API Documentation](https://learn.microsoft.com/en-us/rest/api/azure/devops/)
- [Azure DevOps Boards Documentation](https://learn.microsoft.com/en-us/azure/devops/boards/)
- [Azure DevOps Personal Access Tokens Guide](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate)
- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Cursor MCP Documentation](https://cursor.sh/docs/mcp)

## Support

If you encounter issues not covered in this guide:

1. Check the [PM System User Guide](../USER_GUIDE.md)
2. Review [Troubleshooting](#troubleshooting) section above
3. Check Cursor MCP logs for detailed error messages
4. Verify your Azure DevOps organization permissions and project configuration
