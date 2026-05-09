---
title: "Faculty Guide to AI Tools"
description: "Sign-up instructions for ChatGPT and Claude, data-privacy settings to check, and six research use cases with worked examples."
date: 2024-09-23
lastmod: 2026-05-09
weight: 210
toolkit_category: "teaching"
audience: ["faculty"]
availability: "public"
version: "September 2024; revised May 2026 (Eddie-reviewed 2026-05-09)"
---

A practical onboarding guide for faculty getting started with general-purpose AI tools — how to set up ChatGPT and Claude accounts, which data-privacy settings to check before uploading anything sensitive, and a starter set of research use cases.

The most current version is maintained at the persistent shortlink <https://bit.ly/Faculty_AI_Guide>; this page is the migrated copy.

## Faculty Retreat presentation

Polk's Fall 2024 Penn Law Pedagogy II talk on teaching with AI seeded much of what's now in the Toolkit. The slides remain available internally to Penn Carey Law faculty.

## Companion demos

The example prompts used in the retreat live on the [Teaching with Generative AI — Demos]({{< ref "/toolkit/teaching-demos" >}}) page. Use this guide for setup; use the Demos page for prompts you can adapt.

## Setting up paid accounts

Free tiers of ChatGPT and Claude work for basic experimentation. Paid tiers unlock larger context windows, better models, and the file-upload features most teaching tasks rely on.

**Check institutionally-provided access first.** Penn Carey Law faculty have institutional access to ChatGPT, Claude, and other AI tools through Penn-administered platforms. See the [AI Resources at Penn]({{< ref "/toolkit/ai-resources-at-penn" >}}) page before paying out of pocket — depending on your role, you may already have access at the school's expense.

### ChatGPT

1. Go to <https://chatgpt.com/>.
2. Create an account or log in.
3. Open account settings (from the profile/account menu) and choose a paid plan. Personal plans include Plus and Pro; Business and Enterprise are workspace plans.

Plus and Pro are for individuals (Pro adds higher usage limits). The Business plan (formerly "Team," renamed by OpenAI in August 2025) adds others to a shared workspace — useful for RAs or TAs. Business requires a minimum of two active accounts.

### Claude

1. Go to <https://claude.ai>.
2. Create an account or log in.
3. Open account settings and choose a paid plan.

Pro is the standard individual plan. Max (5x and 20x tiers) provides higher usage limits for heavy users who hit Pro caps. The Team plan adds others to a shared workspace; minimum is five active accounts.

## Keeping your data out of training

Privacy settings differ by platform — and they have changed multiple times since 2023. Always confirm current vendor policy and your account settings before uploading anything sensitive.

**Do not upload to consumer AI tools** (regardless of opt-out settings):

- Student educational records or graded work (FERPA)
- Unpublished co-authored work without all co-authors' consent
- IRB-regulated data or protected interview transcripts
- Material under NDA, embargo, or partner-confidentiality obligations
- Confidential committee or personnel information

For sensitive material that needs AI assistance, use the Penn-administered enterprise tools described on the [AI Resources at Penn]({{< ref "/toolkit/ai-resources-at-penn" >}}) page, or consult the Office of Audit, Compliance and Privacy and PCL ITS first.

### ChatGPT

On Plus and Pro plans: open account Settings → Data Controls and turn **off** the "Improve the model for everyone" toggle. With it off, your conversations and uploads should not feed model training. On Business, Enterprise, and Edu plans, OpenAI's default is not to train on workspace data; admins control settings rather than individual users. See OpenAI's [privacy policy](https://openai.com/policies/row-privacy-policy/) for current terms.

### Claude

As of late 2025, Anthropic's [consumer terms](https://www.anthropic.com/legal/consumer-terms) made training on conversations the **default for Free, Pro, and Max plans**, with an opt-out toggle. To opt out: Settings → Privacy → turn off "Help improve Claude." Even with the toggle off, Anthropic may use chats flagged for Trust & Safety review and any feedback you submit. The Team and Enterprise plans are governed by separate Commercial Terms and do not train on customer data by default.

This area changes frequently. Re-check the current vendor terms and your account settings before uploading anything you would not want surfaced.

## Six research use cases

A starter set of ways AI tools can help with research and academic writing. These work in ChatGPT or Claude — and most have direct analogues in legal-specific tools when the task is legal research rather than general scholarship (see the [Legal AI Tool Guide]({{< ref "/toolkit/legal-ai-tool-guide" >}})).

Verification, attribution, and any compliance obligations (FERPA, IRB, NDA, journal policy, co-author consent) remain with you. The tool is a draft assistant, not a publisher of record. Do not paste material covered by the do-not-upload list above into consumer AI tools.

1. **Literature summarization.** Feed articles or sources to the model and ask for a structured summary. Useful for sifting large volumes; verify quotes and citations against the source.
2. **Developing research questions.** Brainstorm angles, gaps in the literature, and counterarguments based on a topic you describe. The model is good at producing more directions than you'll use; the editorial judgment is yours.
3. **Citation-format help.** Generate citations in a target format (Bluebook, APA, MLA) or quickly check formatting on bibliographies and footnotes. **Always confirm the underlying citation against the source** — the model can format a hallucinated citation just as fluently as a real one.
4. **Critical analysis support.** Ask the model to critique a line of reasoning, surface counterarguments, or stress-test a methodology. Treat the output as a sparring partner, not a verdict.
5. **Note organization.** Feed in notes from various sources and ask the model to organize, find connections, or consolidate into a structured outline.
6. **Drafts from slides or transcripts.** If you have slides or a transcript of a talk, ask the model to convert them into a first draft of a paper or article. Helpful when the underlying content already exists and the friction is in re-expressing it as prose.

For more on getting good results from prompts, see the [Prompt Guide]({{< ref "/toolkit/prompt-guide" >}}).

## Status

Maintained for Penn Carey Law faculty. Vendor account flows, plan tiers, and data-handling defaults change frequently — confirm against current vendor pages before relying on the specifics here. Suggestions, corrections, and additions are welcome — email Polk Wagner at <pwagner@law.upenn.edu>.
