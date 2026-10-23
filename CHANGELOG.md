# Divine Bloodlines — Changelog

**English** · [Русский](CHANGELOG.ru.md) · [Project README](README.md)

This is the **curated repository-wide changelog**, based on the historical files already shipped with the mod. The original files remain untouched under `Divine_Bloodlines_EN/` and `Divine_Bloodlines_RU/` and are indexed below.

**Release tracking:** The last imported changelog is **2.2.7.4.8**. New releases are versioned from the root `VERSION` file, update both `.mod` descriptors automatically, and publish generated notes under [GitHub Releases](https://github.com/lassizness/Divine-Bloodlines-CK2/releases). Historical entries below are not runtime playtest certifications.

## Latest documented changes

### v2.2.7.4.8 — independent bloodlines and secret initiation ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.8.txt))
**Added**
- Independent genealogical bloodlines for **Hera** and **Frigg**, including old-save restoration and genealogy propagation.
- A **four-stage recruitment and initiation** for the Order of the Sickle: first contact, revelation, field trial, final oath. Membership now starts only after the final oath.
- Recruitment preferences for Godslayer descendants and capable, brave, ambitious or hunting-oriented mortals; divine friends/lovers are less likely recruits.
- Raven dossiers: targeted scouting exposes a character and, where relevant, the target's active plot.

**Changed**
- Odin's untargeted Huginn/Muninn power now selects counter-plot intelligence, war scouting or world wisdom for a year, replacing the old random prestige/piety reward.
- Zeus/Hera and Odin/Frigg children retain real parental genealogies while displaying only one correctly classified true-god strength trait.
- Failed initiation no longer kills the candidate; it may result in a minor wound and can be retried later.

### v2.2.7.4.7 — survival guards and recruitment recovery ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.7.txt))
**Fixed**
- Reconciled founder start-army flags to prevent duplicate 2,000-man hosts; old-save duplicates are migrated.
- Expanded last-line accident/death guards across Holy Fury, Reaper's Due, Horse Lords, Conclave, Hermetic and warrior-lodge event branches.
- Reworked an inverted Holy Fury ritual-hunt injury condition that could kill protected gods.
- Added a player-facing grandmaster invitation and emergency Order leadership recovery; the later **v2.2.7.4.8 initiation chain supersedes the one-click joining flow**.
- Ordinary protected-god environmental harm resolves to **90% no effect / 10% Wounded** in the covered paths.

### v2.2.7.4.6 — low-harm defense and hostile-power filtering ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.6.txt))
- Introduced shared low-harm survival logic for intact adult gods in ordinary duels, hunts, beast attacks, executions and captivity.
- Added a hidden anti-plot ward; it is removed when immortality is severed.
- Blocked or neutralized hostile Tainted Touch and Demonic Possession targeting intact gods.
- Restricted temporary diplomatic immunity to the imprisoned state to avoid a council eligibility regression.
- Preserved the existing Sickle/Godslayer authorized-kill exception.

### v2.2.7.4.5 — authoritative inheritance resolver ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.5.txt))
- Replaced competing child classifiers with **DBV2.1290**.
- Same-pantheon full-god children now resolve to one visible true-god trait; Zeus/Odin strength no longer leaks automatically to Hera/Frigg.
- Introduced generic Norse demigod/faded and mixed-faded classifications, with hidden ancestry carried through flags.
- Added old-save ancestry repairs and late hunting/tiger-death protections.

### v2.2.7.4.4 — birth, succession and interface fixes ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.4.txt))
- Delayed the newborn inheritance pipeline by a day, leaving CK2's naming dialog intact.
- Separated divine founder identity, ancestry flags and visible god-tier states, including **cross-pantheon** lineage.
- Improved designated divine-heir selection, including AI fallback and inheritance of certain line-head powers.
- Removed the duplicate legacy Draupnir search action.
- Repaired legendary-journey guard/recovery logic and normalized targeted-decision icons to **28×28**.

### v2.2.7.4 and v2.2.7.3.x — canonical family regressions
- **2.2.7.4** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.txt)): restored the last known-good founder/family creation flow, repaired startup ordering, council eligibility flags and old-save family access.
- **2.2.7.3.1** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.3.1.txt)): narrowly repaired Zeus/Frigg family council permissions without globally changing vanilla character eligibility.
- **2.2.7.3** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.3.txt)): corrected Gungnir/Thunderbolt confirmation tooltips and temporarily restored legacy bloodline membership; later versions refined genealogical separation.

### v2.2.7.2 / v2.2.7.1 / v2.2.7 — relics, AI realms and family roles
- **2.2.7.2** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.2.txt)): canonical family council/commander repair; Labrys labyrinth quest expansion; consistent 2,000-man initial troops and relic-search eligibility.
- **2.2.7.2 complete integration** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.2_COMPLETE.txt)): larger unique Greek/Norse relic pool, God-family returns to restored courts, AI reconquest preparation, explicit inherited line-head powers.
- **2.2.7.1** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.1.txt)): Russian localization corrected to **Windows-1251** for CK2 3.3.5.1.
- **2.2.7** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.txt)): Aegis made searchable, Thunderbolt/Gungnir designated carried relics, designated divine-heir interactions, added mythic relics and AI-only Olympus/Asgard identities.

## Earlier milestones

