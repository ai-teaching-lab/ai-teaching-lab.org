---
title: "Prompt Guide & Scenarios"
description: "A durable prompting framework for law-school and legal-work tasks, with worked examples for class preparation, practice questions, and legal research."
date: 2023-08-17
lastmod: 2026-08-04
weight: 210
toolkit_category: "core"
toolkit_group: "methods"
audience: ["faculty", "student"]
availability: "public"
version: "August 2023; revised August 2026"
---

Prompting is the practice of giving an AI system the context, role, task, format, examples, and constraints it needs to produce useful output. The details of particular tools change; the basic prompting habits below remain useful across general-purpose AI assistants and legal-specific tools.

Course-specific rules control student use. If a syllabus, assignment, exam instruction, clinic rule, journal rule, or supervisor instruction limits AI use, follow that rule.

## Best Practices for Prompting AI

Good prompts do five things:

1. State the task plainly.
2. Give relevant context.
3. Identify the audience and purpose.
4. Specify the output format.
5. Tell the model what not to do.

For legal work, add a sixth habit: require verification. Ask the model to distinguish source-supported claims from assumptions, and check anything you plan to rely on.

## A prompting checklist

### Choose the right tool

Use a tool that fits the task. General-purpose assistants are useful for brainstorming, drafting, explanation, and revision. Legal-specific tools are better when the task depends on legal databases or source-grounded research. For current Penn Carey Law access and setup, use the [AI Resources Portal](https://resources.pennai.law/).

### Add relevant context

Give the model the facts, course, jurisdiction, assignment goal, audience, and constraints. A prompt without context produces generic output.

### Assign a useful role when needed

Assign a role when it helps: professor, skeptical reader, senior associate, student study partner, or judge. The role should match the task and audience.

### Specify the output

Ask for the exact format you need: table, checklist, outline, questions, memo structure, or critique. Include length, tone, and exclusions.

### Iterate and question the result

Treat the first answer as a draft. Ask follow-up questions, request alternatives, and press for uncertainty. Iteration usually matters more than a perfect first prompt.

### Give examples when format matters

Show the model what good output looks like when format or tone matters. Examples often work better than abstract instructions.

### Refine your own work

Use the model to refine your own work, not to replace your judgment. For student work, check whether the course permits the use and whether disclosure is required.

## Quick takeaways

- Bring your own sources when accuracy matters.
- Ask for uncertainty and missing information.
- Require the model to separate law, facts, assumptions, and suggestions.
- Verify every authority, quotation, and factual claim.
- Start a new chat when a long thread starts drifting.
- Do not upload material that the tool is not approved to receive.

## Three worked scenarios

### Scenario 1 — Prepare for Contracts class without replacing the reading

A student has read *Hawkins v. McGee* and wants to test understanding.

> I am preparing for a 1L Contracts class. I have already read *Hawkins v. McGee* and taken notes. Ask me five questions that test whether I understand expectation damages. Do not give me the answers first. After I answer, tell me what I got right, what I missed, and what part of the case I should review.

Useful follow-up:

> Now give me one new hypothetical that changes the facts in a way that affects the damages analysis. Make the answer turn on a fact that a beginning student might miss.

### Scenario 2 — Generate practice questions for Constitutional Law

A professor wants low-stakes practice questions from assigned materials.

> I am teaching Constitutional Law. Based on the readings I provide, create five multiple-choice questions that test judicial review and the reasoning in *Marbury v. Madison*. Each question should have four answer choices, one best answer, and a short explanation. Do not test doctrine outside the materials I provide.

Useful follow-up:

> Make two questions easier, two medium, and one difficult. Label the learning objective for each question.

### Scenario 3 — Build a legal research plan with source verification

A student or faculty member needs a research starting point, not a finished answer.

> I am researching whether [specific legal issue] has been addressed in [jurisdiction/context]. Create a research plan. Give me search terms, likely sources, and categories of authority to check. If you name a case, statute, article, or factual claim, label it "unverified" unless you can point me to a source I can independently inspect.

Useful follow-up:

> Turn this into a source-checking table with columns for source, proposition, database or location to check, verification status, and notes.

## Status

Maintained for the Penn Carey Law community.
