# Jekyll Blog Post Formatting Requirements

## Heading Structure
- **Posts must start with `##` (H2), not `#` (H1)**
- The first `#` heading is reserved for the page title/layout
- All content headings within posts should use `##` and below

## Example Structure
```markdown
---
layout: post
title: "SEO-Optimized Title for Search Engines"
date: YYYY-MM-DD HH:MM:SS
author: author1
tags: [tag1, tag2, tag3]
description: >
  Your post description here.
---

## Engaging Content Title for Readers

**Subtitle or emphasis**

### Section Heading (H3)

Content here...

#### Subsection (H4)

More content...
```

## Title Best Practices
- **Front matter title**: SEO-optimized, keyword-rich title for search engines
- **Content title (first ##)**: Engaging, reader-focused title that hooks attention
- **Avoid duplication**: Don't use the same title in both places
- **Content title can be more creative**: Use compelling hooks, questions, or emotional appeals

## Common Issues
- Starting posts with `#` instead of `##` will cause formatting problems
- The title in the front matter should match the first `##` heading
- All subsequent headings should be `###` and below

## Notes
- This requirement applies to all posts in `_posts/` directory
- The layout handles the main page title automatically
- Content headings should follow proper hierarchy: `##` → `###` → `####` 