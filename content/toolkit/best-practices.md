---
title: "Best Practices for AI in Legal Education"
description: "The Toolkit's flagship document. Student and faculty AI use cases organized by activity type and academic setting; AI training pipelines; efficacy assessment; academic standards; ethical considerations; access and equity."
date: 2025-08-01
lastmod: 2026-05-09
weight: 10
toolkit_category: "core"
audience: ["faculty", "student"]
availability: "public"
version: "August 2025; revised for migration May 2026"
---

The Lab's flagship faculty-facing document. Organizes student and faculty AI use cases by activity type and academic setting; covers AI training pipelines, efficacy assessment, academic standards, ethical considerations, access and equity, and a glossary of terms.

Revised regularly as the field moves.

## Introduction

In summer 2023, the AI Law Lab at the University of Pennsylvania Carey Law School began a sustained research effort to understand how generative AI tools could be integrated into legal education.

"Generative AI tools" covers many platforms capable of generating content — textual, visual, auditory, or interactive. Our focus is on tools that use natural language processing (NLP) to generate and classify text or answer questions conversationally. Some are general-purpose; others are built specifically for the legal domain. General-purpose tools include ChatGPT, Claude, Gemini, and Elicit. Legal-specific tools include Westlaw CoCounsel, Lexis+ with Protégé, Bloomberg Law's AI Assistant, Harvey, and Spellbook. Throughout these materials, "AI tool" refers to both general and legal-specific text-based generative AI tools.

This document makes recommendations across four domains:

1. Use cases for AI tools in legal education
2. AI tool efficacy and performance
3. Academic and ethical standards
4. Access and resources

The recommendations here are not prescriptive, and **do not represent the policy of the Law School or any particular faculty member**. Each situation is different, and may call for different approaches than the ones noted here.

This document is an ongoing collaborative effort within the community. We welcome feedback and suggestions for additions and refinements; we plan to update this document regularly as we learn more about these tools and their uses in law and legal education. Contact information appears at the end.

## Use Cases for Students

Student AI use in legal education divides usefully into eight activity categories: brainstorming, learning, searching, summarizing, informal drafting, formal drafting, editing, and planning.

1. **Brainstorm.** Generate ideas for a writing assignment, research paper, publication, or extracurricular activity. AI tools can be remarkably creative when prompted well (see the [Prompt Guide]({{< ref "/toolkit/prompt-guide" >}})), and the back-and-forth interface lets you follow up to focus on specific topics.

2. **Learn.** Explore a new topic — a case's takeaway points, an overview of a legal doctrine, the basics of an unfamiliar area of law. More open-ended than brainstorming or summarizing. AI tools are quite helpful for general overviews.

3. **Search.** Ask a specific (legal) question. More fact-based and narrow. AI tools can help, but many are prone to hallucination, so use for fact-gathering with caution. Legal-specific tools like Westlaw CoCounsel and Lexis Protégé tend to be better at legal questions but remain susceptible to hallucinations and to surfacing less-relevant authority.

4. **Summarize.** Use AI tools to summarize an area of law, or specific cases or papers. Sometimes the model can do this from its own training data; in other cases you'll need to give it the source materials directly.

5. **Informal Drafting.** Produce case briefs or course outlines. Informal because the document is for personal use, not distribution.

6. **Formal Drafting.** Produce first drafts or skeleton structures for writing assignments. Formal because the draft will eventually be submitted in an official capacity.

7. **Edit.** Revise written work — journal articles, emails, paper drafts, peer review.

8. **Plan.** Some AI tools help create plans or schedules — studying, optimizing a busy week.

### AI use across academic settings

Students may want to use AI tools in different law school settings — during in-class activities, alongside lectures and discussions, or outside class for prep and other at-home learning. The table below summarizes our thoughts and recommendations by setting.

