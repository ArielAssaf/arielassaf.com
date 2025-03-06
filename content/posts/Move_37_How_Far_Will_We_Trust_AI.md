---
title: "Setting Up DNS for GitHub Pages"
date: "2025-03-06"
draft: false
tags: ["github", "dns", "web", "tutorial"]
---

Today I set up my personal website using GitHub Pages with a custom domain. Here's what I learned about configuring DNS records properly:

## Required DNS Records

To point your custom domain to GitHub Pages, you need to configure these DNS records:

### A Records
You need four A records pointing to GitHub's IP addresses:
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

### CNAME Record
For the www subdomain, add a CNAME record:
```
www -> yourusername.github.io
```

## Tips for DNS Configuration

1. Remove any conflicting DNS records
2. Be patient - DNS changes can take up to 24 hours to propagate
3. Use tools like [dnschecker.org](https://dnschecker.org) to verify your DNS settings

## GitHub Pages Setup

In your repository settings:
1. Enable GitHub Pages
2. Add your custom domain
3. Wait for DNS verification
4. Enable HTTPS (available after DNS is verified)

Stay tuned for more updates as I continue building and improving this site!
