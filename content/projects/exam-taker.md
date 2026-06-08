---
title: "Exam Taker"
description: "The AI Final Exam Project — can current AI pass real Penn Carey Law finals when its work is graded blind, on the curve, by the faculty who wrote the exams? Wave 1 results are in."
date: 2026-05-09
lastmod: 2026-06-08
draft: false
type: project
cluster: "assessment-tools"
weight: 20
workstream: "02-assessment-tools/exam-taker"
status: active
pillar: ["research", "build"]
owner: ["Tulio Tagliaferri '27"]
---

Exam Taker is the test-subject side of the Lab's exam work. The pipeline puts a current AI model in the seat of a law student: it answers real Penn Carey Law finals — the same exams enrolled students sit for — and the answers go into the live grading stack to be scored blind, on the curve, by the faculty who wrote them.

Wave 1 ran during the Spring 2026 exam period and is now written up as a draft paper. A frontier model sat for eleven real PCL finals from across the curriculum — tax, remedies, constitutional law, criminal law, intellectual property, legislation, national security, international law, and a seminar. Each exam was answered twice under otherwise identical conditions: once on the model's training alone, and once with the course syllabus and an outline supplied. The answers were packaged to look like ordinary student submissions, given reserved examination numbers that could not collide with any real student, and graded blind by the faculty on their own rubrics. The class curve — recomputed with the AI answers removed — is the comparator.

## Read the work

- **[Draft paper — *Can AI Ace Your Exam? A Penn Law Experiment*](/papers/can-ai-ace-your-exam-2026-06.pdf)** (PDF) — the full Wave 1 write-up, a working draft not yet circulated.
- **[Extended abstract](/papers/can-ai-ace-your-exam-extended-abstract.pdf)** (PDF) — the three-page summary.
- **[Slides](/slides/can-ai-ace-your-exam/)** — the self-contained presentation deck ([PDF](/slides/can-ai-ace-your-exam/can-ai-ace-your-exam-slides.pdf)).

## What we found

Three findings organize the Wave 1 results.

- **The machine is competitive at the top, not merely passing.** Across the exams returned with grades it passed every one and sat at or above the class median on every one, ranked near the top of the class on most, and on a couple of exams outscored every enrolled student. The recurring profile: strong on coverage and issue-spotting, weaker on subtle argument and the connections drawn across issues.
- **Course materials help the multiple-choice components a great deal and the essays almost not at all.** The model's essay competence comes from its training, not from the supplied outline — so the bottom-line composite grade hides what the materials actually do. On at least one exam the materials helped the multiple-choice score and *hurt* the essay, nearly canceling in the average.
- **Faculty can sometimes tell — but mostly for reasons that won't last.** Most early detections rode on formatting artifacts — spacing, font, the reserved ID numbers — rather than the writing, and those are build-script bugs, fixable before the next wave. What survives the fix is harder to engineer away: the two independent answers to a single exam often read as though one hand wrote both, and the prose carries a thoroughness and polish that time-pressured student work does not.

## Why it matters

The empirical answer is yes — a machine that never took the course can write a top-of-the-class answer to the final. The harder question is the one this work puts to colleagues: if that's true, what is the final measuring? On this evidence, not mastery of the course so much as fluency in a genre — the time-limited issue-spotter and the doctrinal multiple-choice block — that current models have already mastered. The durable response is not to chase this year's model's weaknesses but to rethink the instrument: assess what we intrinsically value, assess the human-plus-AI system rather than the unaided human, and favor process over one-shot product.

## Behind the paper

A short companion essay, *Behind the Paper: AI-Assisted Research* (draft), reflects on how the project itself was run — a study of AI exam-taking conducted with AI as the apparatus, and what running it that way taught about trust, control, and keeping a reliable research record. **[Read it here](/papers/behind-the-paper-2026-06.pdf)** (PDF).

## What's next

Wave 2 (Fall 2026) is designed to close the leaks Wave 1 exposed: it fixes the formatting tells, adds models and repeated runs per exam, standardizes the course materials across exams, and turns detection into a measured task. It also widens faculty participation and sharpens the survey instrument that asks graders what surprised them.

## Status

Active. Wave 1 is complete and written up; Wave 2 design and faculty outreach are underway. Shares the underlying pipeline with the Exam Grader project.
