# D&D Class Recommender - A Rule-Based AI System

def recommend_class():
    print("Welcome to the Adventurer's Guild!")
    print("Let's find the perfect D&D class for your next campaign.\n")

    # First layer of rule-based logic
    combat_style = input("Do you prefer 'melee' combat, casting 'magic', or 'both'? ").strip().lower()

    if combat_style == 'melee':
        # Second layer for melee path
        tactics = input("Do you prefer to act as a heavy 'tank' or use 'stealth'? ").strip().lower()
        if tactics == 'tank':
            print("\nResult: You should play a BARBARIAN! Grab a greataxe and start raging.")
        elif tactics == 'stealth':
            print("\nResult: You should play a ROGUE! Stick to the shadows and roll for sneak attack.")
        else:
            print("\nError: I didn't recognize that tactic. The Guild master kicks you out.")

    elif combat_style == 'magic':
        # Second layer for magic path
        source = input("Does your magic come from intense 'study' or a magical 'bloodline'? ").strip().lower()
        if source == 'study':
            print("\nResult: You should play a WIZARD! Time to hit the spellbooks.")
        elif source == 'bloodline':
            print("\nResult: You should play a SORCERER! Your innate magic is ready to burst.")
        else:
            print("\nError: Unknown magic source. Your spell fizzles.")

    elif combat_style == 'both':
        # Second layer for hybrid path
        allegiance = input("Are you sworn to a 'god' or to 'nature'? ").strip().lower()
        if allegiance == 'god':
            print("\nResult: You should play a PALADIN! Smite your foes with divine justice.")
        elif allegiance == 'nature':
            print("\nResult: You should play a RANGER! The wilderness is your domain.")
        else:
            print("\nError: Unknown allegiance. You wander the tavern aimlessly.")

    else:
        # Fallback heuristic for invalid inputs
        print("\nError: I didn't understand that combat style. Let's roll a Nat 20 on reading comprehension and try again.")

# Run the system
if __name__ == "__main__":
    recommend_class()