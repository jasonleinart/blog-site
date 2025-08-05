---
layout: post
title: "Building a GPT-Powered Research Assistant with Airtable + Apify"
date: 2025-01-08 10:00:00
author: author1
tags: [build-logs, automation, gpt, airtable, apify, research-workflow, ai-tools]
description: >
  Step-by-step walkthrough of building an AI research assistant that automatically 
  curates, analyzes, and organizes academic papers using GPT-4, Airtable, and Apify.
image:
  path: /assets/img/sidebar-bg.jpg
related_posts:
  - /blog/scaling-laws-what-they-really-tell-us
  - /blog/agents-vs-automation
---

# 🔧 Build Log: GPT-Powered Research Assistant

**Project:** Automated AI research paper curation and analysis system  
**Tech Stack:** GPT-4, Airtable, Apify, Google Cloud Functions, Python  
**Status:** MVP complete, iterating on analysis quality  
**Build Time:** ~20 hours over 2 weeks  

---

## The Problem

I was drowning in AI research papers. arXiv alone publishes 50+ AI papers daily, and manually tracking what's important was becoming impossible. I needed a system that could:

1. **Monitor** key research sources automatically
2. **Filter** papers by relevance to my interests
3. **Analyze** papers for key insights and practical implications
4. **Organize** findings in a searchable, actionable format

## Solution Architecture

```
arXiv/Papers → Apify Scraper → GPT-4 Analysis → Airtable Database → Alerts/Summaries
```

### Why This Stack:
- **Airtable:** Perfect for structured research data with rich fields
- **Apify:** Reliable web scraping with built-in scheduling
- **GPT-4:** Best available model for research analysis and summarization
- **Google Cloud Functions:** Serverless orchestration and cost control

## Implementation Walkthrough

### Step 1: Setting Up Airtable Base

Created a research database with these key fields:

```
Papers Table:
- Title (Single line text)
- Authors (Multiple select)
- Abstract (Long text)
- PDF URL (URL)
- arXiv ID (Single line text)
- Publication Date (Date)
- Research Area (Multiple select: LLM, Agents, Scaling, etc.)
- Relevance Score (Number 1-10)
- Key Insights (Long text)
- Practical Implications (Long text)
- Status (Select: New, Analyzed, Archived)
- Tags (Multiple select)
```

**Key Design Decision:** Separate analysis fields from paper metadata to track GPT-4's interpretations alongside raw data.

### Step 2: Apify Web Scraper Configuration

Built a custom actor to monitor research sources:

```python
# Simplified scraper logic
import requests
from datetime import datetime, timedelta

def scrape_arxiv_cs_ai():
    """Scrape recent CS.AI papers from arXiv"""
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
    
    query_params = {
        'search_query': 'cat:cs.AI OR cat:cs.LG OR cat:cs.CL',
        'start': 0,
        'max_results': 100,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    
    response = requests.get('http://export.arxiv.org/api/query', params=query_params)
    # Parse XML response and extract paper metadata
    return parsed_papers
```

**Scheduling:** Runs daily at 8 AM to catch new submissions

### Step 3: GPT-4 Analysis Pipeline

The most critical component—getting consistent, useful analysis from GPT-4:

```python
def analyze_paper(title, abstract, authors):
    """Analyze paper relevance and extract insights"""
    
    prompt = f"""
    Analyze this AI research paper for practical implications:
    
    Title: {title}
    Authors: {authors}
    Abstract: {abstract}
    
    Provide:
    1. Relevance Score (1-10) for AI practitioners focused on agents/automation
    2. Key Technical Insights (2-3 bullet points)
    3. Practical Implications (how could this be applied?)
    4. Research Area Tags (choose from: LLM, Agents, Scaling, Training, etc.)
    
    Format as JSON for easy parsing.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1  # Low temperature for consistent analysis
    )
    
    return json.loads(response.choices[0].message.content)
```

**Prompt Engineering Notes:**
- Specific scoring criteria prevent score inflation
- JSON format enables automated data entry
- Low temperature improves consistency
- Examples in prompt improve analysis quality

