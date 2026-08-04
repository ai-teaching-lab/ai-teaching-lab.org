---
title: "Building a Virtual TA for Your Course"
description: "Heron plus the design choices behind course-bounded virtual teaching assistants: corpus, citations, refusals, student expectations, privacy, maintenance, and assessment fit."
date: 2024-09-01
lastmod: 2026-08-04
weight: 140
toolkit_category: "teaching"
toolkit_group: "teaching"
audience: ["faculty"]
availability: "public"
version: "2024; revised August 2026"
---

The Project's model for a virtual TA is [Heron]({{< relref "/projects/heron" >}}): a course-bounded assistant that answers students in Slack from one course's materials, cites the source it used, and says plainly when the materials do not answer the question.

This guide is Heron plus the additional design thoughts faculty need before adapting the pattern. For current Penn-specific options for deploying a course assistant, use the [AI Resources Portal](https://resources.pennai.law/). Platform access, account eligibility, data approvals, and setup steps change too quickly to duplicate here.

## The basic idea

A virtual TA should not be a general chatbot with a course label on it. It should be bounded by the course.

Heron's design is the reference point:

- The corpus is the course's own materials.
- The assistant answers only when retrieved course materials support an answer.
- Answers cite the page, slide, or transcript timestamp students can check.
- Unsupported questions are refused or labeled as outside the course materials.
- The assistant follows the professor's framing and course rules.
- It can be taken offline when the exam period begins.

The point is governance, not magic accuracy. Students already have access to general AI tools. A course-bounded assistant gives them a better path: back to the course, back to the source, and back to the professor's expectations.

## What Heron showed

Heron ran in a Spring 2026 Intellectual Property course. The write-up is linked from the [Heron project page]({{< relref "/projects/heron" >}}).

The short version:

- Students mostly used it near the exam, not steadily through the semester.
- The useful design move was not that the bot was always right.
- The useful design move was that it was constrained: cite, or say it could not answer from the course materials.
- Students could check the answer against a page, slide, or transcript timestamp.
- The tool could be turned off for the exam.

That makes Heron a model for faculty design even when the implementation changes.

## Start with the teaching purpose

Do not build a virtual TA because the technology is available. Build one only if it solves a course problem.

Good uses include:

- answering recurring course-logistics questions from the syllabus;
- pointing students to the right reading, slide, class note, or transcript segment;
- generating practice questions from assigned materials;
- asking follow-up questions instead of giving final answers;
- helping students review doctrine after they have done the reading;
- giving students a low-stakes place to test explanations before office hours.

Poor uses include:

- writing answers to graded work;
- substituting for assigned reading;
- giving legal advice;
- answering beyond the materials provided;
- handling confidential, FERPA-protected, client, clinic, or exam material without approval.

## Define the corpus

The first design choice is what the assistant is allowed to know.

Good source sets include:

- the syllabus and assignment schedule;
- professor-created slides and handouts;
- public cases, statutes, and regulations;
- professor-written hypotheticals and practice problems;
- course FAQs;
- transcripts or notes only if they are approved for the tool and appropriate for student use;
- model instructions for how the assistant should answer student questions.

Be cautious with:

- copyrighted casebook material;
- class recordings or transcripts that include identifiable student participation;
- student work;
- grading rubrics, model answers, or exam questions;
- client, clinic, personnel, or committee materials.

If the source material is sensitive, the platform decision matters. Use the [AI Resources Portal](https://resources.pennai.law/) for current data-policy and platform guidance.

## Use cite-or-refuse as the default

The safest course-assistant pattern is cite-or-refuse.

Useful instruction:

> Answer from the course materials provided. When you answer, identify the specific reading, page, slide, class session, or transcript timestamp that supports the answer. If the course materials do not support an answer, say that plainly. Do not invent citations, readings, slide numbers, transcript timestamps, or class discussions.

This does not make the answer perfect. It does make the answer inspectable. That is the main pedagogical advantage over a general chatbot.

## Write the assistant's boundaries

A good course assistant instruction should state:

1. the course and audience;
2. the materials the assistant may rely on;
3. the kinds of questions it may answer;
4. the kinds of questions it must refuse;
5. how it should cite or point back to materials;
6. what it should say when it does not know;
7. whether it should give direct answers, hints, or Socratic questions;
8. whether and when it should go offline.

Starter language:

> You are a course assistant for [course name]. Use only the syllabus, assigned readings, slides, handouts, transcripts, and other course materials I provide. Help students understand the course materials by asking clarifying questions, pointing them to relevant sources, and explaining concepts at the level appropriate for this course. Do not write answers to graded assignments, do not predict grades, do not provide legal advice, and do not answer questions that require information outside the course materials unless you clearly label the answer as general background.

## Tell students what the assistant is for

Students should know that the assistant supports learning but does not replace the professor, assigned materials, class discussion, office hours, or course rules.

Sample student-facing language:

> This course includes an AI course assistant. The assistant is a study tool grounded in course materials. It can help you locate readings, generate practice questions, and think through concepts after you have completed the reading. It may be wrong, incomplete, or too general. You remain responsible for the assigned materials, class discussion, and all submitted work. Do not use the assistant to write answers to graded assignments unless an assignment expressly permits that use.

If students may use the assistant for submitted work, say exactly how and when disclosure is required. The [AI Syllabus Guide]({{< relref "syllabus-guide" >}}) has copyable language.

## Plan the exam cutoff

Heron's exam cutoff is a design choice worth preserving. If the assistant helps students study before an exam but should not be available during the exam, build that into the course plan.

Say:

- when the assistant will go offline;
- whether old conversations remain available;
- whether the cutoff applies to the professor and teaching team too;
- how the exam instructions describe AI use;
- what students should do if the assistant gives conflicting information before the cutoff.

The exam rule should still be stated separately in the exam instructions.

## Decide who maintains it

A virtual TA is not finished when it launches. Someone needs to maintain it during the semester.

Maintenance work includes:

- updating materials when the syllabus changes;
- removing old drafts or superseded readings;
- checking whether common answers are accurate;
- reviewing failed or confusing interactions if logs are available and appropriate;
- telling students when the assistant's boundaries change;
- shutting it down or archiving it after the course ends.

If no one can maintain it, keep the assistant narrow or do not deploy it.

## Match the assistant to assessment design

| Course design | Good fit | Caution |
| --- | --- | --- |
| Traditional lecture course | Practice questions, doctrine review, syllabus logistics, exam study support before the cutoff | Keep exam rules separate and explicit. |
| Seminar | Research-process questions, source-trail support, topic brainstorming | Do not let the assistant become an undisclosed writing partner. |
| Writing or skills course | Revision prompts, client-communication critique, simulation practice | Preserve first-pass student analysis when that is the learning goal. |
| Clinic | Internal training on public or approved materials | Do not include client or confidential facts unless approved. |

## Related resources

- [Heron project page]({{< relref "/projects/heron" >}}) — implementation, paper, and case-study results.
- [AI Syllabus Guide]({{< relref "syllabus-guide" >}}) — course-policy language.
- [Teaching Examples and AI Demos]({{< relref "teaching-demos" >}}) — starter course-assistant prompt.
- [AI Resources Portal](https://resources.pennai.law/) — current platform, access, setup, and data-policy guidance.

## Status

Maintained for Penn Carey Law faculty.
