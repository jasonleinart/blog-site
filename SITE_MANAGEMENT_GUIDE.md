# AI Frontier Site Management Guide

A comprehensive guide for managing your "Field Notes from the AI Frontier" Jekyll site.

---

## 🚀 Quick Start Commands

### **Start Local Development Server**
```bash
bundle exec jekyll serve --livereload --port 4001
```
- Site will be available at: `http://localhost:4001`
- Auto-refreshes when you make changes

### **Build Site for Production**
```bash
bundle exec jekyll build
```

### **Stop Jekyll Server**
- Press `Ctrl+C` in terminal, or:
```bash
pkill -f "jekyll serve"
```

---

## 📝 Creating Content

### **📰 New Blog Post**

#### **Field Notes (Research Paper Analysis)**
```bash
# Create new file in _posts/
_posts/YYYY-MM-DD-title-of-post.md
```

**Template:**
```yaml
---
layout: post
title: "Understanding GPT-4 Architecture: Key Insights"
description: >
  Analysis of the latest GPT-4 research paper and what it means for practitioners
  building AI systems.
categories: [field-notes]
tags: [research-log, llm, gpt, architecture]
author: author1
---

# Key Findings

## Background
Brief context about the research...

## Main Insights
1. **Architecture Changes**: What's different...
2. **Performance Improvements**: Quantified results...
3. **Practical Applications**: How to apply...

## Takeaways for Practitioners
- Actionable insight 1
- Actionable insight 2

## Related Work
- Links to related papers
- Previous analysis in your Field Notes

---

**Sources:**
- [Paper Title](link-to-paper)
- [Related Research](link)
```

#### **Build Logs (Technical Projects)**
```yaml
---
layout: post
title: "Building a GPT-Powered Research Assistant"
description: >
  Complete walkthrough of creating an AI research assistant using Airtable, 
  Apify, and GPT integration.
categories: [build-logs]
tags: [project-log, gpt, airtable, apify, automation]
author: author1
---

# Project Overview

**Problem:** Manual research paper curation is time-consuming...
**Solution:** AI-powered system that...

## Tech Stack
- **AI**: OpenAI GPT-4
- **Database**: Airtable
- **Web Scraping**: Apify
- **Infrastructure**: Google Cloud Functions

## Implementation Steps

### Step 1: Setup Airtable Base
```javascript
// Code examples with explanations
```

### Step 2: Configure Apify Scrapers
Details of scraper configuration...

### Step 3: GPT Integration
How to connect and prompt engineering...

## Lessons Learned
- What worked well
- What didn't work
- What I'd do differently

## Next Iterations
- Planned improvements
- Additional features
```

#### **Mental Models (Strategic Essays)**
```yaml
---
layout: post
title: "AI Agents vs. Automation: A Decision Framework"
description: >
  Strategic framework for understanding when to use AI agents versus 
  traditional automation in business processes.
categories: [mental-models]
tags: [mental-models, strategy, agents, automation]
author: author1
---

# The Core Question

When building intelligent systems, how do you decide between...

## Framework: The AGENT Matrix

### A - Autonomy Required
Does the task require independent decision-making?

### G - Generative Output  
Does it need to create new content/solutions?

### E - Environmental Adaptation
Must it adapt to changing conditions?

### N - Natural Language Processing
Does it involve complex language understanding?

### T - Task Complexity
How variable and complex are the inputs?

## Decision Tree
[Visual diagram or flowchart]

## Real-World Applications
- **Use Agents When**: Examples...
- **Use Automation When**: Examples...

## Implementation Guidelines
Practical steps for applying this framework...
```

#### **Dispatches (Quick Updates)**
```yaml
---
layout: post
title: "Weekly Dispatches: January 15, 2025"
description: >
  This week's interesting AI developments, tools I'm testing, 
  and quick observations from the frontier.
categories: [dispatches]
tags: [dispatch, weekly, tools, observations]
author: author1
---

# This Week's Highlights

## 🔍 Research Radar
- **Paper of the week**: [Title](link) - Why it matters...
- **Emerging pattern**: Trend I'm tracking...

## 🔧 Tools I'm Testing
- **Tool Name**: What it does, first impressions
- **Another Tool**: Quick assessment

## 💭 Random Observations
- Insight about AI adoption...
- Thought about cognitive amplification...

## 📚 Worth Reading
- [Article Title](link) - Why it's valuable
- [Research Paper](link) - Key takeaway

## 🤔 Open Questions
- Question I'm pondering this week
- Area I want to explore further
```

