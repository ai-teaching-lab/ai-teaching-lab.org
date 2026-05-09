---
title: "Heron — Virtual TA Slackbot"
description: "Pedagogy infrastructure: a Slackbot that serves as a 24/7 virtual teaching assistant for course use."
date: 2026-05-07
lastmod: 2026-05-09
draft: false
type: project
cluster: "teaching-tools"
workstream: "03-teaching-tools/heron"
status: active
pillar: ["build", "teach"]
owner: ["TBD"]
github: "ai-teaching-lab/heron"
---

Heron is a virtual TA Slackbot for law school courses. Backed by retrieval over course materials — syllabus, readings, lecture transcripts — Heron answers student questions, points to relevant materials, and escalates to faculty when something needs human judgment.

## Why this matters

A first-line TA available at 3am the night before an exam, in office-hours queue when the human TAs are saturated, in study-group conversations when no one's quite sure of the answer. Pedagogy infrastructure: students learn from interacting with Heron; faculty save synchronous-TA bandwidth for higher-leverage work.

## Status

v1 prototype lives at `~/code/ip_slackbot` — built around an IP-class corpus and used to validate the retrieval pattern. Lab-owned v2 is the next major build, scoped to generalize the architecture across courses.
