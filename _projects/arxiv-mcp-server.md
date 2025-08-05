---
layout: project
title: 'ArXiv MCP Server'
caption: Docker-first MCP server for AI research paper discovery and analysis
description: >
  A Model Context Protocol (MCP) server that connects LLMs to arXiv papers through a clean API. 
  Built with Docker-first architecture and published on the official Docker MCP Hub.
date: '2025-08-01'
image: 
  path: /assets/img/projects/arxiv-mcp-hero.jpg
  srcset: 
    1920w: /assets/img/projects/arxiv-mcp-hero.jpg
    960w:  /assets/img/projects/arxiv-mcp-hero@0,5x.jpg
    480w:  /assets/img/projects/arxiv-mcp-hero@0,25x.jpg
links:
  - title: Docker Hub
    url: https://hub.docker.com/r/mcp/arxiv-mcp-server
  - title: GitHub
    url: https://github.com/jasonleinart/arxiv-mcp-server
  - title: MCP Hub
    url: https://hub.docker.com/mcp/explore
accent_color: '#4fb1ba'
accent_image:
  background: '#193747'
theme_color: '#193747'
featured: true
---

## Overview

The ArXiv MCP Server bridges the gap between Large Language Models and academic research by providing structured access to arXiv papers through the Model Context Protocol. Built with a Docker-first approach, it's designed for easy deployment and integration with AI assistants.

## Key Features

### 🔍 **Paper Discovery**
- Search arXiv by keywords, authors, or categories
- Filter by publication date and relevance
- Access to 2M+ research papers

### 📄 **Content Access**
- Download and parse PDF content
- Extract abstracts, titles, and metadata
- Generate structured summaries for LLM consumption

### 🐳 **Docker-First Architecture**
- One-command deployment with Docker
- Persistent storage for downloaded papers
- Environment-based configuration
- Production-ready container setup

### 🔗 **MCP Integration**
- Official MCP protocol compliance
- Works with Claude, ChatGPT, and other MCP-compatible LLMs
- Structured tool definitions for reliable AI interaction

## Technical Stack

- **Language**: Python 3.11
- **Framework**: FastAPI for the MCP server
- **Storage**: Local filesystem with Docker volumes
- **PDF Processing**: PyPDF2 for content extraction
- **API**: arXiv API for paper metadata and downloads
- **Containerization**: Docker with multi-stage builds

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   LLM Client    │───▶│  MCP Server     │───▶│   arXiv API     │
│  (Claude, etc.) │    │  (Docker)       │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │  Local Storage  │
                       │  (Papers Cache) │
                       └─────────────────┘
```

## Getting Started

### Quick Start with Docker

```bash
# Pull and run the official image
docker run -v $(pwd)/papers:/mnt/papers \
  -e ARXIV_STORAGE_PATH=/mnt/papers \
  mcp/arxiv-mcp-server
```

### Integration with Claude

```json
{
  "mcpServers": {
    "arxiv": {
      "command": "docker",
      "args": ["run", "--rm", "-v", "./papers:/mnt/papers", 
               "-e", "ARXIV_STORAGE_PATH=/mnt/papers", 
               "mcp/arxiv-mcp-server"]
    }
  }
}
```

## Use Cases

### 📚 **Research Assistant**
- "Find recent papers on transformer architectures"
- "Summarize the key findings from this arXiv paper"
- "What are the latest developments in multi-agent systems?"

### 🔬 **Literature Review**
- Systematic paper discovery and analysis
- Trend identification across research areas
- Citation and reference tracking

### 🤖 **AI-Powered Research**
- LLM-assisted paper analysis
- Automated research summaries
- Intelligent paper recommendations

## Development Journey

This project started as a fork of an existing arXiv MCP server that lacked Docker support. Through iterative development with AI assistance (primarily Cursor and Claude), I:

1. **Dockerized the application** with proper volume mounts and environment configuration
2. **Simplified the deployment process** to a single Docker command
3. **Added production-ready features** like proper logging and error handling
4. **Submitted to Docker MCP Hub** and achieved official publication status

The entire development process took about 10 days, demonstrating the power of AI-assisted development for rapid prototyping and deployment.

## Impact

- **Published on Docker MCP Hub** as an official, verified container
- **Zero-friction deployment** for researchers and AI enthusiasts
- **Active community usage** with positive feedback from early adopters
- **Template for future MCP projects** showing Docker-first best practices

## What I Learned

- **Docker containerization** patterns for Python applications
- **MCP protocol implementation** and tool definition standards
- **AI-assisted development** workflows using Cursor and Claude
- **Open source publishing** processes for Docker Hub and MCP ecosystem

---

*Want to see how this was built? Check out the detailed [build log](/blog/ai-automation/vibe-coded-mcp-server-docker-hub/) for a complete walkthrough of the development process.*