### Step 4: Airtable Integration

Used Airtable's API to store analyzed papers:

```python
def store_paper_analysis(paper_data, analysis):
    """Store paper and analysis in Airtable"""
    
    record = {
        'Title': paper_data['title'],
        'Authors': paper_data['authors'],
        'Abstract': paper_data['abstract'],
        'PDF URL': paper_data['pdf_url'],
        'arXiv ID': paper_data['arxiv_id'],
        'Publication Date': paper_data['pub_date'],
        'Relevance Score': analysis['relevance_score'],
        'Key Insights': analysis['insights'],
        'Practical Implications': analysis['implications'],
        'Tags': analysis['tags'],
        'Status': 'New'
    }
    
    airtable_client.create(record)
```

### Step 5: Cloud Function Orchestration

Google Cloud Function that orchestrates the entire pipeline:

```python
def research_assistant_pipeline(request):
    """Main pipeline function"""
    
    # 1. Trigger Apify scraper
    new_papers = apify_client.call_actor('my-arxiv-scraper')
    
    # 2. Filter for unprocessed papers
    unprocessed = filter_new_papers(new_papers)
    
    # 3. Analyze each paper with GPT-4
    for paper in unprocessed:
        analysis = analyze_paper(paper['title'], paper['abstract'], paper['authors'])
        
        # 4. Store in Airtable if relevance score > 6
        if analysis['relevance_score'] >= 6:
            store_paper_analysis(paper, analysis)
    
    # 5. Generate weekly summary
    if is_friday():
        generate_weekly_summary()
    
    return {'status': 'success', 'papers_processed': len(unprocessed)}
```

## Results & Metrics

After 2 weeks of operation:

### Performance:
- **Papers Processed:** 347 total papers analyzed
- **High-Relevance Papers:** 23 papers scored 8+ (6.6% pass rate)
- **Processing Time:** ~30 seconds per paper
- **Cost:** $12.50 in OpenAI API calls
- **Accuracy:** 85% of high-scored papers were genuinely relevant (manual verification)

### Unexpected Insights:
1. **GPT-4 is consistently conservative** with scoring (good thing)
2. **Abstract quality varies dramatically** across papers
3. **Certain research groups** produce consistently high-quality work
4. **Weekend submissions** tend to be lower quality

## Lessons Learned

### What Worked Well:
- **JSON-formatted prompts** made data integration seamless
- **Conservative relevance scoring** reduced noise significantly
- **Airtable's rich fields** perfect for research data
- **Daily processing** kept the system manageable

### What I'd Do Differently:
- **Add semantic search** across stored papers for better discovery
- **Include citation analysis** to identify important papers early
- **Build feedback loop** to improve GPT-4 analysis over time
- **Add automated social sharing** for high-relevance papers

### Scaling Challenges:
- **API rate limits** become an issue with more papers
- **GPT-4 costs** could be significant at larger scale
- **Storage costs** in Airtable with thousands of papers
- **Analysis consistency** degrades with batch processing

## Next Iterations

### Phase 2 Features:
1. **Citation Network Analysis** - Track paper influence and connections
2. **Researcher Following** - Monitor specific authors automatically
3. **Conference Paper Integration** - Expand beyond arXiv to venue papers
4. **Smart Alerts** - Notify when papers match specific interests

### Technical Improvements:
- **Vector embeddings** for better semantic matching
- **Fine-tuned model** for research analysis (cheaper than GPT-4)
- **Incremental processing** to handle larger volumes
- **Quality feedback loops** based on manual relevance ratings

## Code Repository

Full implementation available at: [GitHub - AI Research Assistant](https://github.com/jasonleinart/ai-research-assistant)

**Includes:**
- Apify scraper configuration
- Cloud Function deployment scripts
- Airtable schema definitions
- GPT-4 prompt templates
- Cost optimization strategies

---

*Next Build Log: Setting up automated CRM → BigQuery pipelines with Cloud Functions and error handling.* 