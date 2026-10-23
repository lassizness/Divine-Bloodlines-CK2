import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGUAGES = ("EN", "RU")


def source(language, path):
    return (ROOT / f"Divine_Bloodlines_{language}" / path).read_bytes().decode("latin1")


class DivineLogicRegressions(unittest.TestCase):
    def test_all_affected_scripts_have_balanced_braces(self):
        paths = (
            "common/on_actions/divine_blood_on_actions.txt",
            "events/divine_blood_v2168.txt",
            "events/divine_blood_core.txt",
            "events/divine_blood_founders.txt",
            "events/divine_blood_v215.txt",
            "events/divine_blood_v227.txt",
            "events/divine_blood_v2272_relics.txt",
            "decisions/divine_blood_v2272_relics.txt",
        )
        for language in LANGUAGES:
            for path in paths:
                with self.subTest(language=language, path=path):
                    text = source(language, path)
                    text = re.sub(r"#[^\n]*", "", text)
                    self.assertEqual(text.count("{"), text.count("}"))

    def test_old_save_genetics_are_not_recomputed_yearly(self):
        for language in LANGUAGES:
            with self.subTest(language=language):
                hooks = source(language, "common/on_actions/divine_blood_on_actions.txt")
                yearly = next(line for line in hooks.splitlines() if line.startswith("on_yearly_pulse"))
                self.assertNotIn("DBV2.1105", yearly)
                self.assertIn("DBV2.1291", hooks)
                migration = source(language, "events/divine_blood_v2168.txt")
                compatibility = migration.split("id = DBV2.1105", 1)[1]
                self.assertIn("character_event = { id = DBV2.1291 }", compatibility)
                self.assertNotIn("character_event = { id = DBV2.1290 }", compatibility)
                resolver = source(language, "events/divine_blood_v22745.txt")
                self.assertIn("NOT = { has_character_flag = db_v22745_inheritance_repaired }", resolver)

    def test_mixed_divinity_keeps_paternal_religion(self):
        for language in LANGUAGES:
            with self.subTest(language=language):
                text = source(language, "events/divine_blood_core.txt")
                religion = text.split("id = DBV2.70", 1)[1].split("id = DBV2.30", 1)[0]
                self.assertIn("db_has_active_olympian_blood_trigger = yes NOT = { db_has_active_norse_blood_trigger = yes }", religion)
                self.assertIn("db_has_active_norse_blood_trigger = yes NOT = { db_has_active_olympian_blood_trigger = yes }", religion)
                self.assertIn("father_even_if_dead = { has_character_flag = db_pantheon_norse }", religion)
                self.assertIn("father_even_if_dead = { has_character_flag = db_pantheon_hellenic }", religion)
                self.assertLess(religion.index("father_even_if_dead = { has_character_flag = db_pantheon_norse }"), religion.index("religion = norse_pagan religion = norse_pagan_reformed"))

    def test_zeus_aegis_is_searchable_not_granted_at_spawn(self):
        for language in LANGUAGES:
            with self.subTest(language=language):
                founder = source(language, "events/divine_blood_founders.txt")
                self.assertIn("add_artifact = db_thunderbolt_of_zeus", founder)
                self.assertNotIn("add_artifact = db_aegis_of_zeus", founder)
                decision = source(language, "decisions/divine_blood_decisions.txt")
                self.assertIn("db_seek_aegis", decision)

    def test_draupnir_uniqueness_shared_across_old_and_new_search(self):
        for language in LANGUAGES:
            with self.subTest(language=language):
                decision = source(language, "decisions/divine_blood_v2272_relics.txt")
                line = next(line for line in decision.splitlines() if line.strip().startswith("db_seek_draupnir ="))
                self.assertIn("has_global_flag = db_draupnir_created", line)
                self.assertIn("has_global_flag = db_relic_draupnir_created", line)
                self.assertIn("any_character = { has_artifact = db_draupnir }", line)

                event = source(language, "events/divine_blood_v2272_relics.txt")
                award = next(line for line in event.splitlines() if "id = DBV2.1255" in line)
                self.assertIn("NOT = { has_global_flag = db_draupnir_created }", award)
                self.assertIn("NOT = { has_global_flag = db_relic_draupnir_created }", award)
                self.assertIn("set_global_flag = db_draupnir_created", award)
                self.assertIn("set_global_flag = db_relic_draupnir_created", award)

                registry = source(language, "events/divine_blood_v215.txt")
                self.assertIn("clr_global_flag = db_draupnir_created clr_global_flag = db_relic_draupnir_created", registry)
                recovery = source(language, "events/divine_blood_v227.txt")
                self.assertIn("has_artifact = db_draupnir } set_global_flag = db_draupnir_created set_global_flag = db_relic_draupnir_created", recovery)

    def test_landless_founder_reconquest_works_with_titular_title(self):
        for language in LANGUAGES:
            with self.subTest(language=language):
                text = source(language, "events/divine_blood_v227.txt")
                for event_id in ("DBV2.1203", "DBV2.1265"):
                    block = text.split("id = " + event_id, 1)[1].split("immediate = {", 1)[0]
                    self.assertIn("OR = { is_landed = no num_of_count_titles_in_realm = 0 }", block)
                restore = text.split("id = DBV2.1270", 1)[1].split("immediate = {", 1)[0]
                self.assertIn("num_of_count_titles_in_realm > 0", restore)

    def test_utf8_bom_removed_from_english_scripts(self):
        paths = (
            "events/divine_blood_core.txt",
            "events/divine_blood_v2168.txt",
            "common/scripted_triggers/divine_blood_triggers.txt",
            "decisions/divine_blood_v227_decisions.txt",
        )
        for path in paths:
            with self.subTest(path=path):
                data = (ROOT / "Divine_Bloodlines_EN" / path).read_bytes()
                self.assertFalse(data.startswith(b"\xef\xbb\xbf"))

    def test_russian_founder_names_remain_cp1251(self):
        data = (ROOT / "Divine_Bloodlines_RU" / "events/divine_blood_founders.txt").read_bytes()
        self.assertIn("Зевс".encode("cp1251"), data)
        self.assertIn("Фригг".encode("cp1251"), data)


if __name__ == "__main__":
    unittest.main()
