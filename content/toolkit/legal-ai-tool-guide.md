---
title: "Legal AI Tool Guide"
description: "Categorized overview of seven legal AI tool families plus the major general-purpose tools — built for faculty trying to make sense of the field."
date: 2025-07-01
lastmod: 2026-05-09
weight: 30
toolkit_category: "core"
audience: ["faculty"]
availability: "public"
version: "July 2025; revised May 2026"
---

A categorized overview of the legal AI landscape — seven domain-specific tool families plus the major general-purpose models (ChatGPT, Claude, Gemini). Built for faculty who want to understand what's out there without having to track every product launch.

The goal is orientation, not endorsement. We name representative tools in each category to make the categories concrete; we don't recommend specific products, and we don't try to be exhaustive. The legal AI market is moving fast — vendors get acquired, products get rebranded (Casetext was acquired by Thomson Reuters in 2023 and CoCounsel is now a Thomson Reuters product; LexisNexis replaced Lexis+ AI with Lexis+ with Protégé in 2026), and new entrants appear every few months. Treat any specific tool name here as illustrative.

## Two layers: general-purpose and legal-specific

Generative AI tools used in legal work fall into two broad layers:

- **General-purpose models** — ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google). These are the foundation models. They're strong at reasoning, drafting, brainstorming, and code, but they're not designed around legal corpora and they generate plausible-sounding citations that don't exist.
- **Legal-specific tools** — products built on top of general-purpose models, often with managed legal databases, retrieval pipelines that surface real authority, and workflow features tailored to lawyers. CoCounsel, Lexis+ with Protégé, Harvey, Spellbook, Relativity, and others fall here.

A typical lawyer or law student today uses both. General-purpose tools are better for thinking out loud and drafting; legal-specific tools are better when citation accuracy matters.

## Seven categories of legal-specific AI

Apart from the general-purpose models, the legal AI market sorts roughly into seven categories.

### 1. Legal research and document production

AI-powered platforms that search legal databases, produce research memos, summarize cases, and draft documents. These are the tools competing most directly with traditional Westlaw and Lexis workflows — and in fact the major incumbents have built their own AI products into those platforms.

### 2. Contract management

Tools for contract drafting, review, redlining, clause libraries, and lifecycle management. Used heavily in transactional practice; many integrate directly with Word.

### 3. Electronic discovery

E-discovery has used machine learning for more than a decade. The current generation of tools applies generative AI to document summarization, issue coding, privilege review, and drafting work product from review sets.

### 4. Practice management

Time tracking, billing, client intake, matter management. AI features here mostly automate administrative overhead so lawyers can spend more time on substantive work.

### 5. Domain-specific platforms

Tools built for a particular practice area — patents, trademarks, immigration, personal injury, M&A diligence. These trade breadth for depth, often with templates, checklists, and outputs tailored to the conventions of one field.

### 6. Lawyer search and access

Consumer-facing platforms that match clients with lawyers, route routine legal questions, or attempt to provide direct legal services. A more experimental category, with regulatory uncertainty around the unauthorized-practice-of-law line.

### 7. Regulatory compliance

Tools that monitor regulatory changes, map obligations across jurisdictions, and help in-house teams keep compliance programs current.

## Representative tools in each category

The table below names a few representative tools per category. Inclusion is illustrative — these are tools we have seen mentioned often enough to be worth knowing about, not endorsements.

| Category | Representative tools |
|---|---|
| Legal research and document production | **CoCounsel** (Thomson Reuters; originally a Casetext product, acquired 2023) and **Lexis+ with Protégé** (LexisNexis) — major legal-AI products from the two incumbents. Both handle research memos, document review, deposition prep, and contract analysis. On Westlaw, the platform now ships as **Westlaw Advantage** (which folds in CoCounsel); on Lexis, "Lexis+ AI" was replaced by **Lexis+ with Protégé** in 2026. **Harvey** — a copilot for lawyers across drafting, research, and analysis tasks, with publicized adoption at several AmLaw firms. |
| Contract management | **Ironclad** — contract lifecycle management used by in-house teams. **Spellbook** — contract review and clause suggestions inside Microsoft Word. |
| Electronic discovery | **Relativity** — established e-discovery platform; AI features build on capabilities from its 2021 Text IQ acquisition for sensitive-data detection. **Everlaw AI Assistant** — generative AI for document summarization, issue coding, sentiment analysis, and draft argument generation in discovery review. |
| Practice management | **Clio Duo** — AI-assisted billing, time tracking, and matter summaries inside the Clio practice-management platform. **MyCase IQ** — comparable AI features for solo and small-firm practice management. |
| Domain-specific | **PatentPal** — generates patent diagrams and specification text from claim sets, aimed at patent attorneys and agents. **Lex Machina** — litigation analytics built on PACER and state-court records, used heavily in IP and complex-commercial practice. |
| Lawyer search and access | **DoNotPay** — consumer service marketed as a "robot lawyer" for routine matters such as contesting tickets. The FTC filed a complaint against DoNotPay in September 2024 over its "AI lawyer" marketing claims, and finalized a consent order in February 2025 imposing $193,000 in monetary relief and barring the company from advertising AI legal services as a substitute for a human lawyer without supporting evidence. The category as a whole faces ongoing regulatory questions about unauthorized practice. |
| Regulatory compliance | **Red Marker** and **Regology** — regulatory-change monitoring and compliance-process management for organizations operating across multiple regimes. |
| General-purpose AI (separate layer, not one of the seven legal-specific categories) | **ChatGPT** (OpenAI), **Claude** (Anthropic), **Gemini** (Google). All three offer free tiers and paid tiers with stronger models. Penn Carey Law has provided ChatGPT Edu accounts to incoming first-year students, 1L teaching assistants, and Littleton/legal-writing fellows since Fall 2025. **Always verify factual and citation outputs against authoritative sources** — general-purpose models generate plausible-sounding but incorrect case law. |

## What faculty should take from this

A few points worth keeping in mind as you talk with students or colleagues about legal AI tools:

- **The category matters more than the product.** Tools come and go; the categories above describe stable functions that lawyers will keep needing. If a student understands what "legal research AI" or "contract review AI" is for, they can evaluate any new entrant.
- **General-purpose vs. legal-specific is the most important distinction.** Use general-purpose tools for thinking, drafting, and brainstorming. Use legal-specific tools when grounded citations matter. Confusing the two is the most common source of bad outputs.
- **Citation hallucination is the central failure mode.** Without retrieval over a real corpus, general-purpose models routinely produce convincing-sounding case citations that don't exist. Legal-specific tools mitigate this with retrieval over real corpora, but they don't eliminate it. Verify before you rely.
- **The market appears to be consolidating around the incumbents.** Westlaw and Lexis have both shipped major AI products (CoCounsel and Lexis+ with Protégé respectively). Several independent legal-AI startups have been acquired or absorbed. Expect this to continue, though foundation-model providers moving directly into the legal stack may complicate the picture.

## Contact

The Legal AI Tool Guide is a Lab document maintained by:

- Ambar Larancuent '26
- Hailey Parikh '27
- Polk Wagner — `pwagner@law.upenn.edu`

*With thanks to AI Law Lab alumni who contributed to the original guide:*

- Meghana Bhimarao '25 — AI Law Lab & CTIC Fellow
- Lakshmi Prakash '25 — AI Law Lab & CTIC Fellow

## Status

Maintained for the Penn Carey Law community. Comments, corrections, and product updates welcome — email Polk Wagner at <pwagner@law.upenn.edu>.
