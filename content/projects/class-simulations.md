---
title: "Class Simulations"
description: "AI-driven simulations built around the actual class problems law students work through each week — starting with patent law."
date: 2026-05-08
lastmod: 2026-05-09
draft: false
cluster: "teaching-tools"
weight: 50
workstream: "03-teaching-tools/class-simulations"
status: planning
pillar: ["build", "research"]
owner: ["TBD"]
github: "pennai-law/class-simulations"
---

Class Simulations builds AI-driven exercises around the class problems students already work through each week. Instead of generic role-plays, the simulations attach to the specific hypotheticals a course assigns — so the AI counterparty pushes back the way the doctrine actually pushes back, and students get to see their reasoning tested against something that has to follow the same rules they do.

Patent law is the starting domain. The doctrine is bounded, the documents are highly structured, and a weekly problem set already exists to bolt the simulations onto.

## What we're doing

- Build simulations around the patent class's existing weekly problems — claim drafting, prior-art arguments, prosecution exchanges, opposition workflows.
- Treat the patent class as a research test bed: same students, same problems, paired with and without the simulation layer, with feedback collected each week.
- Generalize what works. Once the patent simulations are stable, port the pattern to other classes — torts, contracts, civ pro — where structured weekly problems exist.
- Ship the tooling open-source so other faculty can drop their own problem sets in.

## Why this matters

Class problems are where doctrine becomes operational. A simulation that engages with a specific problem — rather than a generic fact pattern — gives students the chance to argue against an interlocutor that knows the rules and won't let them skate. That's the part of practice that's hardest to rehearse in a 100-person classroom.

## Status

Scoped for summer 2026. The patent class is the first deployment target; build deferred until after the assessment-tools and core teaching-tools projects have momentum.
