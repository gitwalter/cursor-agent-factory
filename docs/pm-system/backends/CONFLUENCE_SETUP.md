# Confluence Setup Guide

This guide walks you through setting up Confluence as your documentation backend for the Cursor Agent Factory PM system. Confluence provides wiki pages, spaces, and templates for PM artifacts like requirements, architecture docs, and retrospectives.

## Prerequisites

- **Atlassian Cloud Account**: A Confluence Cloud account (free tier available)
- **API Token**: Required for API access (same as Jira setup)
- **Node.js 18+**: Required for the MCP server
- **Cursor IDE**: Installed and configured

## Step 1: Create an Atlassian API Token

Confluence uses the same Atlassian API token as Jira. If you've already set up Jira, you can reuse that token.

### 1.1 Navigate to Atlassian Account Settings

1. Log in to your Atlassian account at [id.atlassian.com](https://id.atlassian.com)
2. Click your profile picture in the top right
3. Select **Account settings**
4. Scroll down to **Security** section
5. Click **API tokens**

### 1.2 Generate API Token (if not already done)

1. Click **Create API token**
2. Give your token a label: `Cursor MCP Atlassian`
3. Click **Create**
4. **Copy the token immediately** - you won't be able to see it again!

### 1.3 Note Your Account Details

You'll need:
- **Email**: Your Atlassian account email
- **Domain**: Your Confluence instance domain (e.g., `mycompany.atlassian.net`)

## Step 2: Install Atlassian MCP Server

Confluence uses the same Atlassian MCP server as Jira. If you've already set up Jira, the MCP server is already configured.

### 2.1 Verify MCP Server Configuration

Check your Cursor MCP settings. The Atlassian MCP server should already be configured if you set up Jira:

```json
{
  "mcpServers": {
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

If not configured, follow the [Jira Setup Guide](./JIRA_SETUP.md) to set up the Atlassian MCP server.

## Step 3: Configure Environment Variables

Ensure your `.env` file includes Atlassian credentials:

```bash
# Atlassian API Token (shared with Jira)
ATLASSIAN_API_TOKEN=your_api_token_here

# Atlassian Domain (without https://)
ATLASSIAN_DOMAIN=mycompany.atlassian.net

# Atlassian Email
ATLASSIAN_EMAIL=your.email@example.com
```

## Step 4: Test the Connection

### 4.1 Restart Cursor

1. Close Cursor completely
2. Reopen Cursor
3. The MCP server should start automatically

### 4.2 Verify MCP Server Status

1. Open the MCP panel in Cursor
2. Check that `atlassian-cloud` appears as connected
3. Look for any error messages in the MCP logs

### 4.3 Test Confluence Integration

Try using Confluence-related commands in Cursor:

- List spaces
- Query pages
- Create a test page
- Access page content

If commands work, your connection is successful!

## Step 5: Space Setup Recommendations

### 5.1 Create PM Space

Create a dedicated space for PM artifacts:

1. Go to Confluence
2. Click **Spaces** > **Create space**
3. Choose **Team space**
4. Fill in details:
   - **Name**: `PM System` or `Project Management`
   - **Space key**: `PM` (or your preferred key)
   - **Description**: `Project management artifacts and documentation`
5. Click **Create**

### 5.2 Configure Space Permissions

1. Go to **Space settings** > **Permissions**
2. Set appropriate permissions:
   - **View**: All team members
   - **Edit**: Team members and PM system
   - **Admin**: PM administrators
3. Save permissions

### 5.3 Organize Space Structure

Create a logical page hierarchy:

```
PM System (Space)
├── Requirements
│   ├── Functional Requirements
│   ├── Non-Functional Requirements
│   └── User Stories
├── Architecture
│   ├── System Architecture
│   ├── Technical Design
│   └── API Documentation
├── Planning
│   ├── Sprint Plans
│   ├── Release Plans
│   └── Roadmaps
├── Retrospectives
│   ├── Sprint Retrospectives
│   └── Team Retrospectives
└── Metrics
    ├── Velocity Reports
    └── Burndown Charts
```

## Step 6: Page Templates for PM Artifacts

### 6.1 Create Page Templates

Create reusable templates for common PM artifacts:

#### Epic Template

```markdown
# Epic: {Epic Name}

## Description
{Epic description}

## Goals
- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

## User Stories
- [ ] Story 1
- [ ] Story 2
- [ ] Story 3

## Acceptance Criteria
- Criterion 1
- Criterion 2
- Criterion 3

## Dependencies
- Dependency 1
- Dependency 2

## Status
**Current Status**: {Status}

**Last Updated**: {Date}
```

#### Sprint Plan Template

```markdown
# Sprint {Number}: {Sprint Name}

## Sprint Goal
{Sprint goal}

## Duration
**Start Date**: {Date}
**End Date**: {Date}
**Duration**: {X} weeks

## Team Members
- {Member 1}
- {Member 2}
- {Member 3}

## User Stories

### Story 1: {Story Name}
- **Story Points**: {X}
- **Assignee**: {Name}
- **Status**: {Status}

### Story 2: {Story Name}
- **Story Points**: {X}
- **Assignee**: {Name}
- **Status**: {Status}

## Sprint Metrics
- **Total Story Points**: {X}
- **Completed Story Points**: {X}
- **Velocity**: {X} points/week
```

#### Retrospective Template

```markdown
# Sprint Retrospective: {Sprint Name}

## Date
{Date}

## Participants
- {Participant 1}
- {Participant 2}
- {Participant 3}

## What Went Well
- {Positive point 1}
- {Positive point 2}
- {Positive point 3}

## What Could Be Improved
- {Improvement 1}
- {Improvement 2}
- {Improvement 3}

## Action Items
- [ ] {Action item 1} - Owner: {Name} - Due: {Date}
- [ ] {Action item 2} - Owner: {Name} - Due: {Date}
- [ ] {Action item 3} - Owner: {Name} - Due: {Date}

## Metrics
- **Velocity**: {X} story points
- **Burndown**: {Status}
- **Team Satisfaction**: {Rating}/10
```

### 6.2 Save Templates

1. Create a page with your template content
2. Go to **Page actions** > **Create template**
3. Name your template (e.g., "Epic Template")
4. Save the template
5. Templates will be available when creating new pages

## Step 7: Integration with Jira

### 7.1 Link Confluence Pages to Jira Issues

1. In Confluence, create or edit a page
2. Use the Jira macro to link issues:
   ```
   {jira:PROJ-123}
   ```
3. Or use the Jira Issues macro to display multiple issues:
   ```
   {jiraissues:query=project=PROJ AND sprint="Sprint 1"}
   ```

### 7.2 Embed Jira Boards

Embed Jira boards in Confluence pages:

1. In Confluence, create or edit a page
2. Insert **Jira** macro
3. Select **Board**
4. Choose your Jira board
5. The board will be embedded in the page

### 7.3 Create Requirements Pages from Jira Epics

1. In Jira, open an Epic
2. Click **Create Confluence page**
3. Choose a template (e.g., Epic Template)
4. The page will be created in Confluence with Epic details
5. Link the page back to the Epic

## Step 8: Configure PM System Integration

After Confluence is set up, configure the PM system:

```json
{
  "pm": {
    "enabled": true,
    "backend": {
      "type": "confluence",
      "spaceKey": "PM",
      "workspace": "mycompany.atlassian.net"
    },
    "integration": {
      "jira": {
        "enabled": true,
        "projectKey": "PROJ"
      }
    }
  }
}
```

## Step 9: Automation and Macros

### 9.1 Useful Confluence Macros

- **Jira Issues**: Display Jira issues in Confluence
- **Status**: Show status indicators
- **Info/Warning/Note**: Highlight important information
- **Code Block**: Display code snippets
- **Table of Contents**: Auto-generate TOC
- **Page Tree**: Show page hierarchy

### 9.2 Automation Rules

Set up automation rules:

1. Go to **Space settings** > **Automation**
2. Create rules for:
   - Auto-create pages from Jira Epics
   - Update pages when Jira issues change
   - Notify team when pages are updated
   - Archive old pages automatically

## Troubleshooting

### MCP Server Not Connecting

**Problem**: Confluence MCP server doesn't appear in Cursor

**Solutions**:
1. Verify Atlassian MCP server is configured (same as Jira)
2. Check that API token is correct
3. Verify domain and email are correct
4. Check Cursor MCP logs for errors
5. Restart Cursor completely

### Authentication Errors

**Problem**: "401 Unauthorized" or "403 Forbidden" errors

**Solutions**:
1. Verify API token is correct (no extra spaces)
2. Check token hasn't expired
3. Verify email matches your Atlassian account
4. Ensure domain is correct (without `https://`)
5. Verify you have access to Confluence

### Space Not Found

**Problem**: "Space not found" errors

**Solutions**:
1. Verify space key is correct (case-sensitive)
2. Check you have access to the space
3. Verify space permissions
4. Ensure space exists in Confluence

### Page Creation Errors

**Problem**: "Cannot create page" errors

**Solutions**:
1. Verify you have edit permissions in the space
2. Check space permissions
3. Verify parent page exists (if creating child page)
4. Check page title doesn't conflict with existing page

### Jira Integration Issues

**Problem**: Jira macros not working

**Solutions**:
1. Verify Jira and Confluence are in the same Atlassian instance
2. Check Jira project key is correct
3. Verify you have access to the Jira project
4. Test Jira connection separately

## Best Practices

### Documentation

1. **Consistent Structure**: Use consistent page hierarchies
2. **Templates**: Create and use templates for common artifacts
3. **Labels**: Use labels for categorization and search
4. **Versioning**: Use page versions for change tracking
5. **Comments**: Use comments for discussions

### Organization

1. **Space Strategy**: Organize spaces by team/product/initiative
2. **Page Naming**: Use consistent naming conventions
3. **Hierarchy**: Maintain logical page hierarchies
4. **Archiving**: Archive old pages regularly
5. **Search**: Use labels and titles for better searchability

### Integration

1. **Jira Linking**: Link Confluence pages to Jira issues
2. **Bi-directional**: Keep Jira and Confluence in sync
3. **Automation**: Use automation for repetitive tasks
4. **Macros**: Leverage macros for dynamic content
5. **Templates**: Standardize templates across team

## Next Steps

After completing Confluence setup:

1. **Create Templates**: Set up page templates for PM artifacts
2. **Organize Spaces**: Create and organize spaces
3. **Link Jira**: Integrate with Jira for bi-directional linking
4. **Set Up Automation**: Configure automation rules
5. **Team Onboarding**: Share setup instructions with your team

## Additional Resources

- [Confluence API Documentation](https://developer.atlassian.com/cloud/confluence/rest/v2/)
- [Confluence Macros Guide](https://support.atlassian.com/confluence-cloud/docs/use-macros-in-confluence/)
- [Jira-Confluence Integration](https://support.atlassian.com/confluence-cloud/docs/link-confluence-pages-to-jira-issues/)
- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Cursor MCP Documentation](https://cursor.sh/docs/mcp)

## Support

If you encounter issues not covered in this guide:

1. Check the [PM System User Guide](../USER_GUIDE.md)
2. Review [Troubleshooting](#troubleshooting) section above
3. Check Cursor MCP logs for detailed error messages
4. Verify your Confluence space permissions and configuration