### v2.1.6.9.2 — event flow and founder identities ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.9.2.txt))
- Made cancelled artifact searches/Order operations free until confirmation; AI executes confirmed actions.
- Improved divine-strike victim/caster feedback, captive-god judgment and god-related event text.
- Repaired canonical Zeus/Odin names, religions and appearance after Ruler Designer/startup.
- Switched automatic Zeus arrival territory to a randomized **Epirus county**; player-selected founders keep their chosen starting location.

### v2.1.6.9.1 — trait UI and death overrides ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.9.1.txt))
- Migrated old hidden technical traits into flags/modifiers to remove gaps in the trait UI, while preserving trait definition order for saves.
- Fixed scripted-helper load order and added guards for direct duel, battlefield and legendary-death event paths.

### v2.1.6.9 — divine judgment and regalia ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.9.txt))
- Rebalanced Zeus/Gungnir strike outcomes, survivor progression, victim notifications and anonymous divine-death causes.
- Added canonical divine-family regalia, council access and delayed newborn notifications.

### v2.1.6.8 / 8.1 / 8.2 — heroes, genetics, real duels
- **2.1.6.8** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.8.txt)): repaired Legendary Gathering, added proper two-stage Sickle duels, world-wide Godslayer challenges, delayed relic expeditions, cross-pantheon genetics, heroic trials and the Age of Heroes.
- **2.1.6.8.1** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.8.1.txt)): gave player-selected Zeus and Odin one-time 2,000-man starting hosts.
- **2.1.6.8.2** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.8.2.txt)): expanded last-line duel protection and recovered guard override load order. (Further load-order work followed in later patches.)

### v2.1.6.6 / 6.7 — AI population and crash protection
- **2.1.6.6** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.6.txt)): staged automatic founder creation to avoid same-event title-transfer crashes, limited Order recruitment by population, removed erroneous BOM/script dependency, reconciled Sickle uniqueness.
- **2.1.6.7** ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.7.txt)): extended adult-god duel, hunting and generic injury safeguards without changing the **age ≥ 16** protection threshold.

### v2.1.6 / 6.2 — landed founders and startup ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.txt), [source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.2.txt))
- Automatic founders gained a landed start (historically Thessalia for Zeus and Uppland for Odin), independence and one-time 2,000-man forces.
- Added Ruler Designer startup fallbacks, arrival watchdogs and old-save bootstrap recovery. Later patches changed certain territory/start paths.

### v2.1.5 — pantheon families and diplomacy ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.5.txt))
- Introduced fresh auto-arriving founders, additional Olympian demigod inheritance, divine late-life fertility rules, succession recovery and campaign-unique artifacts.
- Replaced overactive romantic event popups with passive divine allure and explicitly initiated divine unions.

### v2.1.4 — automatic divine arrival ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.4.txt))
- First introduced one-time missing-founder arrivals for Zeus/Odin, global notifications, divine attraction and strengthened mortal-vs-god survival logic. Arrival implementation has since been revised.

### v2.1.3 — Order of the Sickle ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.3.txt))
- Added the four-rank secret society, intelligence, demigod hunting, relic theft, traps and Grand Hunts; society membership itself never permits killing intact gods.

### v2.1.2 — origins, powers and bloodlines ([source](Divine_Bloodlines_EN/CHANGELOG_v2.1.2.txt))
- Expanded divine transformations, Odin and Zeus abilities, heroic demigod mechanics, special artifacts, inherited Godslayer ancestry and canonical founder families.
- Normalized game UI icons and established biological paternal/maternal inheritance safeguards.

## Full historical changelog index

Each version below links to the **original English-package record**. The Russian package contains matching version-named records; do not delete or rewrite them just because this summary exists.

- `v2.2.7.4.8` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.8.txt)
- `v2.2.7.4.7` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.7.txt)
- `v2.2.7.4.6` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.6.txt)
- `v2.2.7.4.5` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.5.txt)
- `v2.2.7.4.4` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.4.txt)
- `v2.2.7.4` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.4.txt)
- `v2.2.7.3.1` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.3.1.txt)
- `v2.2.7.3` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.3.txt)
- `v2.2.7.2` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.2.txt)
- `v2.2.7.1` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.1.txt)
- `v2.2.7` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.txt)
- `v2.1.6.9.2` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.9.2.txt)
- `v2.1.6.9.1` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.9.1.txt)
- `v2.1.6.9` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.9.txt)
- `v2.1.6.8.2` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.8.2.txt)
- `v2.1.6.8.1` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.8.1.txt)
- `v2.1.6.8` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.8.txt)
- `v2.1.6.7` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.7.txt)
- `v2.1.6.6` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.6.txt)
- `v2.1.6.5` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.5.txt)
- `v2.1.6.4` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.4.txt)
- `v2.1.6.3` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.3.txt)
- `v2.1.6.2` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.2.txt)
- `v2.1.6` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.6.txt)
- `v2.1.5` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.5.txt)
- `v2.1.4` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.4.txt)
- `v2.1.3` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.3.txt)
- `v2.1.2` — [EN source](Divine_Bloodlines_EN/CHANGELOG_v2.1.2.txt)

Additional integration record: [v2.2.7.2 COMPLETE](Divine_Bloodlines_EN/CHANGELOG_v2.2.7.2_COMPLETE.txt).

Historical static-check reports can be found next to the logs as `VALIDATION_v*.txt`; for example [v2.2.7.4.8 validation](Divine_Bloodlines_EN/VALIDATION_v2.2.7.4.8.txt). **These are not reports of a successful CK2 runtime playtest.**
