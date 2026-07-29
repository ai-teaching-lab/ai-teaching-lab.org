---
title: "MCQ Creator"
description: "Generate law-school multiple-choice questions with built-in distractor validation and psychometric quality controls."
date: 2026-05-09
draft: false
type: project
cluster: "assessment-tools"
weight: 40
workstream: "02-assessment-tools/mcq-creator"
status: active
pillar: ["build", "teach"]
owner: ["TBD"]
github: "pennai-law/mcq-creator"
---

MCQ Creator is the Project's productized version of the `law-mcq-generator` skill: a faculty-facing tool for drafting multiple-choice exam questions that pass the structural and psychometric quality checks the assessment literature actually expects.

The point is to make it cheap to produce *good* MCQs — narrative- or fact-pattern-based, with plausible distractors, single best answers, and no clueing — instead of the cookie-cutter items most generators produce.

## What we're doing

- Productize `law-mcq-generator` into a faculty-facing tool with course presets across IP, contracts, torts, con law, civ pro, and other doctrinal courses.
- Enforce the quality controls the underlying skill is built on: Haladyna-Downing-Rodriguez structural rules, distractor validation against the doctrine, single-best-answer guarantees, cognitive-taxonomy tagging so question difficulty is intentional.
- Support narrative and fact-pattern formats — not just one-line stems — so MCQs can probe the same kinds of reasoning a short essay would.
- Output question banks in formats that drop into the major exam-delivery platforms.

## Why this matters

MCQs are a powerful teaching and assessment tool when they're built well and a waste of student time when they aren't. The bar to *building them well* is high enough that most faculty just don't — which leaves a real assessment lever underused. This tool puts that lever in reach without asking faculty to learn the psychometric literature themselves.

## Status

Active. The underlying `law-mcq-generator` skill is in production use; productization as a standalone tool is the next step.
