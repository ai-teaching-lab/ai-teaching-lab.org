---
title: "Essay Creator"
description: "Generate assessment-grade essay exams — issue spotters and fact-pattern questions — with rubrics built for AI-assisted grading."
date: 2026-05-09
draft: false
type: project
cluster: "assessment-tools"
weight: 30
workstream: "02-assessment-tools/essay-creator"
status: active
pillar: ["build", "teach"]
owner: ["TBD"]
github: "pennai-law/essay-creator"
---

Essay Creator is the Lab's productized version of the `law-essay-generator` skill: a faculty-facing tool for drafting law-school essay exam questions — issue spotters and fact-pattern questions — that meet assessment-science quality standards out of the box.

It produces the question, the model answer, and the rubric in a single pass, with the rubric designed for AI-assisted grading on the back end.

## What we're doing

- Productize `law-essay-generator` into a faculty-facing tool: web interface, course presets, support for the major doctrinal courses (IP, contracts, torts, con law, civ pro).
- Enforce the assessment-science controls the underlying skill is built on: SOLO taxonomy layering, construct alignment to the course's actual coverage, distractor logic for issue-spotter sub-questions.
- Output rubrics that drop directly into Exam Grader — closing the loop between generation and grading.
- Build a small library of vetted exam patterns from participating faculty, so each new question starts from a known-good template rather than from scratch.

## Why this matters

The slow, painful part of law-school exam writing is producing fact patterns that surface the right issues at the right level of difficulty without leaking the answer. A tool that gets faculty to a credible first draft — with a rubric and a model answer attached — moves the bottleneck back to where it belongs: judgment, not drafting.

## Status

Active. The underlying `law-essay-generator` skill is in production use; productization as a Lab project is the next step.
