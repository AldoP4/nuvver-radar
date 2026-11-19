# /radar

[Español](README.md) | **English**

**Stop asking AI "what business should I start?" and getting the same answer as everyone else.**

`/radar` is a skill for Claude Code (and other agents) that finds **business opportunities that exist today, for you**, and tells you how to get paid: who buys, why now, what people already pay, how to reach that buyer in 7 days, and how to test it before writing a line of code.

It was built in Spanish for Latin America, but it works in any language and country: it searches in yours.

```
/plugin marketplace add AldoP4/radar-oportunidades
/plugin install radar@radar-oportunidades
```

Then type `/radar` (or `/radar:radar` as a plugin), or just ask Claude *"what can I sell with what I know?"*. No keys, accounts or config: it uses your agent's built-in web search.

## What it does

1. **Clock.** Anchors the real date from your machine and counts the days to every deadline, so the model stops assuming it lives in its training year.
2. **Your profile.** Skills, time, money, what you won't do, and your income goal.
3. **"Why now" signals** of 7 kinds: dated regulation, platform changes, new AI capabilities, recurring complaints, money already being spent, seasons, and gaps that open up.
4. **12–20 candidates**, each written as *"For [buyer] who [pain] because [why now]: [what you deliver]"*.
5. **A hard filter.** A weighted 7-criteria rubric where **"does anyone already pay for this?"** and **"can you reach the buyer in 7 days?"** weigh the most, plus kill rules, devil's advocate and a pre-mortem.
6. **The top 3, in depth:** buyer and where they are, competitors and prices, price ladder, the trust the buyer needs, how to reach them, and a **7-day test** to sell before you build.

You get a `radar-YYYY-MM-DD.md` report and **the one action to take today**. See a [real example report](ejemplos/radar-2026-11-18-mexico.md) (Mexico, Nov 18, 2026; in Spanish).

## Built on

*Why Now* (Sequoia), organic ideas and schlep blindness (Paul Graham), follow the money and the stair-step approach (Rob Walling), Jobs to Be Done (Christensen, Moesta), *The Mom Test* (Rob Fitzpatrick), pre-selling (Noah Kagan), riskiest assumption testing (Eric Ries), the value equation (Alex Hormozi), the pre-mortem (Gary Klein), and distribution first. Details in [metodologias.md](skills/radar/references/metodologias.md).

## Install

**Claude Code:** the two commands above. **Other [Agent Skills](https://agentskills.io) hosts:** `npx skills add AldoP4/radar-oportunidades -g`. **Manual:** copy `skills/radar` into `~/.claude/skills/radar`.

Made by [Aldo Pazzi](https://github.com/AldoP4) in Puebla, Mexico, with Claude Code · [Nuvver](https://nuvver.org) · MIT license.
