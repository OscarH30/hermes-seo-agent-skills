---
name: hermes-seo-strategy
description: "Use when validated SEO research or audit findings need prioritization, a content roadmap, site architecture, internal-link plan, programmatic SEO guardrails, schema specification, or a content brief. Trigger on 'SEO strategy,' 'content roadmap,' 'content brief,' 'topic cluster,' 'site architecture,' 'internal linking,' or 'programmatic SEO.' Turns evidence into an approved-ready plan; it never deploys changes."
license: MIT
metadata:
  author: Vindex Consulting
  version: 1.1.0
---

# Hermes SEO Strategy

Turn a bounded research or audit handoff into a practical plan. Do not create strategy from assumed keyword data, traffic, or customer proof.

## Boundary

- Preserve the source labels: OBSERVED, INFERRED, and GAP.
- Separate recommended work from implementation. CMS/code/schema/redirect/publishing actions require explicit human approval of the exact action.
- Do not create pages at scale or suggest automation until a small manual batch passes the unique-value test.
- Do not promise rankings, traffic, rich results, AI citations, or conversions.

## Method

1. Confirm business outcome, audience, geography, conversion action, horizon, resources, existing evidence, and the research provider. Prefer dated OpenSEO data when it is the approved/default source; preserve its query, locale, project, and metric context in the brief. Resolve or name missing decision-critical inputs.
2. Rank opportunities by business contribution, confidence, effort, dependency, and reversibility. If numerical scoring is requested, define inputs and calculate with a tool; never invent a score.
3. Assign a single primary intent and page job to each proposed asset. Avoid cannibalization.
4. Design hubs, spokes, navigation, URL direction, and contextual internal links only where they improve a user path and findability. Keep important pages reachable through ordinary navigation.
5. For structured data, specify only markup that matches visible content and official eligibility. A specification is not deployed markup.
6. For programmatic SEO, require differentiated, accurate value per page, preferably proprietary/product-derived data, an ownership model, and a small manually reviewed pilot.
7. Build one content brief per selected asset: audience; intent/query theme; page job; unique angle; source plan; business-owner or subject-matter-expert source/link opportunity; approved claims; claims requiring review; outline; internal links; conversion action; metadata direction; acceptance criteria; and approval gates.

## Deliverable

Return a prioritized roadmap plus content briefs for only the approved highest-value assets. Each roadmap row needs: opportunity; evidence; owner; dependency; effort; measurement; review point; and approval-required action.

Hand an approved brief and approved claims to `hermes-seo-copywriting`. Hand existing copy needing a refresh to `hermes-seo-editing`.