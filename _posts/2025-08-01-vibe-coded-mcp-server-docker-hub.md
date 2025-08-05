---
layout: post
title: "How I Vibe-Coded an MCP Server and Got It Published on Docker Hub"
date: 2025-08-01 14:00:00
author: author1
tags: [build-logs, mcp, docker, cursor, vibe-coding, ai-tools]
description: >
  From not knowing Docker to publishing an official MCP server on Docker Hub in 10 days. 
  A behind-the-scenes look at vibe-coding with AI assistance.
related_posts:
  - /blog/multi-agent-ai-systems-landscape
  - /blog/gpt-research-assistant-build
---

# Vibe-Coding an MCP Server

I didn't know how to write a Dockerfile a few weeks ago. I barely knew what MCP (Model Context Protocol) was. But today, my project—arxiv-mcp-server—is live on the Docker MCP Hub, officially published and available for anyone using LLMs with Docker Desktop. I built it mostly in Cursor, vibe-coded the entire thing, and somehow made it work. This post is a behind-the-scenes reflection on how it came together, what I learned, and what it felt like to ship something real despite not being a traditional developer.

---

## The Spark: What Even Is MCP?

A while back, I came across a project called [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server). It lets you run a lightweight server that connects LLMs to arXiv papers through a structured protocol called MCP. That means you can search for papers, download them, read their content, and even generate structured prompts for deep analysis—all from within an AI assistant that supports MCP tools.

I was immediately hooked. I love research papers, and I had already started building a personal research assistant that could parse and synthesize content from arXiv. The problem? The upstream repo didn't have an official Docker image, and I wanted something I could deploy with minimal effort.

That's when I decided to fork it and make it Docker-first.

---

## Vibe Coding in Cursor

Cursor.dev was my main workspace for the entire project. I used Claude and ChatGPT as copilots, bouncing between tools depending on the type of help I needed. There were moments when I had no idea what I was doing, but I kept the momentum by describing what I wanted and letting AI guide me.

At one point I asked, "Can you fix this Dockerfile so it installs dependencies without caching and uses a non-root user?" And boom—I had a clean, minimal base image with proper permissions and volume mounts.

Other times, I ran into strange issues: like why the server couldn't access the mounted /data folder. AI explained Docker volumes, helped me rework the ARXIV_STORAGE_PATH environment variable, and got me unblocked.

It was less about writing perfect code and more about *narrating my intentions* and letting AI help me iterate.

---

## The Build Log, in Hindsight

If I had to break it into milestones, here's what happened:

### 1. Forking and Cleaning Up

I cloned the original repo and stripped out everything I didn't need. I simplified the file structure, rewrote parts of the README to focus on Docker use, and committed the first version with the message: initial docker-first setup.

### 2. Dockerfile Rewrite

This was the big one. The original repo had no Dockerfile, so I created one from scratch with AI's help. I went through maybe 6 or 7 iterations:

- Switched to python:3.11-slim
- Added a user with no root permissions
- Made sure pip cleaned up after install
- Exposed the right ports
- Mounted /mnt/papers as the working volume

Eventually, I got the container running with just:

```bash
docker run -v $(pwd)/papers:/mnt/papers \
  -e ARXIV_STORAGE_PATH=/mnt/papers \
  mcp/arxiv-mcp-server
```

### 3. Testing the Tools

Once the container was live, I ran some test prompts inside Claude:

```json
{"tool": "search_papers", "input": {"query": "transformer architectures"}}
```

That returned IDs. Then I used download_paper and read_paper. I was reading arXiv abstracts from a local Docker container within seconds. That felt like magic.

### 4. CI and GitHub Actions

I wanted some automation but didn't want to overdo it. I added a simple CI workflow:

- Run black, flake8, and mypy
- Run pytest on the test folder
- Build the Docker image and scan it with trivy for vulnerabilities

This gave me just enough peace of mind to push confidently.

### 5. Publishing to Docker MCP Hub

This was surreal.

I submitted the project to the official mcp Docker org and within a couple days, it was accepted. The container showed up in the [Docker MCP Server Gallery](https://hub.docker.com/mcp/explore), with my name on it. It's signed by Docker, listed as a Verified Publisher image, and fully ready to plug into Claude or any other LLM using Docker's new tool system.

I had gone from "what is MCP?" to "this is now a published container" in about 10 days.

---

## What I Learned

- **You don't have to know everything**: Most of this came together one step at a time. I didn't try to master Docker or Python or CI before starting.

- **Cursor is underrated**: Having an AI pair programmer baked into my editor made it feel like a collaborative experience, not a solo grind.

- **Just-in-time learning works**: When I hit something unfamiliar, I looked up just enough to move forward. I never sat down to "study Docker" or "learn pytest." I just solved the next problem.

- **AI doesn't replace effort**: Claude and ChatGPT didn't write this for me. They helped me *write it faster.* They gave me context, explanations, and fixes, but I still had to understand what was happening and test everything myself.

---

## Final Thoughts

I'm proud of this build. Not because it's the most advanced or technically perfect project, but because I followed through. I turned curiosity into something real. And I did it in a way that reflects where development is going: fast, iterative, AI-assisted, and open.

If you're thinking about building something but feel like you're "not technical enough," I hope this encourages you to start anyway. Let your tools carry some of the load. Let your intuition lead the way. And if it breaks? Ask good questions. Try again. Keep going.

That's what vibe coding is all about.

*Next Build Log: "Building a Personal Knowledge Graph with Obsidian and Python"*