| Setting | Student usage |
|---|---|
| **Doctrinal coursework** (most 1L classes, often Socratic) | Proceed with extreme caution when using AI in traditional doctrinal coursework, especially as a 1L. A core part of being a successful law student is learning to navigate case readings and in-class dialogue (including the Socratic method) in a traditional doctrinal setting. Heavy reliance on AI in this context risks displacing the core skills 1L doctrinal courses are designed to build, and can be a source of in-class distraction. <br><br>AI is well-suited to supplement doctrinal learning *outside* class. It can help work through concepts, ask questions, or clarify your understanding of class material. It's also useful for exam prep — generate multiple choice questions or fact patterns to test yourself; ask it to decode or analyze practice exams; ask for study tips for a specific subject. Effective use depends on knowing how to [prompt]({{< ref "/toolkit/prompt-guide" >}}) the tool. You can also create a custom GPT or Claude Project with specific instructions and your class materials uploaded — generating review materials from a more or less "closed universe" reduces the chance of hallucination. |
| **Research & writing courses** | Research and writing courses vary in their AI policies. Some Legal Practice Skills faculty have integrated AI into instruction — for demonstrations, or as one of several research tools — while others have not. Possible classroom uses include researching elements of a cause of action, tightening writing, and generating rough first drafts of legal analysis. <br><br>In other courses, faculty may discuss the acceptable ways students may use AI — brainstorming paper topics, working on sentence structure, editing, generating first drafts. Always follow your individual instructor's policy. If your professor doesn't address AI use upfront, ask. |
| **Clinics, seminars, journals, other coursework** | Non-doctrinal courses, including research and experiential coursework, may allow more AI use depending on the professor's policy and the nature of the course. If the professor doesn't address AI use upfront, ask. <br><br>See the [Prompt Guide]({{< ref "/toolkit/prompt-guide" >}}) for more on getting good results. |
| **Upper-division coursework** | Compared with 1L doctrinal courses, upper-division courses generally have more room for AI use, particularly to learn content. By the time students reach upper-level coursework, they should be able to identify where AI tools perform well (summarizing, editing, quickly learning content at a high level) and where they don't (learning professor-specific takeaways, navigating complex doctrine). |
| **Use outside class** | AI tools help work through concepts, ask questions, or clarify understanding. Effective use depends on prompting — see the [Prompt Guide]({{< ref "/toolkit/prompt-guide" >}}). <br><br>These uses can supplement, but should not replace, the core synthesis work of summarizing and outlining yourself — the synthesis is much of the learning. With that caveat, specific ways to use AI tools when studying for class: <br>1. Summarizing cases — as a check on your own reading, not a substitute for it <br>2. Generating multiple choice questions or fact patterns to test your knowledge <br>3. Decoding or analyzing practice exams ("why is xyz concept true") <br>4. Getting real-life examples <br>5. Generating study tips for a specific subject <br>6. Stress-testing an outline you've already drafted |

## Use Cases for Faculty

Many of the student use cases above have faculty counterparts.

| Setting | Faculty usage |
|---|---|
| **Doctrinal coursework** | Modern generative AI tools support faculty in developing both in-class and supplementary materials. <br><br>Examples: generating lesson plans, drafting class slides, planning a week or semester, formulating questions and problems for class, building practice problems and exam questions. <br><br>Teaching assistants can be useful for many of these tasks as well. <br><br>As with all AI use, effective use depends on prompting — see the [Prompt Guide]({{< ref "/toolkit/prompt-guide" >}}). |
| **Research & writing courses** | Beyond classroom slides and scheduling, faculty can use AI to demonstrate and teach legal research using AI. <br><br>AI tools also help create hypothetical scenarios and examples, or produce lists of possible topics or research areas. |
| **Seminars** | AI tools help brainstorm seminar topics and find useful papers and readings. They can quickly summarize a large number of articles, making the selection of readings more efficient. |
| **Upper-division coursework** | Similar use cases as doctrinal coursework, above. |
| **Non-course uses** | AI tools are helpful in three categories: teaching, research, and organization. <br><br>1. **Teaching** — refresh content and material; keep up to date with new developments and cases. <br>2. **Research** — brainstorm ideas for papers or articles; write first drafts; edit drafts. <br>3. **Organization** — plan office hours; plan weekly personal and professional schedules. |

## How AI Tools Are Trained

AI tools are built in three stages — training, validation, and testing:

1. **Training.** Fit model parameters to a labeled training dataset.
2. **Validation.** Evaluate the model on a held-out validation set to tune hyperparameters and choose between candidate models.
3. **Testing.** Assess final performance on a separate test set the model has never seen.