---

## 🎯 Updating Content

### **📍 Update Now Page**

**File**: `now.md`

**Structure:**
```yaml
---
layout: page
title: Now
description: >
  What I'm actively working on, learning, and exploring at the AI frontier.
hide_description: false
---

# 📍 What I'm Doing Now

*Last updated: [CURRENT DATE]*

## 🎯 Current Sprint
**Focus:** [Current main focus]
**Timeline:** [Time period]

### Active Projects
- **Project 1** - Description
- **Project 2** - Description

## 📚 Learning Focus
### Technical Skills
- **AWS Certification** - Progress update
- **New Framework** - What you're learning

### Research Areas  
- **Topic 1** - Current exploration
- **Topic 2** - Questions you're investigating

## 🤔 Open Questions I'm Exploring
1. **Question 1:** What's the real difference...
2. **Question 2:** How can AI tools...

## 🔄 Current Experiments
- **Experiment 1:** Description
- **Experiment 2:** What you're testing

## 📈 What's Coming Next
### Short-term Goals
- Goal 1
- Goal 2

### Longer-term Vision  
- Vision point 1
- Vision point 2
```

### **📄 Update Resume**

**Data File**: `_data/resume.yml`

#### **Add New Work Experience**
```yaml
work:
  - company: "New Company"
    position: "Your Title" 
    website: "https://company.com"
    startDate: "2025-01-01"
    endDate: null  # null for current position
    summary: >
      Description of role and focus areas.
    highlights:
      - "Achievement 1 with metrics"
      - "Achievement 2 with impact"
      - "Achievement 3 with results"
  
  # Previous experience...
  - company: "Previous Company"
    # ... existing entries
```

#### **Add New Skills**
```yaml
skills:
  - name: "New Skill Category"
    level: "Advanced"  # Beginner, Intermediate, Advanced, Master
    keywords:
      - "Specific Tool 1"
      - "Specific Tool 2"
      - "Framework/Method"
```

#### **Add Education/Certifications**
```yaml
education:
  - institution: "Certification Body"
    area: "Specialty Area"
    studyType: "Certification"
    startDate: "2025-01-01"
    endDate: "2025-06-01"
    gpa: ""
    courses:
      - "Course 1"
      - "Course 2"
```

#### **Add Publications**
```yaml
publications:
  - name: "Article/Post Title"
    publisher: "jasonleinart.com"
    releaseDate: "2025-01-01"
    website: "https://jasonleinart.com/link-to-post/"
    summary: "Brief description of the content and its value."
```

---

## 🔗 Social Links & Contact

### **Add Social Media Profile**

**File**: `_config.yml`

Find the `profiles` section in your resume data:
```yaml
# In _data/resume.yml under basics:
profiles:
  - network: "GitHub" 
    username: "jasonleinart"
    url: "https://github.com/jasonleinart"
  - network: "LinkedIn"
    username: "Jason Leinart"
    url: "https://linkedin.com/in/jasonleinart"
  - network: "Twitter"  # Add new platform
    username: "@yourusername"
    url: "https://twitter.com/yourusername"
```

### **Update Contact Information**

**File**: `_data/resume.yml`
```yaml
basics:
  email: "jason@jasonleinart.com"
  phone: "(optional)"
  website: "https://jasonleinart.com"
```

---

## 🎨 Visual Updates

### **Replace Logo**
1. **Add new logo**: Save to `assets/img/new-logo.png`
2. **Update config**: In `_config.yml`:
   ```yaml
   logo: /assets/img/new-logo.png
   ```

### **Replace Background Image**
1. **Add new background**: Save to `assets/img/new-background.jpg`
2. **Update config**: In `_config.yml`:
   ```yaml
   accent_image: /assets/img/new-background.jpg
   ```

### **Use Solid Color Background** (Alternative)
```yaml
accent_image:
  background: rgb(25,55,71)  # Dark blue-gray
  overlay: false
```

### **Update Colors**
```yaml
accent_color: rgb(79,177,186)  # Teal accent
theme_color: rgb(25,55,71)     # Dark theme
```

---

## 📊 Site Configuration

### **Update Site Information**

**File**: `_config.yml`

```yaml
# Basic site info
title: Jason Leinart
description: >
  Field Notes from the AI Frontier. Exploring automation, intelligence, 
  and the systems that shape our future.
tagline: Field Notes from the AI Frontier

# Contact & feed info
feed:
  name: Jason Leinart
  email: jason@jasonleinart.com

# Copyright
copyright: © 2025 Jason Leinart. All rights reserved.
```

