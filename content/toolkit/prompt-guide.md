---
title: "Prompt Guide & Scenarios"
description: "The Project's oldest publication. Introduces the CRAFTED prompting framework with three worked-through scenarios — Contracts class prep, Constitutional Law practice questions, CoCounsel research."
date: 2023-08-17
lastmod: 2026-05-08
weight: 40
toolkit_category: "core"
audience: ["faculty", "student"]
availability: "public"
version: "August 2023, revised for public release May 2026"
---

The Project's oldest publication and still in active use. The CRAFTED framework was first written in August 2023 for ChatGPT 3.5 / GPT-4 and CoCounsel; the principles apply across modern general-purpose AI assistants (ChatGPT, Claude) and legal-specific tools.

This is the first Toolkit document released publicly. The framework has held up across model generations because it focuses on what's durable about prompting — context, role, specificity, iteration — rather than what's transient about any particular model.

## Best Practices for Prompting AI

Using AI tools like ChatGPT, Claude, or CoCounsel can substantially extend your research and problem-solving capability as a lawyer. Getting the most out of each tool depends on prompting — crafting prompts that align with each tool's strengths while providing the context and guidance needed to manage its weaknesses.

The seven principles below form the acronym **CRAFTED**.

## The CRAFTED Framework

### C — Choosing the right tool

Different AI tools have different strengths. General-purpose models like ChatGPT and Claude shine at brainstorming, generating practice questions, drafting and revising, and contextual reasoning. Legal-specific tools like CoCounsel are tuned for legal research with curated legal corpora — useful when you need a more reliably grounded starting point on case law and statutes. Pick the tool that fits the task before you write the prompt.

### R — Relevance through context

Specify the case, concept, or material you're working with. Include relevant background. The model can't read your mind about which Hawkins case or which dormant Commerce Clause issue you mean — give it the context it needs to land in the right neighborhood.

### A — "Act as" prompting

Cast the model into a role: *"Acting as a contracts professor…"* or *"Acting as opposing counsel…"* Role prompts are a small piece of context that tightens output quality dramatically. The roles you can assign are essentially limitless.

### F — Fine-tune for specifics

If you want a particular kind of response — a story, a list of pros and cons, a numbered analysis, a memo, a hypothetical — say so explicitly in the prompt. The more specific the ask, the better the result.

### T — Thoughtful interaction

Use AI like an intellectual sparring partner, not like Google search. Initiate a back-and-forth — ask the model something, push back on its answer, ask follow-ups, refine. **Just because the tool says something that sounds plausible doesn't mean it's right.** Treat AI as a study partner with unlimited time, not as an oracle.

### E — Examples for clarity

Showing the model what you want is often more effective than describing it. Include sample outputs in the prompt to demonstrate format, tone, or depth. The model is good at pattern-matching against examples.

### D — Development through refinement

Iterate. If the response isn't quite what you need, adjust and rephrase. The first prompt rarely produces the best output. Continuous refinement — adding context, narrowing scope, asking for revisions — is how strong prompting actually works in practice.

## Quick takeaways

- Use "Act as" prompting to cast the model into a role.
- Be specific about the type of response you want.
- Always cross-check facts, citations, and legal claims against authoritative sources.
- Provide context and examples for best results.
- Iterate — the first prompt is a starting point, not the answer.

## Three worked scenarios

The three scenarios below trace common workflows for law students and faculty: studying a case, generating practice questions, and conducting legal research.

### Scenario 1 — Help me prepare for Contracts class

A common 1L workflow: a student is preparing for Contracts and wants to deepen their understanding of *Hawkins v. McGee*, a foundational case on expectation damages. ChatGPT or Claude works well for this kind of reasoning task.

**Prompt 1.** Establish context.

> I am studying for my 1L Contracts class. A key case for the day is *Hawkins v. McGee*.

The model returns a summary of the case — the hairy-hand surgery, expectation damages, the difference between value-as-promised and value-as-delivered. Useful as a baseline, but not yet pedagogically sharp.