For example, ChatGPT is built on the GPT family of models — **Generative Pre-trained Transformer**. The name is revealing: these systems (1) generate results, (2) are pre-trained on large corpora, and (3) use the transformer architecture to self-weight text inputs to "understand" text and infer meaning and context. OpenAI's InstructGPT and ChatGPT used Reinforcement Learning from Human Feedback (RLHF), a technique that incorporates human ratings into the training loop to fine-tune the system for helpful, conversational responses. Claude (Anthropic) uses related alignment techniques, including Constitutional AI, which trains models against a written set of principles using AI-generated feedback in addition to (or in place of) human ratings.

Training is critical. Done poorly, it produces classic failure modes — overfitting (the model performs well on training data but poorly on new data) and underfitting (poor performance on both). Because AI algorithms imitate the world they were trained on, performance is determined by the quality and accuracy of the training data. Good training requires data that is high-quality, accurate, and broadly representative of the domains the model is expected to handle.

General-purpose AI tools like ChatGPT and Claude are trained on enormous text collections — books, articles, Wikipedia, and large web datasets like Common Crawl. As companies acquire access to better training data, the tools improve. AI platforms can also be trained or supplemented with domain-specific materials — most relevantly here, legal materials. These law-specific tools work better in legal contexts because they're trained on focused legal corpora and may be limited to particular legal tasks. The validation process is more refined because the model is trained and validated on text within a narrow legal corpus. (These tools remain early in development and require careful use.) General-purpose tools are typically less effective on specific legal questions because their training data is so broad — better for general questions and brainstorming, less reliable on complex legal nuance.

## AI Tool Efficacy and Performance

In the past few years, there's been substantial discussion about AI tools and their potential to transform legal practice. Enthusiasts envision AI tools providing valuable legal insight or functioning as pseudo-lawyers. Today's tools fall short of those expectations. AI can speed up legal research, help with brainstorming and first drafts of legal writing, and support document editing. But the tools do not yet possess the reliability or accuracy needed to transform the profession. The next generation of legal professionals must learn how to work alongside these tools and recognize their limitations.

AI tools work best when paired with human expertise, critical thinking, and legal reasoning. An iterative approach — flexible prompting, refining as you go — produces the strongest results. The tools also produce false information, which means you must always fact-check. A useful baseline: assume the tool is wrong unless you can verify against another source.

## Academic Standards

AI is a tool, like textbooks, lecture slides, reference works, or websites. Like any other tool, it's best practice to be clear about what is and isn't allowed.

Including an AI usage policy in the syllabus is an effective way to set expectations clearly. See the Lab's [Syllabus Guide]({{< ref "/toolkit/syllabus-guide" >}}) for templates and examples.

**For students, the most important consideration is the faculty member's policy:**

1. **Follow class policies.** Faculty will adopt a range of policies on AI use. These policies supersede any general recommendation, guideline, or suggestion you find elsewhere — including in this Toolkit. *When in doubt, ask.*

2. **Be transparent.** When you use AI, basic attribution and citation rules apply — just as they would for an article, news source, or website.

3. **Always check accuracy.** If you use AI tools at any stage, scrutinize what was generated and verify that it's accurate and what you intended.

## Ethical Considerations

AI tools raise important ethical issues. Responsible use requires awareness of bias embedded in algorithms — if a model is trained on data containing bias against a group, the model's decisions and outputs will reflect that bias. Lack of transparency and accountability are related challenges. Many AI tools are technically opaque — "black box" models — meaning the internal algorithmic process isn't visible to the user, which makes it hard to examine why a particular output appeared. That opacity makes it harder to detect and address bias and discrimination, which is why human discretion remains essential when using AI-generated content.

AI tools also raise specific challenges for lawyers, who operate under a professional code that requires high standards of accuracy, accountability, and reliability. Anything a lawyer says or writes in a professional context — especially in court — must be accurate, complete, justifiable, and truthful. Lawyers are particularly exposed to AI weaknesses because models hallucinate — they generate factually incorrect, fabricated, or sometimes nonsensical information that looks plausible. Many attorneys have been sanctioned since 2023 — beginning with the high-profile *Mata v. Avianca* matter — for filing briefs containing AI-generated fabricated citations they did not verify. Damien Charlotin's [AI Hallucination Cases Database](https://www.damiencharlotin.com/hallucinations/) maintains an ongoing tally.

