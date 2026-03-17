# Rule-based-Ai
Part 1: Prompting the AI for Project Ideas
Three Project Ideas:

The D&D Class Recommender (Recommendation System)

What it does: A text-based assistant that asks the user a series of questions about their preferred combat style and personality, then recommends the perfect Dungeons & Dragons class to play.

How it works using rules: It uses a decision tree of IF-THEN statements based on keyword inputs. For example, if the user inputs "magic" and then "study," it outputs "Wizard." If they input "melee" and "stealth," it outputs "Rogue."

The Bodybuilding Split Generator (Diagnostic/Planning Tool)

What it does: An assistant that asks the user about their experience level and how many days a week they can train, then recommends an optimal workout split.

How it works using rules: It matches integer inputs (days per week) and string inputs (beginner/advanced) to hardcoded schedules. For instance, IF days == 6 AND level == "advanced", THEN output = "Push/Pull/Legs Split".

The Anime Watchlist Guru (Recommendation System)

What it does: A chatbot that suggests a specific anime series based on the user's current mood, preferred genre, and time commitment.

How it works using rules: It filters a small, hardcoded database using conditionals. IF genre == "Isekai" AND length == "short", THEN output = "Chillin' in Another World".

Chosen Project & Justification:
I chose the D&D Class Recommender. I am a big fan of the game, and translating the logic of character creation into a rule-based Python script feels like a natural, fun way to understand early AI. It perfectly demonstrates how a system can take human preferences and map them to specific outcomes using simple heuristics, without needing complex machine learning.

Part 2: Designing Your Rule-Based System
Rules and Logic (Pseudocode):

Prompt 1: "Do you prefer 'melee' combat, 'magic', or a mix of 'both'?"

Logic Tree 1 (Melee):

IF 'melee' -> Prompt: "Do you prefer to 'tank' damage or use 'stealth'?"

IF 'tank' -> Recommend: Barbarian

IF 'stealth' -> Recommend: Rogue

Logic Tree 2 (Magic):

IF 'magic' -> Prompt: "Does your magic come from 'study' or a 'bloodline'?"

IF 'study' -> Recommend: Wizard

IF 'bloodline' -> Recommend: Sorcerer

Logic Tree 3 (Both):

IF 'both' -> Prompt: "Are you sworn to a 'god' or to 'nature'?"

IF 'god' -> Recommend: Paladin

IF 'nature' -> Recommend: Ranger

Fallback Rule:

ELSE -> "I didn't understand that input. Let's roll a Nat 20 on reading comprehension and try again."
