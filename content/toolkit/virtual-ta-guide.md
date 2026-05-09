---
title: "Creating a Virtual TA with Custom GPTs"
description: "A step-by-step guide to building a course-specific virtual teaching assistant, using the Lab's IP TA as a template."
date: 2024-09-01
lastmod: 2026-05-09
weight: 230
toolkit_category: "teaching"
audience: ["faculty"]
availability: "internal"
version: "2024; revised for migration May 2026"
---

A walkthrough for faculty who want to build a course-specific virtual teaching assistant using OpenAI's Custom GPTs (or the equivalent in Claude Projects, Gemini Gems, or whatever your platform of the moment offers). The example throughout is the Lab's IP TA — a study-and-review assistant for Intro to Intellectual Property at Penn Carey Law.

This is the conceptual precursor to the Lab's **Heron** virtual-TA Slackbot project. The Custom GPT path is a low-effort starting point: no code, no hosting, no integration work. You drop in syllabus materials, write a few paragraphs of instructions, and the platform handles the rest.

## Before you start

Custom GPTs are useful when:

- You want students to be able to ask questions about course-specific material — your syllabus, your slides, your hypotheticals — and get answers grounded in *your* framing of the doctrine.
- You don't need analytics, persistent memory across students, or integration with another platform.
- You're comfortable with students using the AI tool's web interface rather than having the TA embedded somewhere (Canvas, Slack, your course site).

If you need any of those things, a Custom GPT is the wrong tool — look at Heron-style implementations or build something custom.

## Seven steps

### 1. Navigate to the GPT editor

Go to [chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor). You need a paid ChatGPT account (Plus, Team, or Enterprise) to publish a Custom GPT. From the editor, open MyGPTs from the top-right menu.

### 2. Create a new GPT

Click the plus sign to start a new GPT.

### 3. Open the Configure tab

Two tabs appear at the top left — Create and Configure. Skip the Create tab (it's a guided builder that walks you through the same fields conversationally) and go directly to Configure. You'll have more control and a cleaner result.

### 4. Fill in the configuration

This is where the real work happens. The fields are:

#### Name

Pick something descriptive. The Lab's IP TA is called "Intro to IP TA" — students see the name in the chat header, so make it obvious what course it serves.

#### Description

One sentence on what the GPT is for. The IP TA's description: *"Study and Grading assistant for IP Law at Penn Carey Law."*

#### Instructions

This is the most important field. Treat it as a full briefing for a smart but inexperienced TA who has never seen your course before. Cover:

- **Audience.** Who is this for? "Students in the Intro to Intellectual Property class at the University of Pennsylvania Carey Law School."
- **Purpose.** What does the TA do? Study help? Practice questions? Grading rubric explanations? Be specific. Multiple purposes are fine — just enumerate them.
- **Voice and depth.** How should the TA respond? "Detailed but concise explanations, enriched with real-life case examples. Encourages understanding through Q&A; helps students grasp key takeaways without overwhelming them."
- **Subject scope.** What content domain? For the IP TA, the syllabus modules: patents, trademarks, copyrights, trade secrets, and basic IP-law principles.
- **Boundaries.** What should the TA *not* do? Common ones: don't write papers, don't answer take-home exam questions, don't substitute for the assigned reading.

The IP TA's full instructions live in the Lab's internal materials — ask if you'd like to see them as a starting template.

#### Conversation starters

Pre-written prompts that appear as buttons when a student opens the GPT. They serve two purposes — orienting the student to what the TA can do, and seeding the conversation in productive directions. A few examples from the IP TA:

- *Welcome:* "Hello! I'm [Name], your virtual TA for Intro to Intellectual Property. I'm here to help you understand topics like patents, copyrights, and trademarks. Ask me about key concepts, definitions, and examples."
- *Guidance:* "When asking about a specific concept, use keywords and I'll do my best to clarify. For example: 'What is fair use?'"
- *Learning objectives:* "This course covers intellectual property types, the purpose of IP rights, and the basics of protecting creations and inventions under IP law."

Three or four starters is plenty. More clutters the interface.

#### Knowledge

Upload course materials — syllabus, key textbook chapters, lecture slides, practice questions, hypotheticals, and (if available) cleaned-up transcripts of class recordings. The GPT uses retrieval over these documents to ground answers in your course rather than the model's general training.

A few practical notes:

- PDFs and Word docs work well. Slides export to PDF cleanly.
- The retrieval is imperfect — if a student asks about a doctrine you covered in class but not in any uploaded document, the GPT will fall back on the model's general knowledge of IP law, which may or may not match your framing. Upload broadly.
- Keep an eye on file count and size. Performance degrades with very large knowledge bases.

#### Capabilities

Check Web Search, DALL-E Image Generation, and Code Interpreter & Data Analysis. Web Search is the most useful — it lets the TA pull recent cases and developments. The other two are rarely used in a doctrinal-law TA but don't hurt to enable.

#### Actions

Skip this. Actions are for connecting the GPT to external APIs (authentication layers, custom databases). For a study TA, you don't need it.

### 5. Publish

Click Create at the top right. Choose visibility — "Only me," "Anyone with a link," or (for Team/Enterprise accounts) "My workspace." Link-based sharing is the practical default for a course TA.

### 6. Tune the response style

Once the GPT is live, open it and have a few real conversations. Adjust the tone in the prompting interface — *"Be more concise."* *"Use fewer bullet points."* *"Always cite the case name when discussing doctrine."* These adjustments fold back into the GPT's instructions automatically.

A few tone defaults that work well for a law-school TA:

- Approachable, clear, professional.
- Match the complexity students are expected to handle. Don't dumb it down; don't pile on jargon.
- End answers with an invitation to follow up: *"If this wasn't clear or you'd like a deeper explanation, ask me to elaborate."*

### 7. Test and iterate

Simulate the questions students are likely to ask. Stress-test the boundaries — try to get the TA to write a paper, or answer an exam question, or hallucinate a case. Where it fails, tighten the instructions. Where it succeeds, note what's working.

Update knowledge as the course evolves. New cases, new hypotheticals, revised slides — re-upload and the TA stays current.

## Privacy note

When you upload documents to a Custom GPT, OpenAI does not use those documents for model training. They remain within the context of your GPT. This is a meaningful distinction from pasting content directly into a regular ChatGPT conversation, where data handling depends on your account settings. Confirm OpenAI's current data-handling terms before uploading anything sensitive — the policy is stable but the wording shifts periodically.

## Status

Maintained internally for the Penn Carey Law community. Public release pending review.
