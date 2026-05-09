---
title: "Exam Taker"
description: "Wave 2 of the AI Final Exam Project — putting current models against real Penn Carey Law finals and reporting what they can and can't do."
date: 2026-05-09
draft: false
type: project
cluster: "assessment-tools"
weight: 20
workstream: "02-assessment-tools/exam-taker"
status: active
pillar: ["research", "build"]
owner: ["Tulio Tagliaferri '27"]
github: "ai-teaching-lab/exam-taker"
---

Exam Taker is the test-subject side of the Lab's exam work. The pipeline runs current AI models against real law-school finals — the same exams Penn Carey Law students sit for — and produces structured reports comparing model performance against the faculty's grading rubric.

This is Wave 2 of the AI Final Exam Project. Wave 1, run during Spring 2026, covered roughly ten Penn Carey Law professors' final exams; Wave 2 widens the model cohort, tightens the rubric pairing, and reports back to participating faculty in a form they can use.

## What we're doing

- Run a wider slate of models against the Spring 2026 PCL final-exam set — frontier models from each major lab, plus a handful of smaller open-weight comparisons.
- Pair every transcript with the faculty rubric and a faculty grader's score, so we can report agreement and disagreement at the rubric-point level rather than at the headline-grade level.
- Survey participating faculty: what surprised them, where the AI did better than expected, where it failed, and what they'd want to know next.
- Publish the aggregate findings — including model-by-model and doctrine-by-doctrine breakdowns — so the legal-education community can see what current models actually do on real law-school work.

## Why this matters

Faculty intuitions about AI exam-taking are everywhere on the spectrum, and most of them are based on demos rather than data. The point of this work is to put the question on empirical footing: against an actual final, against an actual rubric, scored by the actual faculty, what do current models do? The answer affects how faculty design exams, how schools think about academic integrity, and what the next generation of legal-education research should ask.

## Status

Active. Wave 1 results are in hand; Wave 2 design and faculty outreach are underway. Shares the underlying pipeline with the Exam Grader project.
