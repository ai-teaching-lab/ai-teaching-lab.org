---
title: "Building a Virtual TA for Your Course"
description: "Four ways to give your course a virtual teaching assistant — Claude Projects, PennChat Agents, the Lab's Heron Slackbot, or an externally-hosted tool — with access, cost, setup, and data tradeoffs for each."
date: 2024-09-01
lastmod: 2026-07-13
weight: 230
toolkit_category: "teaching"
audience: ["faculty"]
availability: "public"
version: "2024; revised July 2026"
---

A virtual TA is a course-specific AI assistant, grounded in your syllabus, readings, and framing, that students can ask questions of directly. As of mid-2026 there are four real ways to build one at Penn Carey Law, and they differ enough in access, cost, and setup that the right choice depends heavily on your course. This guide walks through all four.

This replaces the older version of this guide, which walked through building a ChatGPT Custom GPT. That path is no longer workable for reaching students: ChatGPT EDU remains available at Penn Carey Law, but only for faculty and staff — students are moving to Claude for 2026–27, so a Custom GPT has no student audience to reach on the institutional side. The four paths below are the current landscape.

## The four paths, at a glance

| Path | Who can reach it | Cost | Setup effort | Where materials go | Best for |
|---|---|---|---|---|---|
| **1. Claude.ai / Claude Projects** | Faculty (research account); 1Ls (2026–27 curriculum); other students only if they have their own Claude account | Free tier is limited; full Project functionality needs a paid plan (Pro/Max/Team/Enterprise) | Low — build a Project, write instructions, upload files. No code. | Anthropic's servers, under your (or each student's) individual account | A 1L course, or any course where you can assume students already have Claude |
| **2. PennChat Agents** | Everyone — faculty, staff, all student levels (pilot now, full launch expected after mid-August 2026) | Free during the pilot; credit-based system at full launch (pricing TBD) | Low-to-medium — rebuild your instructions/knowledge/tools as a PennChat Agent; no import from a Custom GPT | Penn's secure hosted environment (LibreChat), approved for most data up to High Risk | Broad reach across a whole class regardless of year, especially with sensitive course material |
| **3. Heron (Slack)** | Anyone in your course's Slack workspace — no Claude/ChatGPT/PennChat account needed | Real, ongoing: Pinecone, OpenAI embeddings, an LLM provider, and Railway hosting all bill separately; not free | Medium-to-high — fork a repo, configure a YAML file, stand up a Slack app, deploy, sync materials | Third-party infrastructure (Pinecone, OpenAI, your chosen LLM provider, Railway) — not a Penn-reviewed tool | Courses already living in Slack, or where you want page/slide/timestamp-level citations and are comfortable with (or have help for) the technical setup |
| **4. Externally-hosted** | Whoever you grant access to, on whatever platform you choose | Variable, and entirely on you | High — you're building and running a service | Wherever you host it — outside Penn's reviewed tools entirely | Narrow, low-risk use cases where you need something Penn's tools don't offer, and you have the technical support to run it |

Read the sections below before picking — the table compresses a lot of nuance, especially on path 1's sharing story and path 3's data posture.

## Path 1: Claude.ai and Claude Projects

**Who can access it.** Faculty have Claude access through research accounts today; a University-wide Claude agreement is expected around August 2026. For 2026–27, 1Ls receive Claude.ai (and likely Claude Code) as part of the 1L Legal Practice Skills curriculum. Outside that curriculum, Penn hasn't confirmed institutional Claude access for 2Ls, 3Ls, or LLMs — if you teach one of those courses, this path depends on students bringing their own Claude accounts.

**What it costs.** Claude's free tier is limited; full Project functionality requires a paid plan (Pro, Max, Team, or Enterprise). Whether the 1L curriculum's Claude access includes a paid tier for students, or what the university-wide agreement will look like, isn't confirmed in Penn's current tool documentation — **check with me before telling students what tier they'll have.**

