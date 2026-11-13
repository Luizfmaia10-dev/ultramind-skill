# ultramind-skill

**A token-efficient meta-skill for discovering, ranking, selecting, and orchestrating agent skills without losing user requirements.**

## What it does

- Reads the available skill **inventory once per task**, using compact metadata rather than opening every large skill file.
- Computes an internal relevance ranking: **Metric X = 0.45 × Focus + 0.55 × Prompt Alignment**.
- Selects the smallest set of installed skills that fully covers the task, then follows their mandatory instructions.
- Treats 17 backup capability slots as **suggestions** unless a real skill implementation is installed and available.
- Preserves requirements, constraints, and original information; never removes them unilaterally.
- Uses progressive disclosure: entrypoint → selected skill instructions → needed references only.
- Follows the actual [Ponytail](https://github.com/DietrichGebert/ponytail) principle of the **smallest complete solution**, without cutting checks, security, accessibility, or tests.
- Reports actual actions and uncovered requirements without fabricating results.

## Install

Copy the entire `ultramind-skill` directory into your agent's configured skills directory. Example paths for supporting clients include `.agents/skills/ultramind-skill` and `.claude/skills/ultramind-skill`. Your host must support the Agent Skills format and expose a skill inventory for discovery to work.

The skill entrypoint is **`SKILL.md`**. It is the only required file. Keep `references/` for backup matching and scoring; `scripts/` are optional and use only Python's standard library.

This package does **not** install or bundle the 17 third-party backup skills; it includes a mapped reference catalog instead.

## Typical requests

- "Build a responsive React + Spring Boot SaaS with authentication and tests. Choose and use my existing skills."
- "Find the best skills for reviewing performance, security, and code quality of this API."
- "Rank the installed skills relevant to an existing SaaS architecture review; recommend missing capabilities."

## How it works

1. Preserve the full requirement set and constraints.
2. Discover skill names/descriptions in a single pass; reuse the compact in-task index.
3. Score candidates internally using Metric X.
4. Select installed skills to cover **all** mandatory requirements.
5. Suggest missing capabilities using the reserve catalog, but never pretend those entries are installed.
6. Follow the selected skills' full mandatory instructions, execute where available, and validate.

## Optional local utilities

```bash
python scripts/index_skills.py --root /path/to/skills --output /tmp/my-skills.json
python scripts/rank_skills.py examples/backend-task.json
python -m unittest discover -s tests -v
```

`index_skills.py` reads only frontmatter of direct skill folders in explicitly supplied roots and does not install or modify skills. `rank_skills.py` uses agent/user-provided scores; it is a deterministic calculator, **not a natural-language understanding model**.

## Repository layout

```text
ultramind-skill/
├── SKILL.md
├── README.md
├── references/
│   ├── backup-catalog.md
│   ├── metric-x.md
│   ├── operating-rules.md
│   └── research.md
├── scripts/
│   ├── index_skills.py
│   └── rank_skills.py
├── examples/
│   └── backend-task.json
└── tests/
    └── test_skill_tools.py
```

## Provenance and limitations

The implementation is informed by public Agent Skills practices and several prominent GitHub projects, summarized with links in [research](references/research.md). It does not claim to have analyzed every GitHub skill or to have tested actual agents in every runtime. The scripts and static package structure can be locally unit-tested; effectiveness in a specific agent must be verified in that agent.

**Principle:** Read once. Understand deeply. Rank intelligently. Select precisely. Execute efficiently. Preserve every requirement.
