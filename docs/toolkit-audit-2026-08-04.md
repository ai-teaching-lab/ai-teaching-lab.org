# Toolkit Audit — 2026-08-04

| Page | Current role | Fall 2026 decision | Verification needed | Edit level |
| --- | --- | --- | --- | --- |
| `/toolkit/` | Generated landing page | Reframe as task-based Start Here page | Rendered landing page | Major |
| `ai-resources` | External Resources portal card | Keep as only access/setup/data-policy entry point | Live portal reachable | Minor |
| `ai-resources-at-penn` | Duplicate Penn resource directory | Preserve URL, remove from list, point to Resources portal | Build renders page but excludes from list | Medium |
| `faculty-guide` | Personal account setup guide | Preserve URL, remove from list, point to Resources portal | Build renders page but excludes from list | Medium |
| `syllabus-guide` | Fall 2026 syllabus language | Keep as first Toolkit resource | Anchor and link checks | Minor |
| `best-practices` | Old flagship overview | Rewrite as Fall 2026 principles guide | Stale-claim grep | Major |
| `policy-templates` | Struve templates | Keep, add Fall 2026 context and lastmod | Internal links | Minor |
| `teaching-demos` | Fall 2024 demo archive | Recast as reusable teaching examples | Custom GPT stale-language grep | Medium |
| `virtual-ta-guide` | Platform comparison with access claims | Recast as course-assistant design guide; route platform choice to Resources portal | Access-claim grep | Major |
| `guidance-1l` | Student Claude guidance | Align with Fall 2026 course-rule baseline | ChatGPT Edu drift grep | Medium |
| `ai-tips-1l` | Presenter notes | Align with student guide and Claude language | ChatGPT Edu drift grep | Medium |
| `prompt-guide` | CRAFTED prompting guide | Keep durable framework, modernize role | Stale description grep | Medium |
| `legal-ai-tool-guide` | Product/category overview | Keep category literacy; remove access/setup claims | Product/access grep | Medium |
| `resource-menu` | Duplicate menu page | Preserve URL, remove from list, point to Toolkit | Build renders page but excludes from list | Medium |

## Boundary Decision

Access, setup, eligibility, account tiers, data policy, privacy settings, and product-specific availability belong in the AI Resources portal at `https://resources.pennai.law/`. The AI Project Toolkit should link there instead of duplicating those details.
