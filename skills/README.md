# Hermes SEO Skills

These are the canonical Vindex source files for the Hermes SEO Agent training pack. They are knowledge skills: they research, analyze, plan, draft, and edit, but do not require credentials or take external actions.

Install all six through the project-local copies in `.agents/skills/` after cloning the published repository and running `hermes skills trust .` from its root.

Skill sequence:

1. `hermes-seo-orchestrator` selects the smallest appropriate stage and preserves the evidence trail.
2. `hermes-seo-research` establishes demand, intent, SERP, competitor, and customer-language evidence.
3. `hermes-seo-audit` identifies observed technical, on-page, internal-link, and structured-data gaps.
4. `hermes-seo-strategy` turns validated findings into architecture, prioritized roadmaps, and content briefs.
5. `hermes-seo-copywriting` drafts a selected, approved brief.
6. `hermes-seo-editing` improves existing copy without inventing claims.

All skills use OBSERVED, INFERRED, and GAP labels. Publishing, CMS changes, analytics/Search Console changes, account connections, spending, outreach, and external sharing require explicit human approval.