### **Add/Remove Navigation Items**

**File**: `_config.yml`
```yaml
menu:
  - title: Field Notes
    url: /field-notes/
  - title: Build Logs  
    url: /build-logs/
  - title: Mental Models
    url: /mental-models/
  - title: Dispatches
    url: /dispatches/
  - title: Now
    url: /now/
  - title: Resume
    url: /resume/
  - title: About
    url: /about/
  # Add new item:
  - title: Projects
    url: /projects/
```

---

## 🏷️ Content Organization

### **Tag Strategy**

**Primary Categories** (use in front matter):
- `field-notes` - Research analysis
- `build-logs` - Technical projects  
- `mental-models` - Strategic frameworks
- `dispatches` - Quick updates

**Thematic Tags**:
- `research-log`, `project-log`, `mental-models`, `dispatch`
- `career-shift`, `life-in-transition`
- `automation`, `agents`, `llm`, `gpt`
- `gcp`, `aws`, `cloud`
- `notion`, `airtable`, `tools`
- `research`, `papers`
- `beginner-friendly`, `technical-deep-dive`, `strategic-overview`

### **File Organization**
```
_posts/
├── 2025-01-06-weekly-ai-dispatches.md          # Dispatch
├── 2025-01-07-agents-vs-automation.md          # Mental Model
├── 2025-01-08-gpt-research-assistant-build.md  # Build Log
└── 2025-01-09-scaling-laws-analysis.md         # Field Notes
```

---

## 🔧 Development Workflow

### **Content Creation Process**
1. **Start local server**: `bundle exec jekyll serve --livereload --port 4001`
2. **Create new post** in `_posts/` folder
3. **Save and preview** changes at `http://localhost:4001`
4. **Refine content** with live reload
5. **Build for production**: `bundle exec jekyll build`

### **Common File Locations**
- **Posts**: `_posts/YYYY-MM-DD-title.md`
- **Pages**: Root directory (e.g., `about.md`, `now.md`)
- **Resume data**: `_data/resume.yml`
- **Site config**: `_config.yml`
- **Images**: `assets/img/`
- **Content type pages**: `_featured_categories/`

### **Front Matter Templates**

**Minimal Post:**
```yaml
---
layout: post
title: "Your Title"
description: >
  SEO description under 160 characters
categories: [field-notes]  # or build-logs, mental-models, dispatches
tags: [relevant, tags, here]
author: author1
---
```

**Page:**
```yaml
---
layout: page
title: "Page Title"
description: >
  Page description for SEO
hide_description: false
---
```

---

## 🐛 Troubleshooting

### **Common Issues**

**Jekyll won't start:**
```bash
bundle install  # Install missing gems
bundle exec jekyll serve --trace  # See detailed errors
```

**Changes not showing:**
- Check syntax in front matter (YAML)
- Ensure proper file naming: `YYYY-MM-DD-title.md`
- Restart Jekyll server

**Broken links:**
- Check file paths are correct
- Ensure URLs in `_config.yml` match your setup

**Images not loading:**
- Verify image paths: `/assets/img/filename.ext`
- Check file exists in `assets/img/` folder
- Ensure proper file extensions

### **Validation**
- **YAML Front Matter**: Use online YAML validator
- **Markdown**: Preview in VS Code or similar
- **Site Build**: Check terminal for error messages

---

## 📱 Going Live

### **Deployment Checklist**
1. ✅ All content reviewed and proofread
2. ✅ Images optimized and properly linked
3. ✅ Contact information updated
4. ✅ Navigation working correctly
5. ✅ Local build successful: `bundle exec jekyll build`
6. ✅ Test all major pages and links
7. ✅ Resume PDF updated (if applicable)

### **GitHub Repository**
- Commit changes with descriptive messages
- Push to new repository for deployment
- Configure GitHub Pages or deploy to preferred host

---

## 💡 Content Ideas & Planning

### **Content Calendar Template**
- **Monday**: Research review (Field Notes potential)
- **Wednesday**: Project progress (Build Logs updates)  
- **Friday**: Weekly Dispatch (quick observations)
- **Monthly**: Mental Models essay (strategic deep-dive)

### **Evergreen Content Ideas**
- **AI tool comparisons** and honest reviews
- **Research paper summaries** with practical takeaways
- **Career transition insights** and lessons learned
- **Systems thinking** applied to AI/automation
- **Building in public** project documentation

---

*This guide covers the most common site management tasks. Keep this file updated as you discover new workflows and requirements.* 