**Important caveat:** Because plausibility is not the same as accuracy, always verify case citations and factual claims against authoritative sources (Westlaw, Lexis, the original casebook). Models can produce convincing-sounding but inaccurate descriptions, particularly for case names and procedural posture.

**Prompt 2.** Cast the model into a role.

> Pretend you are my law school professor.

The output shifts noticeably — the model adopts a more pedagogical voice, raising the kinds of questions a professor might press on. *"Act as"* is a small change with outsized effect.

**Prompt 3.** Ask for active engagement, not summary.

> As my professor, ask me 3 insightful questions about *Hawkins v. McGee* to test my conceptual understanding of the core contracts principles.

The model produces questions that target the doctrinal heart of the case — measure of damages, the difference between expectation and reliance, the policy reasons for protecting expectation. Asking for questions you have to answer beats asking for answers you have to read; this is where AI as study partner really earns its keep.

**Prompt 4.** Use the model's answers to check your own.

> Provide answers to these questions.

Sample answers help you see how to articulate the dispositive facts and main points. But — once again — cross-check against verified legal sources before relying on anything the model says about doctrine.

### Scenario 2 — Generate practice questions for Constitutional Law

Both students and faculty often want practice questions. AI is well-suited to this — it's a generative task, the model can adjust difficulty on request, and the output can be tuned with iteration.

**Prompt 1.** Generate short-answer questions.

> Pretend you are a constitutional law school professor and ask me three insightful questions about *Marbury v. Madison*.

The model produces three questions targeting different facets of the case — judicial review's textual basis, the political context of the decision, and the principle's modern reach. A starting point that the student can answer or that the professor can adapt.

**Prompt 2.** Generate a hypothetical fact pattern.

> Acting as a law school constitutional law professor, please create a short answer question using a hypothetical about the dormant Commerce Clause.

The model creates a hypothetical with a state regulation, an out-of-state interest, and the discrimination/burden analysis built in. Faculty can adapt the hypothetical, dial the difficulty up or down, or ask the model to generate variations.

**Prompt 3.** Generate multiple-choice questions.

> Please create a practice test with two multiple-choice questions, each with four answer choices and solutions (show the solutions separately under each question), about the Commerce Clause in the *Lochner* era, using the following cases: *Champion v. Ames* and *Hammer v. Dagenhart*.

For MCQ generation, **specificity is everything**. The more cases you name, the more concepts you target, the more constrained the answer choices, the better the output. Generic prompts produce generic questions; specific prompts produce questions that actually test what you want them to test.

### Scenario 3 — Research for a writing assignment

Picking the right tool matters most for research tasks, where reliability of citations is high-stakes. General-purpose models can hallucinate cases; tools with curated legal corpora are designed to mitigate this. CoCounsel offers less prompting flexibility than ChatGPT but is more reliable on case law.

**Prompt 1.** Establish the research question.

> What are some cases in which algorithms were found to be protected and not protected under section 230 of the Communications Decency Act?

CoCounsel returns an overview of relevant cases. The output is grounded in CoCounsel's legal corpus, which means citations are far more likely to be real.

**Prompt 2.** Refine.

> Narrow this by the cases that have been cited the most.

CoCounsel's strength is breadth across legal materials; iterative refinement narrows that breadth into something usable for a writing assignment.

**Notes on CoCounsel-style tools:**

- They produce overviews well, but case ordering may not match what Lexis or Westlaw would surface as most relevant — refine by jurisdiction, time period, or citation count.
- They are less flexible for creative prompting than ChatGPT or Claude, but compensate with a narrower, higher-quality corpus.
- They tend to be more transparent about limits — a useful property for legal research where confident-sounding wrong answers are particularly dangerous.

## Contact

The Prompt Guide is a Project document maintained by:

- Ambar Larancuent '26
- Hailey Parikh '27
- Polk Wagner — `pwagner@law.upenn.edu`

*With thanks to AI Law Lab alumni who contributed to the original guide:*

- Meghana Bhimarao '25 — AI Law Lab & CTIC Fellow
- Lakshmi Prakash '25 — AI Law Lab & CTIC Fellow
