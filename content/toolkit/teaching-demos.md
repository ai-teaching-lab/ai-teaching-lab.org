---
title: "Teaching with Generative AI — Demos"
description: "Two-level demonstration prompts from the Fall 2024 Faculty Retreat — image generation, class scripting, hypothetical creation, Virtual TA setup, essay grading."
date: 2024-09-25
lastmod: 2026-05-09
weight: 220
toolkit_category: "teaching"
audience: ["faculty"]
availability: "public"
version: "Fall 2024; revised May 2026 (Eddie-reviewed 2026-05-09)"
---

The example prompts used in Polk's Fall 2024 Faculty Retreat session on teaching with generative AI. Each prompt is reproduced as it was given to the model so you can adapt the wording to your own course.

The prompts work in ChatGPT and Claude, and most carry over with minor tweaks to whatever general-purpose model you prefer. Pair this page with the [Faculty Guide to AI Tools]({{< ref "/toolkit/faculty-guide" >}}) for setup and account guidance.

The materials below assume you've uploaded the relevant readings into the model session. ChatGPT and Claude both accept PDF and DOCX uploads — free tiers have stricter daily limits than paid tiers, so a class session's worth of materials usually requires a paid plan. The demos use the IP class fair-use cases as the running example; substitute your own materials for your course.

**Before uploading:** confirm you have the right to share the materials with the AI tool, and don't upload student work or anything covered by FERPA, NDA, or partner-confidentiality. See the [Faculty Guide to AI Tools]({{< ref "/toolkit/faculty-guide" >}}) for the full do-not-upload list.

## Level 1 — Common teaching tasks

### Use AI to create images for slides

After uploading the readings, ask the model to generate a domain-relevant image:

> These readings are for a class session in Intellectual Property at Penn Law. Please create a photo-realistic image of a science laboratory as suggested by the *Texaco* case, with binders of *Journal of Catalysis* and other scientific journal articles on shelves and lab tables throughout. Show a scientist operating a photocopier in the corner, making copies of an article from one of those journals for her colleagues.

Useful when you want a slide visual that ties directly to the doctrine. Image generation is a strength of these tools; the output quality is improving steadily.

### Use AI to script or outline a class

> These readings are for a class session in Intellectual Property at Penn Law. I need to teach all four of these cases in an 80-minute class. Create a suggested outline for the class, with suggested timing, including some time for Q&A. Treat the cases in the order in which they appear in the readings, but spend more time on the *Campbell* and *Warhol* cases.

Good for first drafts. Adjust the timing pass yourself — the model tends to be optimistic about how much fits in an 80-minute block.

### Use AI to create slides

> These readings are for a class session in Intellectual Property at Penn Law. Please create a set of about 4–5 slides concerning the *Google* case only. Instead of using many bullet points on the slides, ask a few questions per slide highlighting the important issues.

The "questions, not bullets" framing is the key move here — it shifts the slide design toward a Socratic frame rather than information dump.

### Use AI to create hypotheticals

> Give me three hypothetical examples I can use at the end of the class to illustrate the theoretical tensions in the law's development in this area.

Faculty often find this the highest-value single use — generating fresh hypotheticals that surface a doctrine's open questions.

## Level 2 — Higher-leverage tasks

### Use AI to create practice problems

> Now create a practice problem based on this class session that the students can work on outside of class. Make it substantively complex and write it so that the students will need to grapple with some of the open questions and ambiguities in the law after the Supreme Court's decision in *Warhol*. Design it so that students will need to write about one to two pages to answer it.

Then, in the same session:

> Now create a sample answer, and an explanation of why that answer is a good one.

The pair — problem plus reasoned model answer — gives faculty a starting point for a graded assignment without writing both pieces from scratch.

### Use AI as a Virtual TA

Create a Custom GPT (ChatGPT Plus or higher) or a Claude Project (available on Claude's free plan) seeded with your slides and readings. The system prompt below works as a starting point:

> You are a helpful and friendly teaching assistant for Introduction to Intellectual Property. Your task is to provide answers to student inquiries based on the materials given only. Be sure to only use these materials as sources for your answers to the student inquiries, and tell the student if a question cannot be answered using these materials (and you can then use your best efforts to answer it anyway). When answering, provide a reference to the reading materials and/or slides whenever possible.

For a deeper walkthrough of the Custom GPT setup process, see [Creating a Virtual TA with Custom GPTs]({{< ref "/toolkit/virtual-ta-guide" >}}).

### Use AI to evaluate ("grade") essays

The Lab's Spring 2024 IP exam was the testbed for the Lab's first AI-grading work. The exercise paired:

- An essay question (the IP exam fact pattern)
- A scoring rubric and answer key
- A blank output template for AI-generated grades
- Student answers (one or many)

Ask the model to score each answer against the rubric, returning structured output that maps to the template.

This work later became the basis for the Lab's [Exam Grader]({{< ref "/projects/exam-grader" >}}) project — a calibration-based grading pipeline currently in production use.

## Status

Maintained for Penn Carey Law faculty. Demos may be updated as new model capabilities open new pedagogical patterns. Email Polk Wagner at <pwagner@law.upenn.edu> with suggestions.