**What setup involves.** Build a Claude Project: give it custom instructions (the same kind of briefing you'd write for a Custom GPT — audience, purpose, voice, scope, boundaries) and upload knowledge files (syllabus, readings, your own hypotheticals). No code, no hosting.

**The sharing story — read this before you promise anything.** Claude Projects live on an individual account. There is no button that publishes a Project to "everyone in my course" the way a GPT Store listing works. What's confirmed: a Project's files, instructions, and chat history follow your account across devices once you're logged in, and full functionality needs a paid plan; if your account is managed by an organization, that org's settings can affect access independently of Claude itself. What's *not* confirmed is whether Penn's forthcoming Claude deployment will provision projects as a shared, multi-user workspace — that would likely require a Team- or Enterprise-style account structure, and nothing in Penn's current tool documentation says whether that's how the rollout will work. **Treat any claim of a "shared class Project" as unverified until I've confirmed it.**

The workaround that works today regardless of how that resolves: build the Project as your own reference tool, then hand students the underlying pieces — your instructions and your (rights-cleared) materials — as something they paste into a Project on their *own* individual account. It's more setup per student than a single shared link, but it doesn't depend on a capability nobody has confirmed yet. **This is the most genuinely open question in this guide — I don't have a clean answer for class-wide Project sharing, and I'd rather say that plainly than invent a procedure.**

**What data can go in.** Follow the same do-not-upload list that applies to any AI knowledge base: no class recordings or transcripts of them (FERPA protects identifiable student speech), no student work or grading materials with names attached, no copyrighted casebook material beyond fair use, nothing under NDA or embargo. Penn's data-risk review anticipates Claude will be approved for Low and Moderate Risk data, but that approval is explicitly "to be confirmed at rollout" — don't put anything you'd classify as High Risk into a Project yet.

**When to pick this path.** Your course is a 1L course (where Claude access is a given via the curriculum), or you're comfortable requiring or assuming students already have paid Claude accounts. It's the lowest-effort path with the best model quality, but the honest access gap for non-1L courses is real — don't build this for a 2L seminar and assume every student can reach it.

## Path 2: PennChat Agents

**What PennChat is.** Penn's AI portal, hosted inside Penn's secure network, fronting both Anthropic's Claude and OpenAI's models in one interface. It runs on **LibreChat**, an open platform, and its **Agents** feature is the direct successor to ChatGPT's Custom GPTs: you give an agent standing instructions, attach knowledge files it searches across, and add tools (web search, a code interpreter, and OpenAPI-based actions — which tools are switched on can vary during the pilot).

**Who can access it.** Broader than any other path: faculty, staff, and students at every level, currently in a pilot running through roughly mid-August 2026, then moving to a full enterprise launch. This is the only path that reliably reaches 2Ls, 3Ls, and LLMs alongside 1Ls without depending on personal accounts.

**What it costs.** Free during the pilot. At full launch, PennChat moves to a credit-based usage system — the specific pricing isn't set yet, so don't commit to numbers with students until that's published.

**One access catch:** PennChat requires a connection to PennNet, AirPennNet, or the GlobalProtect VPN. A student working from off-campus without the VPN can't reach it — worth flagging if your course has remote components.

**What setup involves.** There's no one-click import from a ChatGPT Custom GPT — a Custom GPT is rebuilt, not migrated. Paste your instructions into a new PennChat agent, re-upload your knowledge files, and recreate any actions as PennChat tools. Every Custom GPT capability has a direct equivalent; it's manual, not automatic. Start from the Agent Builder in PennChat's side panel. (LibreChat's own agent documentation covers the mechanics in more depth than Penn-specific guidance does.)

**What data can go in.** This is PennChat's strongest point: it's approved for Low, Moderate, and most High Risk data (excluding SSNs and credit-card numbers, and avoiding identifiable PHI) — the broadest data approval of any general-purpose AI tool reviewed at Penn Carey Law, alongside Microsoft Copilot Chat. If your course materials include anything sensitive, this is the safest of the four paths.

**When to pick this path.** You want to reach your whole class regardless of year, your course touches data more sensitive than "public syllabus and readings," or you'd rather wait a few weeks for the full launch than build something today on infrastructure Penn hasn't reviewed. The tradeoff is the VPN requirement and a pilot timeline that isn't finished yet — this is a path for the fall semester, not necessarily for something you need live this month.

## Path 3: Heron (Slack)

**What it is.** Heron is the Lab's own open-source project: a RAG-powered Slack bot that answers student questions using your course materials. Students `@mention` the bot inside a Slack channel; it retrieves relevant passages from your materials (stored in a Pinecone vector database), and generates an answer with page citations via an LLM, called through LiteLLM so it can run on Anthropic, OpenAI, or Google models. It supports PDF, Word, Markdown, CSV, Google Docs, and Google Sheets, syncing automatically from a Google Drive folder. Markdown transcripts with `[HH:MM:SS]` timestamps get citations like "Class 5 Transcript, around the 7:00 mark" instead of page numbers, and slide decks cite by slide number.

The code is course-agnostic — one repository, and everything course-specific (bot name and personality, system prompts, topic categories) lives in a single `course_config.yaml` file you edit or generate with an interactive setup wizard.

**Who can access it.** Anyone who's a member of the Slack workspace and channel the bot is installed in — no Claude, ChatGPT, or PennChat account required at all. This is the lowest access barrier of the four paths if your course (or your students generally) already lives in Slack. DMs to the bot are admin-only; students interact by mentioning it in an allowed channel.

**What it costs — and this is the one path with real ongoing dollar cost.** Unlike the other three, Heron isn't a flat-rate or free institutional tool. You (or whoever administers it) need, and pay for, separately: a Pinecone account (vector database), an OpenAI API key (used for embeddings regardless of which model answers questions), an API key for at least one LLM provider (Anthropic, OpenAI, or Google), and hosting — the reference deployment runs on Railway. None of these costs are fixed numbers in the codebase; they scale with usage and current vendor pricing. **Get current quotes before committing to this path for a course of any size.**

