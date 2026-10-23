# Divine Bloodlines — Crusader Kings II

**English** · [Русский](README.ru.md) · [Changelog (EN)](CHANGELOG.md) · [История изменений (RU)](CHANGELOG.ru.md)

A mythology-focused mod for **Crusader Kings II 3.3.5.1**, introducing divine rulers, hereditary godhood, evolving bloodlines, legendary relics, divine powers, and a mortal secret society that can challenge the gods.

> **Development status:** This repository contains both English and Russian variants of the mod. The latest historical changelog is **v2.2.7.4.8**, but both `.mod` descriptors currently display **v2.2.7.4.6**. These labels have not yet been reconciled. The archived validation for 2.2.7.4.8 is static only; full in-game verification is still needed.

## Contents

- [Requirements and installation](#requirements-and-installation)
- [Starting a divine campaign](#starting-a-divine-campaign)
- [Divine blood and inheritance](#divine-blood-and-inheritance)
- [Immortality and godslaying](#immortality-and-godslaying)
- [Powers and artifacts](#powers-and-artifacts)
- [Order of the Sickle](#order-of-the-sickle)
- [World events and heroism](#world-events-and-heroism)
- [Development and compatibility](#development-and-compatibility)
- [Troubleshooting and feedback](#troubleshooting-and-feedback)

## Requirements and installation

- **Game:** Crusader Kings II, version **3.3.5.1**.
- **Holy Fury:** used for duels, bloodlines, warrior lodges, and several event chains.
- **Monks and Mystics:** required for the **Order of the Sickle** society (the script checks the `Mystics` DLC).
- Other DLC-specific event integrations are present. Not every DLC combination has been tested in-game.

1. Download or clone this repository.
2. Open your CK2 user-mod directory, normally `Documents/Paradox Interactive/Crusader Kings II/mod/` on Windows.
3. For **English**, copy **both** `Divine_Bloodlines_EN/` and `Divine_Bloodlines_EN.mod` into that `mod/` directory.
4. For **Russian**, copy **both** `Divine_Bloodlines_RU/` and `Divine_Bloodlines_RU.mod` instead.
5. Enable **only one** language variant in the CK2 launcher; do not activate both simultaneously.
6. Start a new campaign for initial testing. Older saves have migration and repair events, but compatibility across every historical version is not guaranteed.

Your installation should look like:

```text
Crusader Kings II/
└── mod/
    ├── Divine_Bloodlines_EN/
    │   ├── common/
    │   ├── decisions/
    │   ├── events/
    │   ├── gfx/
    │   ├── interface/
    │   └── localisation/
    └── Divine_Bloodlines_EN.mod
```

For Russian, replace both `_EN` names with `_RU`. The `.mod` file points to `mod/Divine_Bloodlines_EN` or `mod/Divine_Bloodlines_RU`; folder names must match exactly.

## Starting a divine campaign

- The mod defines **Zeus** and **Odin** origin-marker traits for Ruler Designer. Their initialization establishes canonical divine identities.
- If a founder was not selected by a player, the mod has **one-time automatic arrival** logic for the missing founder. Arrival and old-save recovery use event-led world initialization.
- Zeus and Odin have independent pantheon identities, divine families, succession mechanics and deity-specific abilities. Canonical figures include **Hera, Poseidon, Hades, Demeter, Hestia, and Frigg**.
- Founders and their divine families can participate in council and commander systems through dedicated eligibility handling.
- Certain founder/AI arrival mechanics create troops or territorial claims; exact results depend on start conditions and existing-save state.

## Divine blood and inheritance

Divinity is not simply a permanent inherited bonus. The mod tracks **genealogical ancestry**, **biological parentage**, and **current divine blood strength** separately.

- Blood components pass through the **biological father and mother**, regardless of marriage type, concubinage or bastard status.
- Descendants may be **true gods**, **active demigods**, **faded descendants**, or carriers of **latent** divine ancestry. Blood can weaken over generations and, under the scripted conditions, awaken again.
- Zeus and Odin founder lines are distinct from generic **Olympian** and **Norse** god states.
- Same-pantheon true-god unions retain full divine status where the lineage resolver permits it. A full Olympian and a full Norse god can produce a **cross-pantheon true god**; mixed ancestry is not automatically the special **Blood of Two Thrones** state.
- **Hera and Frigg have their own genealogical bloodlines** in the latest recorded patch, without pretending to be Zeus/Odin descendants. This ancestry remains distinct from the child's one visible strength trait.
- Hereditary traits and ancestry are repaired by the birth resolver and migration events, including for some older saves.

The precise implementation is in [bloodlines](Divine_Bloodlines_EN/common/bloodlines/divine_bloodlines.txt), [traits](Divine_Bloodlines_EN/common/traits/divine_blood_traits.txt) and the [inheritance events](Divine_Bloodlines_EN/events/divine_blood_v22745.txt).

## Immortality and godslaying

An **intact true god aged 16 or older** is intended to survive ordinary mortal killing, mundane duels, hunting accidents, assassinations, and many vanilla event deaths. This protection does **not** apply unconditionally to younger gods, or to gods whose immortality has been severed. Several late-loaded compatibility guards exist because CK2 uses numerous separate death paths.

**Cronus' Sickle** is a unique lost relic obtained through a search chain. Against an intact adult god, an eligible non-Godslayer wielder generally needs a **first successful duel to sever immortality**, then a **later finishing attack**. The first successful god-killer can establish the hereditary **Godslayer Bloodline**; its descendants have a special god-hunting exception even without the Sickle. Possessing society membership alone does not grant the right to kill gods.

God-capture, prison-escape, divine judgment, duels and injury handling also have dedicated mechanics. The latest historical patches expanded survival guards, but **static validation is not proof that every vanilla or DLC death event is safe**.

## Powers and artifacts

### Zeus and the Olympian pantheon

Zeus-related gameplay includes thunderbolt judgment, divine visitation, transformations into **swan, bull, eagle and serpent**, related form actions, and Olympian family/pantheon mechanics. Divine blood and line-head authority determine which powers descendants may use.

### Odin and the Norse pantheon

Odin-related systems include **Huginn and Muninn** intelligence and scouting, rune insight, **Seidr**, sacred oaths, blessings, divine wandering, Yggdrasil events, and Norse supernatural support. In the latest recorded patch, raven powers provide scoped intelligence rather than random prestige/piety payouts.

### Relics and expeditions

Named relics include **Cronus' Sickle, Gungnir, Zeus' Thunderbolt, Aegis, Draupnir, the Labrys, Hades' Bident, Poseidon's Trident, the Cornucopia of Amalthea, the Golden Fleece**, and additional Greek/Norse legendary objects. Searches are event chains with outcome feedback, cooldowns and campaign-wide uniqueness guards. The Labrys' labyrinth expedition is distinct from the Sickle's god-killing mechanic. **Mjolnir** is deliberately not duplicated as a second custom artifact.

See [artifact definitions](Divine_Bloodlines_EN/common/artifacts/divine_blood_artifacts.txt), [relic decisions](Divine_Bloodlines_EN/decisions/divine_blood_v2272_relics.txt) and [relic events](Divine_Bloodlines_EN/events/divine_blood_v2272_relics.txt).

## Order of the Sickle

The **Order of the Sickle** is a hostile **secret mortal society** with four ranks and a **Secret Knowledge** currency. Its ranks provide intelligence, demigod hunting, relic theft, trap preparation, Sickle tracing and Grand Hunts. Intact true gods and active demigods cannot be members; faded or latent descendants may qualify.

The most recent documented recruitment process uses **four stages**: first contact, revelation, a field trial and a final oath. Membership is granted only after completing the oath. AI membership and leadership have recovery/population controls. Recruitment, costs and outcomes are probabilistic; they are not guaranteed in every game.

The society requires **Monks and Mystics**. For implementation details see [society definition](Divine_Bloodlines_EN/common/societies/db_order_sickle.txt), [society events](Divine_Bloodlines_EN/events/divine_blood_society.txt) and [society decisions](Divine_Bloodlines_EN/decisions/divine_blood_society_decisions.txt).

## World events and heroism

The mod adds news and event chains for divine arrivals, the birth of new demigods or true gods, blood reawakening, godslayers, and changes to the world's divine population. Demigods can pursue **heroic paths**, undergo trials, and, when qualified, create a **hero cult**. A larger **Age of Heroes** is governed by population and progression checks.

Both founding pantheons have long-term religious restoration/reformation and faith-expansion goals. Vanilla systems such as Holy Fury warrior lodges are integrated through specific recovery and survival safeguards.

## Development and compatibility

```text
Divine_Bloodlines_EN/     English game files
Divine_Bloodlines_RU/     Russian game files
Divine_Bloodlines_EN.mod  English launcher descriptor
Divine_Bloodlines_RU.mod  Russian launcher descriptor
README.md                English project overview
README.ru.md             Russian project overview
CHANGELOG.md             English summary of version history
CHANGELOG.ru.md          Russian summary of version history
```

- **`master`** is the main branch. Make feature/fix branches and open pull requests against `master`.
- Apply gameplay changes to **both** EN and RU variants; preserve legitimate language-specific differences.
- **Do not reorder existing traits**: their order is relevant for CK2 saved-game trait IDs.
- Keep the intended localization encodings: **RU CSV in Windows-1251 (CP1251)** and **EN CSV in UTF-8**. Avoid automatic encoding conversions or formatting unrelated files.
- The mod overrides several vanilla scripted triggers, scripted effects and DLC event paths. Other mods that modify those same paths can conflict; broad compatibility is not claimed.
- Preserve existing CK2 scripting conventions and change only what the fix requires.

The repository already includes original per-version `CHANGELOG_v*.txt` and `VALIDATION_v*.txt` files under **both** language folders. Those are historical source records and remain unchanged. Read [the English changelog](CHANGELOG.md) or [Russian changelog](CHANGELOG.ru.md) for an organized summary.

## Troubleshooting and feedback

If the launcher does not see the mod, check the directory layout, the matching `.mod` file, and whether the language variants are accidentally both enabled. If text is garbled, check the game language, selected mod variant and original localization encoding.

For a crash or gameplay bug, open a [GitHub issue](https://github.com/lassizness/Divine-Bloodlines-CK2/issues) with your **CK2 version**, **active DLC/mods**, **new game vs old save**, **language variant**, **steps to reproduce**, and relevant `error.log` / `game.log` files. Do not include sensitive system information in logs.

**Testing note:** The repository's latest archived validation was static (syntax/asset/consistency checks). It does not replace an actual CK2 client test.
