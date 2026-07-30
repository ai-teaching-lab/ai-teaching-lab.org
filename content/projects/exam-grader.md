---
title: "Exam Grader"
description: "Calibration-based AI grading for law-school essay exams — deployed against Polk's Spring 2026 IP class."
date: 2026-05-09
lastmod: 2026-06-08
draft: false
cluster: "assessment-tools"
weight: 10
workstream: "02-assessment-tools/exam-grader"
status: active
pillar: ["build", "research"]
owner: ["Tulio Tagliaferri '27"]
---

Exam Grader is the Project's calibration-based grading tool for law-school essay exams. The model doesn't grade in a vacuum — it grades against a calibration set the faculty member has already scored, learning the rubric from worked examples before scoring the rest of the stack.

The first real deployment is the Spring 2026 Intellectual Property final exam at Penn Carey Law.

## What we're doing

- Build the calibration pipeline: ingest the rubric, the model answer, and the faculty-graded calibration set; learn the scoring pattern; apply it to the rest of the exams.
- Surface the model's reasoning per essay — not just a score, but the rubric points it credited and the rationale.
- Run paired grading on the Spring 2026 IP final: AI scores in parallel with the faculty grader, with the differences flagged for review.
- Track agreement, surface the cases where AI and human disagree, and feed those back into the calibration design.

## Why this matters

Law-school exam grading is the highest-friction step in the teaching cycle and the place where consistency matters most. A grader that anchors to a faculty member's own calibration set — rather than to a generic rubric — is the version most likely to actually fit how that faculty grades. If it works, it changes how faculty allocate time at the most labor-intensive moment of the semester.

## Status

Active build. Shares the underlying pipeline with the Exam Taker project. The first deployment is the Spring 2026 IP final at Penn Carey Law; results feed Wave 2 of the AI Final Exam Project.
