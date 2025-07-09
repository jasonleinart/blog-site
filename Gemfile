source "https://rubygems.org"

# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!
gem "jekyll", "~> 3.8"

# Fixes `jekyll serve` in ruby 3
gem "webrick"

gem "jekyll-theme-hydejack", path: "./#jekyll-theme-hydejack"

# Core Jekyll dependencies for GitHub Pages compatibility
gem "kramdown-parser-gfm"
gem "liquid", "4.0.4"
gem "rouge", "3.26.0"
gem "terminal-table", "1.8.0"

group :jekyll_plugins do
  # Core Jekyll plugins
  gem "jekyll-include-cache"
  gem "jekyll-compose"
  gem "jekyll-feed"
  gem "jekyll-sitemap"
  gem "jekyll-paginate"
  gem "jekyll-redirect-from"
  gem "jekyll-seo-tag"
  gem "jekyll-last-modified-at"
  
  # GitHub Pages standard plugins
  gem "jekyll-default-layout"
  gem "jekyll-optional-front-matter"
  gem "jekyll-readme-index"
  gem "jekyll-titles-from-headings"
  gem "jekyll-relative-links"
  gem "jekyll-avatar"
  gem "jekyll-coffeescript"
  gem "jekyll-commonmark-ghpages"
  gem "jekyll-gist"
  gem "jekyll-github-metadata"
  gem "jekyll-mentions"
  gem "jekyll-theme-primer"
  gem "jemoji"
end

gem 'wdm' if Gem.win_platform?
gem "tzinfo-data" if Gem.win_platform?