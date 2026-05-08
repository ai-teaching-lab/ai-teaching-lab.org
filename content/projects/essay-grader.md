---
title: "AI Exam Taker / Essay Grader"
description: "Unified pipeline for studying AI as test-subject and AI as grader of law-school exams."
date: 2026-05-08
draft: false
type: project
workstream: "02-essay-grader"
status: active
pillar: ["research", "build"]
owner: ["Tulio Tagliaferri '27"]
github: "ai-teaching-lab/essay-grader"
---

A unified pipeline that puts AI on both sides of the law-school exam: AI as test-subject (taking exams written for human students) and AI as grader (scoring student essays against rubrics). Both questions are about AI's actual fluency with legal reasoning at exam scale, and they share most of the underlying infrastructure.

## What we're doing

- **Pipeline.** A single codebase that ingests exam files (fact patterns, MCQ banks, rubrics, model answers) and runs either side of the experiment — model-as-taker or model-as-grader.
- **Wave 2 plans.** Building on v1 results, the next round expands the model and faculty cohort and tightens the rubric/transcript pairing.
- **Faculty survey.** Structured feedback from participating faculty on what they observed, what surprised them, and how the AI grades compared with their own.

## Prior work this builds on

The current pipeline grows out of several earlier Lab efforts:

- **Literature review.** An annotated bibliography of AI-grading research, summarized in the Lab's "Exams / Student Evaluations" working notes.
- **Faculty demo (Fall 2024 Retreat).** Worked AI essay-grading demonstration using an actual IP exam, scoring rubric, and sample student answers.
- **Grading prototypes.** Earlier Python scripts for essay grading and accuracy evaluation, documented in the Lab's GitHub work.

## Why it matters

Exams are the highest-stakes pedagogical artifact in legal education. If AI can grade them reliably, that affects how faculty allocate time and how schools think about scale. If AI can take them well, that affects what we should be teaching law students to do in the first place.
