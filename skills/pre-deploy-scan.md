# Skill — pre-deploy-scan

- **ID:** `4fe7be2e-00ab-480b-b63b-bbbac2abb67c`
- **Created:** 2026-06-08T06:18:10Z

## Description

Fast (<30s) pre-flight security + SEO scan that runs before any user-facing deliverable is marked in_review. Covers exposed secrets, missing RLS, unauthenticated write paths, env/credential patterns, and SEO basics (title, meta description, sitemap, aria-labels). Outputs a structured pass|warn|block verdict. Extends security-review-checklist (which runs later, at in_review → done).

## Owned by

- [`deployment-engineer`](../agents/deployment-engineer.md)

## Config

```json
{}
```
