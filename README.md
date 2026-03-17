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

Gemini said
Here is everything you need for your final document and your Python file, all consolidated in one place so you can easily copy and paste it right now.

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



Part 4: Reflection and Submission
Reflection:
My rule-based system, the D&D Class Recommender, operates using a nested decision tree built entirely on IF-THEN-ELSE heuristics. It functions by prompting the user for string inputs via the terminal, converting those inputs to lowercase to avoid case-sensitivity errors, and passing them through specific conditional logic branches. Because there is no machine learning or natural language processing involved, the system relies entirely on the user typing the exact predefined keywords (like "melee" or "magic"). It perfectly highlights the nature of early AI: highly logical, predictable, and functional, but completely rigid and incapable of inferring meaning outside of its strict parameters.

While collaborating with the AI assistant to design this, the main challenge was keeping the scope narrow. Modern AI is so used to generating expansive, complex solutions that I had to specifically prompt it to tone down the logic to simple if/elif/else statements, ensuring it didn't try to introduce advanced data structures or predictive text matching. Getting the fallback rules (the else statements) correct was also crucial; because rule-based systems are fragile, the AI and I had to ensure the program wouldn't crash if a user typed "sword" instead of "melee," but would instead output a formatted error message.

ELSE -> "I didn't understand that input. Let's roll a Nat 20 on reading comprehension and try again."

Test cases 
PS A:\Dnd_AI_Project> & C:/Users/Admin/AppData/Roaming/uv/python/cpython-3.14.3-windows-x86_64-none/python.exe a:/Dnd_AI_Project/main.py
Welcome to the Adventurer's Guild!
Let's find the perfect D&D class for your next campaign.

Do you prefer 'melee' combat, casting 'magic', or 'both'? melee
Do you prefer to act as a heavy 'tank' or use 'stealth'? tank

Result: You should play a BARBARIAN! Grab a greataxe and start raging.
PS A:\Dnd_AI_Project> & C:/Users/Admin/AppData/Roaming/uv/python/cpython-3.14.3-windows-x86_64-none/python.exe a:/Dnd_AI_Project/main.py
Welcome to the Adventurer's Guild!
Let's find the perfect D&D class for your next campaign.

Do you prefer 'melee' combat, casting 'magic', or 'both'? magic
Does your magic come from intense 'study' or a magical 'bloodline'? study

Result: You should play a WIZARD! Time to hit the spellbooks.
PS A:\Dnd_AI_Project> & C:/Users/Admin/AppData/Roaming/uv/python/cpython-3.14.3-windows-x86_64-none/python.exe a:/Dnd_AI_Project/main.py
Welcome to the Adventurer's Guild!
Let's find the perfect D&D class for your next campaign.

Do you prefer 'melee' combat, casting 'magic', or 'both'? i want to be a pizza

Error: I didn't understand that combat style. Let's roll a Nat 20 on reading comprehension and try again.
PS A:\Dnd_AI_Project> 

