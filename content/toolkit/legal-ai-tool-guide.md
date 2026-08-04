---
title: "Legal AI Tool Guide"
description: "A category-based guide to legal AI tools, focused on what different tool families do and how to evaluate outputs."
date: 2025-07-01
lastmod: 2026-08-04
weight: 220
toolkit_category: "core"
toolkit_group: "methods"
audience: ["faculty", "student"]
availability: "public"
version: "July 2025; revised August 2026"
---

This guide helps faculty and students evaluate legal AI by task, evidence base, and verification obligation. It is not an access guide, product catalogue, or endorsement list. For current Penn Carey Law access, account setup, and product-specific guidance, use the [AI Resources Portal](https://resources.pennai.law/).

The useful question is not "which product is best?" It is: what task is this tool performing, what material can it draw on, what can go wrong, and what must a lawyer verify before relying on the output?

## Start with the task

Legal AI is most useful when the task is clear. Match the tool and the level of supervision to the work, rather than treating every AI system as a substitute for legal research or legal judgment.

### Legal research and authority analysis

**Use it for:** finding leads, comparing authorities, organizing a research trail, and testing possible lines of analysis.

**Watch for:** invented or incomplete authority, a citation that does not support the proposition offered, overlooked jurisdictional limits, outdated law, and missing contrary authority.

**Minimum check:** confirm the authority, proposition, context, jurisdiction, currency, and contrary authority. Read the source; do not rely on a model's description of it.

### Analysis of supplied documents and document sets

**Use it for:** summarizing, comparing, clustering, surfacing questions, and preparing a first-pass issue list from documents you have supplied.

**Watch for:** missing documents, quotations that omit context, unsupported factual inferences, and material that should be handled under separate confidentiality or privilege rules.

**Minimum check:** confirm document coverage, quoted language, missing context, and the factual basis for every consequential inference.

### Drafting, revision, and adversarial testing

**Use it for:** creating a first draft, improving organization, proposing alternatives, identifying ambiguities, and stress-testing an argument.

**Watch for:** unsupported legal or factual assertions, generic language that does not fit the matter, and a polished answer that conceals weak analysis.

**Minimum check:** identify every proposition that needs support, check the underlying sources, and retain your own legal judgment about the argument and its consequences.

### Workflow, triage, and recurring operational work

**Use it for:** sorting, routing, labeling, and surfacing patterns in recurring work.

**Watch for:** a workflow that misses relevant material, treats an uncertain pattern as a decision, or obscures a choice with legal consequences.

**Minimum check:** test what the workflow leaves out, review decisions with legal consequences, and make sure the human reviewer can see the material and reasoning behind a result.

## Ask what the tool knows

Before evaluating an answer, ask what material the system can actually draw on.

- **Model knowledge** is an answer generated from learned patterns, without the source set being visible to the user.
- **Retrieved sources** are materials selected from a defined collection to help generate an answer.
- **Supplied sources** are documents the user provides to the system for a particular task.
- **Workflow or organizational data** is matter, firm, or other operational information that informs an answer or action.

Source availability and source reliability are different questions. A linked citation, retrieved document, or confident answer supplies evidence to inspect; it does not prove that the conclusion is correct.

Retrieval can improve grounding by bringing relevant material into the task. It does not eliminate errors in retrieval, interpretation, or synthesis. The same is true when a tool works from a document set: the answer may be useful, but the reader must still determine whether the material is complete, relevant, and accurately understood.

## Verify the output as a lawyer would

Use this workflow before relying on AI-generated legal work:

1. Identify the legal propositions that matter.
2. Open and read the cited or supplied source.
3. Check authority, proposition, context, jurisdiction, and currency.
4. Look for missing facts, contrary authority, and unsupported inferences.
5. Make and own the professional judgment.

This approach reflects the professional responsibilities that surround AI use, including competence, confidentiality, supervision, communication, and fees. It is educational guidance, not jurisdiction-specific ethics advice. A useful output can save time, but it does not transfer responsibility from the lawyer or student using it.

## Teaching activities

Faculty can teach legal-AI literacy without running a product demonstration or requiring students to use AI. These activities make verification and professional judgment visible.

### Compare answers in a doctrinal course

**Course setting:** a doctrinal course introducing a rule or line of cases.

**Learning objective:** distinguish a fluent answer from a source-supported legal analysis.

**Student task:** compare a general answer and a source-grounded answer to the same question. Identify each unsupported proposition and explain whether either response supports its conclusion.

**Debrief:** ask what changed when the students could inspect sources, and what they would need to verify before relying on either answer.

### Build a verified research trail in legal research or writing

**Course setting:** legal research, legal writing, or an assignment requiring authority research.

**Learning objective:** turn an AI answer into a research process rather than treating it as research results.

**Student task:** begin with an AI answer, locate every cited source, state the proposition each source actually supports, identify what is missing, and produce a corrected research plan.

**Debrief:** ask which errors were visible only after opening the authority and which research steps the original answer skipped.

### Audit a method in a seminar

**Course setting:** an upper-level seminar with a research memo or paper.

**Learning objective:** evaluate the method and evidence behind a conclusion, not just the conclusion itself.

**Student task:** assess an AI-generated research memo by separating its research question, source base, legal propositions, assumptions, counterarguments, and conclusions.

**Debrief:** ask which parts of the memo are supported, which parts are inference, and how the student would revise the research method before using the memo in a paper.

### Supervise a first-pass issue list in a transactional or clinic course

**Course setting:** a transactional, drafting, or clinic course using a supplied document set.

**Learning objective:** practice supervising a first-pass work product.

**Student task:** use a supplied document set to generate an issue list, identify the additional facts and governing law needed, and state what a supervising lawyer would verify before advising a client.

**Debrief:** ask which issues were useful leads, which required more factual development, and what should never be inferred from silence in the documents.

For prompting and iteration techniques, see the [Prompt Guide & Scenarios]({{< relref "prompt-guide" >}}). For choices about course and assignment rules, see the [AI Syllabus Guide]({{< relref "syllabus-guide" >}}).

## Related resources

- [Prompt Guide & Scenarios]({{< relref "prompt-guide" >}}) — prompting, iteration, and verification habits.
- [AI Syllabus Guide]({{< relref "syllabus-guide" >}}) — course and assignment AI rules.
- [AI Use Policy Templates]({{< relref "policy-templates" >}}) — attribution and disclosure models for writing-intensive work.
- [Best Practices for AI in Legal Education]({{< relref "best-practices" >}}) — course-design principles.
- [AI Resources Portal](https://resources.pennai.law/) — current Penn Carey Law access, setup, and product-specific guidance.

## Further reading

- [ABA Formal Opinion 512: Generative Artificial Intelligence Tools](https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf)
- [Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools](https://law.stanford.edu/wp-content/uploads/2024/05/Legal_RAG_Hallucinations.pdf)
- [AI-Powered Lawyering: AI Reasoning Models, Retrieval Augmented Generation, and the Future of Legal Practice](https://papers.ssrn.com/abstract=5162111)
- [GenAI in Legal Education: A Practical Guide for Professors and Students](https://www.cali.org/sites/default/files/GenAIinLegalEducationMunsterman-May2026.pdf)

## Acknowledgment

With thanks to the AI Law Lab alumni who contributed to the original guide:

- Meghana Bhimarao '25 — AI Law Lab & CTIC Fellow
- Lakshmi Prakash '25 — AI Law Lab & CTIC Fellow

## Status

Maintained for the Penn Carey Law community.
