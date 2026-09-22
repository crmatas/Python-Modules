from alchemy import grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
elements = ("Earth wind and fire")
print("Testing record light spell: "
      f"{grimoire.light_spell_record('Fantasy', elements)}")