Practicing lawyers also need to comply with confidentiality and client-data privacy rules. Inputting client information into a public AI tool may break attorney-client privilege, depending on the tool and on who can see prompts on the company's end. Many law firms initially prohibited attorneys from using publicly-available AI tools for these reasons, and many continue to restrict such use even as they roll out internal, enterprise-grade alternatives.

## Access and Resources

### How to get access

Most legal AI tools are subscription-based and require credentials, but law students have several free options: ChatGPT, Claude, Gemini, and Microsoft Copilot. Starting in Fall 2025, 1L students, teaching assistants for 1L courses, and Littleton Fellows receive ChatGPT Edu accounts through the Law School. Westlaw CoCounsel and Lexis+ with Protégé are also available as part of the Law School's subscriptions.

### Training resources

The Lab maintains an evolving set of training materials and workshops for Penn Carey Law students and faculty. See the [Toolkit landing page]({{< ref "/toolkit" >}}) for current offerings.

Useful external resources include Wharton professor Ethan Mollick's YouTube series ["Practical AI for Instructors and Students"](https://www.youtube.com/playlist?list=PL0EdWFC9ZZrUAirFa2amE4Hg05KqCWhoq) and his AI blog [One Useful Thing](https://www.oneusefulthing.org/).

### Equity considerations

AI in legal education will have important equity effects. Some community members have access to particular AI tools that others don't. Some have better access to computing resources or background knowledge in the field. Students and faculty should keep these access and knowledge differences in mind when integrating AI tools into the learning environment.

Beyond access and knowledge, AI tools themselves contain biases and knowledge gaps that can render output incomplete, misleading, or discriminatory. Members of the legal community have a duty to guard against bias in their work, and special care is required when using AI tools to make sure final products meet the standard.

## Glossary

**Artificial intelligence (AI)** — the ability of a computer to perform tasks commonly associated with human intelligence. AI is not new, but its current widespread application is.

**Generative AI** — a broad term for any AI system that *generates* content.

**Foundation models** — large artificial neural networks pre-trained on large datasets *without a particular end-use in mind*. The term was coined by researchers at Stanford's [Center for Research on Foundation Models](https://crfm.stanford.edu/) in 2021 to describe the shift toward fundamental underlying models that drive many specific applications. Earlier AI models were trained on task-specific data for narrow uses.

**Large language models (LLMs)** — a subset of foundation models focused on text data and natural language tasks. Typically classified by parameter count and by the amount and type of training data. The GPT family (OpenAI) and Claude (Anthropic) are examples; ChatGPT and Claude.ai are direct interfaces to those underlying LLMs.

**Hallucinations** — when AI models, particularly LLMs, generate incorrect or misleading information presented as fact. Hallucinations range from minor inconsistencies to fully fabricated content, and they often appear plausible because the language is fluent.

**Prompting** — the process of crafting instructions or inputs (prompts) that guide a generative AI model to produce desired outputs — text, images, code. Detailed prompts (specifying tone, audience, goals) produce better output. See the Lab's [Prompt Guide]({{< ref "/toolkit/prompt-guide" >}}).

**Training** — the process of teaching a machine learning algorithm from data. The model is fed a dataset and its parameters are iteratively adjusted based on the results, with the goal of improving performance on a specific task — making predictions, classifying information. Training does not enable a model to independently reason; it makes the model better at predicting results based on the data it has seen.

## Contact

This document is maintained by:

- Ambar Larancuent '26
- Hailey Parikh '27
- Polk Wagner — `pwagner@law.upenn.edu`

*With thanks to AI Law Lab alumni who helped create this document:*

- Meghana Bhimarao '25 — AI Law Lab & CTIC Fellow
- Lakshmi Prakash '25 — AI Law Lab & CTIC Fellow

## Status

The Lab's flagship faculty resource, updated regularly to reflect the current state of AI in legal education. Comments and suggestions: <pwagner@law.upenn.edu>.
