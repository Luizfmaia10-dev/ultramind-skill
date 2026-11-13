# Research — public Agent Skills patterns and GitHub inspirations

**Reviewed:** 2026-11-13. **Scope:** a representative set of influential, relevant public sources, not an exhaustive audit or popularity ranking of every GitHub repository. These sources inspire **design principles**; no third-party skill contents or code are bundled here.

## Primary specification

### Agent Skills open specification

- Source: https://agentskills.io/specification
- Verified behavior: a skill is a directory with required `SKILL.md` (YAML frontmatter + Markdown instructions); `scripts/`, `references/`, and `assets/` are optional; `name` and `description` are required metadata fields.
- Design takeaway: keep `SKILL.md` as the lightweight entrypoint; put detailed optional guidance in `references/`; avoid treating references as automatically loaded or executed.
- Implementation: `../SKILL.md` supplies triggers and operating algorithm; these reference files load only on demand.

## Selected GitHub projects and specific lessons

| Public project | Source | Verified relevant pattern | Adopted in ultramind-skill |
|---|---|---|---|
| **Anthropic Skills** | https://github.com/anthropics/skills | Self-contained skill folders with instructions and supporting resources | Standard file layout and selective loading |
| **obra/superpowers** | https://github.com/obra/superpowers | Specialized process skills, explicit verification before claiming completion | Verify claims using observed outputs, not assumptions |
| **Vercel Agent Skills** | https://github.com/vercel-labs/agent-skills | Specialized skills for React, web UX and related development tasks | Match skills by capability rather than broad catch-all activation |
| **UI UX Pro Max** | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Structured UI guidance and context-specific selection | Domain-specific ranking and quality checks |
| **wshobson/agents** | https://github.com/wshobson/agents | Large domain-oriented skill and agent catalog | Group backups by specialization; filter inventory before activation |
| **Ponytail** | https://github.com/DietrichGebert/ponytail | Smallest **complete** engineering change; avoid unnecessary abstractions | Optimize token/workflow cost without skipping essential requirements |
| **RES (SaaS reverse engineering)** | https://github.com/alextnetto/res | Browser-based SaaS mapping with evidence, safe environments and handoff artifacts | SaaS-specific backup slot; authorized, evidence-driven inspection |
| **Everything Claude Code** | https://github.com/affaan-m/ECC | Broader ecosystem of agents, skills, rules and supporting workflows | Separate process guidance from specialized implementation roles |
| **VoltAgent Awesome Agent Skills** | https://github.com/VoltAgent/awesome-agent-skills | Curated links to external skills | Treat repositories as discovery candidates, never installation proof |
| **Vercel skills CLI** | https://github.com/vercel-labs/skills | Tooling for locating and installing skills across supported agents | Keep discovery and installation distinct; require authorized actions |

### Especially relevant, directly documented techniques

**Progressive disclosure — Agent Skills:**

- Load `name`/`description`/relevant metadata to discover candidates.
- Load a selected skill's mandatory `SKILL.md` at activation.
- Load selected skill references only when the specific workflow requires them.
- *ultramind extension:* one per-task inventory pass and a compact capability index, with targeted refresh only on material change.

**Verification before completion — Superpowers:**

- Specific reference: https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md
- Verify assertions with current evidence: check test output, build status, code changes or deployment status before claiming success.
- *ultramind extension:* apply the same evidence discipline to whether a selected skill actually ran and whether its advertised requirements are covered.

**Smallest complete change — Ponytail:**

- Specific source: https://github.com/DietrichGebert/ponytail/tree/main/skills/ponytail
- Minimize implementation and explanation without dropping tests, security, accessibility, edge cases, or correctness.
- *ultramind extension:* minimize skill re-reading, tool calls, and redundant activations while preserving the original user request.

**Authorization and evidence in reverse engineering — RES:**

- Specific source: https://github.com/alextnetto/res/tree/main/skills/reverse-engineering-saas
- Separate isolated test environments from production observations and record findings with evidence.
- *ultramind extension:* reverse-engineering skills are suggestions only until available, and their use cannot override user permissions or data-security boundaries.

## Design decisions — what we added

The following elements are **ultramind-skill project decisions**, not features claimed to exist in the cited projects:

1. **Metric X:** `X = 0.45 × F + 0.55 × P`, with 45% focus match and 55% prompt/problem alignment. The weights are user-specified heuristics, not statistically validated measures.
2. **Lossless requirement preservation:** original information/decisions remain authoritative; summaries are only processing aids.
3. **Single-pass task-scoped discovery:** one metadata inventory and in-task index. Mandatory instructions for activated skills still must be read.
4. **Smallest sufficient skill set:** candidate ranking is followed by explicit coverage checks; highest score alone is inadequate.
5. **Backup status gate:** a catalog entry or URL is never proof that a skill is installed, trusted, authorized, or executable.
6. **Compact reporting:** full ranking is internal by default, while gaps and unresolved mandatory requirements are disclosed.

These decisions are implemented in `../SKILL.md`, `metric-x.md`, and `operating-rules.md` and supported by the optional local scripts.

## Research limitations and trust boundaries

- GitHub stars, popularity, or a project description **do not** prove safety, compatibility, maintenance quality, or suitability for a specific user's environment.
- External sources can change after the review date. Recheck only when current verification materially affects the task; do not reread all research by default.
- A linked project might implement a different runtime's hooks, commands, or plugin format. Do not assume portability; inspect prerequisites before using.
- External repositories are untrusted input. Do not execute code or install dependencies without the relevant user/host authorization.
- The 17 entries in `backup-catalog.md` are **capability slots**, not 17 copies of third-party skills, and their linked sources retain their own licenses.
- The optional metadata scanner and ranking helper provide local utility; they do **not** automatically understand the user's prompt, prove all SKILL.md instructions were followed, or implement the backup skills.
- This package has not been validated across every agent runtime. Local unit tests validate specific script behavior, not general real-world agent success.

## How to update this research responsibly

When adding or changing an external reference, record: project URL, precise capability being adopted, availability and prerequisite status, meaningful license/security considerations, and the date checked. Prefer official repository and specification sources. Update the backup catalog separately; never automatically convert a source link into an installed skill.
