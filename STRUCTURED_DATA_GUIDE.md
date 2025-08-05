# Structured Data & LLM Optimization Guide

This site now includes comprehensive structured data markup for better SEO and LLM discovery. Here's how to use all the features:

## 🔍 What's Included

### 1. Article Schema (Automatic)
- **Automatically applied** to all blog posts (`layout: post`)
- Includes: headline, description, author, publisher, dates, keywords, word count
- Optimized for Google's Article rich results

### 2. Breadcrumb Schema (Automatic)
- **Automatically applied** to all blog posts
- Creates navigation breadcrumbs: Home → Category → Article
- Helps with site structure understanding

### 3. Website Schema (Homepage)
- **Automatically applied** to homepage
- Includes site info, author details, search functionality
- Optimized for knowledge panels

### 4. FAQ Schema (Optional)
- **Manual activation** by adding `faq: true` to front matter
- Structure FAQs in your content using:
  ```markdown
  ## Q: Your question here?
  ## A: Your answer here.
  
  ## Q: Another question?
  ## A: Another answer.
  ```

### 5. LLM Discovery Meta Tags (Automatic)
- **Automatically applied** to all blog posts
- Includes AI-friendly metadata for better LLM training data discovery
- Content classification, reading time, expertise level

## 📝 How to Use FAQ Schema

Add this to your post's front matter:
```yaml
---
layout: post
title: "Your Post Title"
faq: true
# ... other front matter
---
```

Then structure FAQs in your content:
```markdown
# Your Post Content

## Q: What are multi-agent AI systems?
## A: Multi-agent AI systems are networks of autonomous agents that work together to solve complex problems.

## Q: How do they differ from single-agent systems?
## A: They can handle more complex tasks through collaboration and specialization.
```

## 🎯 LLM Optimization Features

### Content Classification
- Automatically tags content type, category, reading time
- Adds expertise level metadata
- Includes topic keywords for better discovery

### AI Training Friendly
- Clean content summaries
- Structured topic tags
- Reading difficulty indicators
- Content format specifications

## 🔧 Customization Options

### Adding Custom Schema
Create new schema types in `_includes/structured-data.html`:

```html
{% if page.custom_schema %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "YourSchemaType",
  // Your custom schema
}
</script>
{% endif %}
```

### Modifying Existing Schema
Edit `_includes/structured-data.html` to customize:
- Author information
- Publisher details
- Image specifications
- Content categorization

## 📊 Testing Your Structured Data

### Google Tools
- [Rich Results Test](https://search.google.com/test/rich-results)
- [Schema Markup Validator](https://validator.schema.org/)

### Other Tools
- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [Twitter Card Validator](https://cards-dev.twitter.com/validator)

## 🚀 Best Practices

### For Articles
- Always include meaningful descriptions
- Use relevant tags and categories
- Add alt text to images
- Keep titles under 60 characters

### For FAQs
- Use clear, natural language questions
- Provide comprehensive answers
- Structure logically (general to specific)
- Limit to 10-15 FAQ pairs per page

### For LLM Discovery
- Write clear, informative content
- Use consistent terminology
- Include relevant examples
- Structure content with clear headings

## 📈 Expected Benefits

### SEO Improvements
- Rich snippets in search results
- Better click-through rates
- Enhanced knowledge panel eligibility
- Improved site structure understanding

### LLM Discovery
- Better content indexing by AI systems
- Improved context understanding
- Enhanced training data quality
- Better AI-generated summaries

### User Experience
- More informative search results
- Better social media previews
- Clearer content categorization
- Enhanced accessibility