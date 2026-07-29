---
title: "Course Materials"
description: "An extraction primitive: turn the messy artifacts of a real course — PDFs, slide decks, casebook excerpts, syllabi — into clean structured text that downstream tools can use."
date: 2026-05-08
lastmod: 2026-05-09
draft: false
type: project
cluster: "teaching-tools"
weight: 10
workstream: "03-teaching-tools/course-materials"
status: active
pillar: ["build", "teach"]
owner: ["TBD"]
github: "pennai-law/course-materials"
---

Course Materials is the extraction primitive that sits underneath the rest of the Teaching Tools cluster. The job is narrow and load-bearing: take the messy artifacts of a real course — PDFs, slide decks, casebook excerpts, syllabi, lecture transcripts — and turn them into clean, structured text that other tools can consume reliably.

It's not a casebook-creation project. It's the layer that makes casebook creation, virtual-TA retrieval, exam generation, and class-simulation tooling possible in the first place.

## What we're doing

- Maintain the `materials-md` extraction toolchain — a deterministic CLI that converts PDFs, DOCX, PPTX, and HTML to clean markdown.
- Handle the cases that matter for legal materials: scanned casebook pages, court opinions in messy formats, slide decks with speaker notes, structured tables of cases.
- Ship the output in a shape downstream Project tools can use directly — Heron's retrieval, exam-grader's reference texts, class-simulations' problem stems, casebook-builder's source corpus.

## Why this matters

Every other Teaching Tool either works or fails on the quality of its input. Hallucinations in a virtual TA, miscalibrated exam grading, drift in a class simulation — most of these trace back to dirty source text. Getting the primitive right once means the rest of the cluster gets cleaner inputs by default.

## Status

Active. The CLI is in production use across Polk's own teaching workflow and across other Project skills. Next work: harden the casebook-extraction path against scanned-page edge cases and document the output schema so our other projects can integrate against a stable contract.
