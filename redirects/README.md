# Redirects

This folder contains redirect files for old URLs that need to be redirected to new locations.

## Structure

Each redirect follows the pattern: `redirects/[old-path]/index.md`

For example:
- `redirects/thoughts/blog/index.md` redirects `/thoughts/blog/` to `/blog/`

## Adding New Redirects

1. Create the directory structure matching the old URL path
2. Add an `index.md` file with the redirect configuration:

```yaml
---
redirect_to: /new-url/
---
```

## Current Redirects

- `/thoughts/blog/` → `/blog/`

## How It Works

The `jekyll-redirect-from` plugin automatically generates redirect pages from these files, creating proper 301 redirects that are SEO-friendly.
