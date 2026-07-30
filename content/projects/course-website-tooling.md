---
title: "Course-Website Tooling"
description: "Generalize the Legal Education at Model Velocity microsite into reusable templates the Project and others can deploy quickly."
date: 2026-05-09
draft: false
cluster: "teaching-tools"
weight: 30
workstream: "03-teaching-tools/course-website-tooling"
status: planning
pillar: ["build", "teach"]
owner: ["TBD"]
github: "pennai-law/course-website-tooling"
---

Course-Website Tooling is the build layer underneath the Project's Training Materials work. It generalizes the Legal Education at Model Velocity microsite — the four-module microsite, the cloned-voice podcast pipeline, the NotebookLM audio overview, the auto-generated PDF summaries — into reusable templates that future training packages and course microsites can deploy without rebuilding from scratch.

Each new training package the Project ships should be a thin instantiation of this layer, not a one-off project.

## What we're doing

- Templatize the Legal Education microsite: parameterized module structure, reusable navigation, audio embed pattern, PDF summary generator, integrated NotebookLM overview slot.
- Standardize the production pipeline — content goes in as markdown, audio is generated via the cloned-voice and NotebookLM workflows, the site is built and deployed in a single pass.
- Ship the templates as open-source so other faculty can run their own course microsites without reinventing the architecture.

## Why this matters

The Legal Education microsite proved out a content + audio + microsite formula that works. The cost of producing the next package is mostly determined by how much of that formula has to be rebuilt versus how much is already in template form. This project is the difference between producing one nice microsite a year and producing five.

## Status

Planning. Rides under the Training Materials project as the build layer that lets Training scale.