**What setup involves.** Fork the repository, run the setup wizard (`python scripts/setup.py`) to generate your course config, create a Slack app with the required OAuth scopes and Socket Mode enabled, set the environment variables (Slack tokens, Pinecone key, OpenAI key, your chosen LLM provider key, a Google service-account credential for Drive sync), and deploy — the reference setup targets Railway. Then point it at a Google Drive folder of course materials and sync. Admin control happens through Slack slash commands (`status`, `health`, `sync`, `resync`, `model`, `export`, and more) restricted to a configured list of admin Slack user IDs; which channels the bot will respond in is also configured explicitly. This is a real technical setup — plan on doing it yourself if you're comfortable with Python and API credentials, or getting help from an RA or the Lab.

**What data can go in — and this needs a clear-eyed answer.** Whatever you put in the synced Google Drive folder gets sent to OpenAI (for embeddings) and stored in Pinecone (a third-party vector database), plus whichever LLM provider answers questions. This is **not** one of the tools Penn Law ITS or Penn ISC has reviewed and approved for a specific data-risk tier — it doesn't appear on Penn's list of endorsed AI tools at all. That means there's no institutional data classification covering it; you're relying on Pinecone's, OpenAI's, and your LLM provider's own commercial data-handling terms, which you should read before uploading anything. Treat this the same as any personal-account AI tool: fine for ordinary public course materials (syllabus, published readings, your own slides), and a bad fit for anything FERPA-protected, confidential, or above Low/Moderate risk. One more thing worth knowing: the bot logs student queries — a rolling window of the last 1,000 in an active file, with everything older archived indefinitely (deletable only via an explicit admin command) — so there's a standing record of which students asked what, unless you actively purge it.

**When to pick this path.** Your course already runs on Slack, you want citation precision (specific pages, slide numbers, or transcript timestamps) that a general chat tool won't give you out of the box, and you're willing to either do the setup yourself or line up help — and to budget for the ongoing API and hosting costs. It's the most capable and most customizable of the four, and also the most work.

## Path 4: Externally-hosted

**What this means practically.** Anything you build or run outside Penn's institutional systems and Penn-reviewed tool list — that includes a self-hosted Heron instance sitting on infrastructure Penn hasn't reviewed (see Path 3), but also covers other options: a custom web app calling an LLM API directly, a third-party AI-chatbot-builder SaaS product, or any other outside service you point students to.

**The tradeoff, honestly.** You get control and flexibility Penn's reviewed tools don't offer — pick any model or provider, customize without waiting on a pilot to finish, reach people without Penn credentials if that matters for your use case. You give up institutional review and support in exchange: nobody at Penn Law ITS has vetted the vendor's data-handling terms, there's no help desk if it breaks during the semester, and you (or whoever built it) are the ongoing maintainer for as long as it's live. A bot that goes dark mid-exam-prep because nobody was watching it is worse than no bot.

**When it's appropriate.** Low-risk, non-sensitive material, where you specifically need a capability none of the first three paths offer, and you or a collaborator can actually maintain a running service through the semester. Check the material you're putting in against Penn's data risk classification framework before you start — the same three tiers (Low, Moderate, High Risk) that govern every other tool on this page apply here too, except there's no vendor review to lean on. You're doing that assessment yourself.

**When it isn't.** Any FERPA-protected material, anything above Low/Moderate risk, or any course where you can't guarantee someone is maintaining the service for the term. If you're not sure which bucket you're in, that's the sign to use one of the first three paths instead.

## Which path should you pick?

Start with who needs to reach it. If it's just your own 1L section, Claude Projects is the least work and the best model quality — but confirm with me what tier of Claude access students actually have before you build around an assumption. If you need to reach 2Ls, 3Ls, or LLMs, or your materials are more sensitive than an ordinary reading list, wait for PennChat's full launch or use it now during the pilot. If you want Slack-native delivery and citation precision and are willing to pay for and maintain the infrastructure, Heron is the Lab's own answer to that. Reach for an externally-hosted option only when the first three genuinely don't cover what you need, and only for material that doesn't carry real data risk.

None of these are mutually exclusive with good pedagogy design — the [AI Syllabus Guide]({{< ref "/toolkit/syllabus-guide" >}}) covers setting expectations around a virtual TA the same way it covers AI use generally, and the do-not-upload guidance in this doc applies no matter which path you pick.

## Status

Maintained for the Penn Carey Law community. Vendor UI flows, pilot timelines, and data-approval terms change — verify against current Penn Law ITS and Penn ISC guidance before relying on the specifics here. Comments and corrections: <pwagner@law.upenn.edu>.
