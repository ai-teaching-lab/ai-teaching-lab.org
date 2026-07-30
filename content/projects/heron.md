---
title: "Heron — A Course-Bounded Virtual TA"
description: "A virtual teaching-assistant chatbot bound to one course's materials: it answers students in Slack from the assigned readings, with citations. Plus the argument that faculty should consider building these to govern the AI students already use. Spring 2026 results and a draft paper."
date: 2026-05-07
lastmod: 2026-06-13
draft: false
cluster: "teaching-tools"
weight: 40
workstream: "03-teaching-tools/heron"
status: active
pillar: ["build", "teach"]
owner: ["R. Polk Wagner"]
---

**Heron is a virtual teaching assistant for a single course — a chatbot students talk to in Slack.** Ask it about a case, a doctrine, or the week's reading, and it answers from *that course's own materials* — the assigned readings, slides, and class transcripts — citing the exact page or timestamp so a student can check the source, and saying so plainly when the materials don't cover the question. It is named for Heron of Alexandria, the first-century engineer of steam toys and automatic doors: a fitting namesake for a course about invention.

R. Polk Wagner built Heron and ran it in his Intellectual Property course at Penn Carey Law in the spring of 2026. Heron itself is one working example; the general idea it argues for is the point. Faculty should consider building *course-bounded, cite-or-refuse* teaching assistants — bound to one course's materials, citing what they can and declining what they can't — not to beat general chatbots like ChatGPT on answer quality (the evidence says they won't), but to *govern* a tool students already use, pointing it at the course, the source, and the exam.

> **Where Heron fits in the Project.** Heron is the *teaching* side of the Project's work — the always-on assistant that helps students learn *during* the course. Its siblings work the *assessment* side: [Exam Taker](/projects/exam-taker/) puts an AI in the student's seat to test what finals actually measure, and [Exam Grader](/projects/exam-grader/) helps faculty grade.

## Read the work

- **[Draft paper — *Heron in the Classroom: A Faculty-Built AI Teaching Assistant for Legal Education*](/papers/heron-in-the-classroom-2026-06.pdf)** (PDF) — the full write-up: the design, the one-semester case study, the cost and skill it actually takes, and a replication path. An early working draft, not yet circulated.

The paper's abstract:

> The faculty debate over whether to permit AI in our courses is, I think, largely over, settled less by argument than by two facts: a frontier model now passes real law-school finals, and in a blinded study law professors preferred an AI tutor's answers to a colleague's three times in four. The obvious response — ground the model in the course's own materials — does not, the evidence suggests, make its answers any better. The case for a course-bounded teaching assistant therefore rests not on accuracy but on governance: answering from this course's materials, citing a page a student can open, refusing when the readings cannot support an answer, and going dark for the exam. I make two claims. The first is that faculty should consider building such tools; the second, more often doubted, is that one faculty member can. I built and ran Heron in my Intellectual Property course in the spring of 2026 — alone, in about ten hours of setup, at under a dollar per enrolled student. The tool sat nearly unused until the week before the exam, when thirty-three students put close to a thousand questions to it and the course's own materials answered 96.6% of them. One semester cannot prove a design philosophy; it can show what one looks like, and that building it is now within reach.

## The design: six principles

Heron runs on six choices, each answering to a pedagogical commitment rather than to accuracy.

- **The corpus is the course, and nothing else.** Retrieval is limited to the assigned materials — no open web — so the tool becomes a way *into* the readings rather than a way around them.
- **Cite, or say you can't.** Every retrieval is scored against a similarity threshold; clear it and Heron answers from the passages and cites them, fall below it and it discloses, plainly, that the question is out of scope.
- **A citation you can open.** Pinpoint references — a page, a slide number, a transcript timestamp — so the student can verify against the source, not a summary of it.
- **The bot sounds like the course.** Aligned to the course's voice and to its standard for a complete answer, the rule applied rather than the black-letter rule recited.
- **It goes dark for the exam.** A configured cutoff takes the tool offline during the examination period — for everyone, the instructor included.
- **When it doesn't know, it says so — plainly.** No upbeat hedge, no confident bluff, never a citation invented to fill a gap.

## What one semester showed

One course, one instructor, one semester — a case study, not a test. Heron was live all term but sat nearly untouched until the last week before the exam, when students arrived all at once: in the six days before the final, **33 students (43% of the class) put close to a thousand questions to Heron**. The course's own materials answered **96.6%** of them; the rest fell through to a labeled general-knowledge disclaimer. Use was conversational, not transactional — **86% of questions came inside back-and-forth threads** — and the exam-period cutoff engaged on schedule, taking the tool offline when the course needed it gone. The cite-or-refuse design held; what it could not do was make students reach for the tool across the term rather than only in the week it could help them most.

## Why it matters: governance, not accuracy

The capability question is settled. A frontier model already passes real Penn Carey Law finals when graded blind (see the Project's [Exam Taker](/projects/exam-taker/) project), and in a blinded study this spring, law professors more often preferred an AI tutor's short answers to a fellow professor's. And yet grounding a capable model in a fixed course corpus does not reliably make its answers *better* — in both that tutoring study and the exam work, the grounded system did not outperform the stock one.

So the case for a course-bounded teaching assistant cannot rest on better answers. It rests on governance: answering from *this* course in *this* course's frame, citing a page a student can actually open and check, sending students back to the source, and going silent for the exam. None of that is about being right more often. It is the pedagogical work a polished, ungrounded chatbot quietly skips — and it is exactly what a general chatbot, by design, leaves ungoverned.

## Build it yourself

The second claim is the one most colleagues doubt until they see it done: a single faculty member, without an engineering team, can now build and run such a thing. Heron is five commodity pieces wired together — Slack, a managed vector database, an embedding model, a multi-provider LLM layer, and a one-process host — with most of the implementation code written by an AI coding assistant under the author's direction and review. The cost was about **ten hours** for the first working version, **under an hour a week** to run, and **under a dollar per enrolled student** for the semester. The skill required is real but bounded: comfort at the command line, environment variables, a little Git, and the patience to read an error message without flinching.

The code is open source and built to be forked: **[github.com/pennai-law/heron](https://github.com/pennai-law/heron)**. Point it at your own course's materials, set a handful of configuration choices, and deploy.

## Status

Active. Deployed in a Spring 2026 Intellectual Property course and written up as an early draft paper. The implementation is one example, built one way; a lab-owned, course-general v2 — generalizing the architecture across courses — is the next major build.
