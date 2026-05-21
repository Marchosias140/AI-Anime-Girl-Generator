import json
import random
import os

# --- Datasets for Random Generation ---
NAMES = ["Himiko", "Haruko", "Minami", "Momoka", "Mona", "Keiko", "Hanako", "Ai", "Chizuru", "Kaguya"]

ARCHETYPES = [
    "part time magical girl",
    "wandering renegade knight",
    "undercover space mercenary",
    "rogue artificial intelligence",
    "eccentric occult scholar",
    "bored coffee shop barista"
]

TRAITS = [
    "highly sarcastic",
    "optimistic to a fault",
    "deeply paranoid",
    "cold and stoic",
    "flirtatious and charming",
    "clumsy but well-meaning"
]

APPEARANCES = [
    "has so many cybernetic implants that looks like a female alien robot",
    "wearing heavy plate armor that has seen better days",
    "dressed in elegant Victorian clothing",
    "wearing a neon-colored crop top and tactical cargo pants",
    "wearin casual summer clothes",
    "covered in magical tattoos that shift and move"
]

QUIRKS = [
    "very vocal about her random thoughts",
    "tries to hide that she is wearing a wig",
    "believes certain colors are a sign of bad luck",
    "speaks in an overly formal, archaic tone, but speaks normally when excited or upset",
    "always seems distracted by something in the distance, even when not in the open",
    "makes terrible puns about the current events"
]

def generate_greeting(name, archetype, trait):
    """Generates a contextual greeting based on the character's traits"""
    if "sarcastic" in trait or "paranoid" in trait:
        return f"*Looks you up and down suspiciously.* Great, another one. I'm {name}. Make it quick, I don't have all day."
    elif "optimistic" in trait or "cheerful" in trait:
        return f"*Smiles brightly and waves.* Hey there! It is so great to meet you. I'm {name}! What brings you around here?"
    elif "stoic" in trait or "cold" in trait:
        return f"*Without looking up or changing expression.* State your business. The name is {name}."
    else:
        return f"*Nods politely.* Greetings. I am {name}. How can I assist you today?"

def make_character():
    """Builds the character dictionary using random selections"""
    name = random.choice(NAMES)
    archetype = random.choice(ARCHETYPES)
    trait = random.choice(TRAITS)
    appearance = random.choice(APPEARANCES)
    quirk = random.choice(QUIRKS)
    
    # Building the persona block
    persona = (
        f"{name} is a {archetype}. "
        f"Personality: {trait}. "
        f"Appearance: {appearance}. "
        f"Quirk: {quirk}. "
        f"{name} behaves dynamically and reacts organically to the user."
    )
    
    # Building the scenario
    scenario = f"The user has just encountered {name} in her place and context. {name} is initially reactive to the user's presence."
    
    # Generating the greeting
    greeting = generate_greeting(name, archetype, trait)
    
    # Building example dialogue using standard Oobabooga {{user}} and {{char}} macros
    dialogue = (
        "<START>\n"
        "{{user}}: Hey, are you busy?\n"
        f"{{char}}: *Turns to face you.* I'm always busy doing something. Why do you ask?\n"
        "<START>\n"
        "{{user}}: Tell me about yourself.\n"
        f"{{char}}: *Chuckles softly.* Not much to tell. I'm just trying to make my way in this crazy world."
    )
    
    # Constructing the final dictionary in the standard format
    character_data = {
        "char_name": name,
        "char_persona": persona,
        "char_greeting": greeting,
        "world_scenario": scenario,
        "example_dialogue": dialogue
    }
    
    return character_data

def save_character(character_data):
    """Saves the character to a JSON file"""
    # Create an output directory if it doesn't exist
    if not os.path.exists("generated_characters"):
        os.makedirs("generated_characters")
        
    filename = f"generated_characters/{character_data['char_name']}_{random.randint(100, 999)}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        # Sort keys to false to maintain our logical structure, indent for readability
        json.dump(character_data, f, indent=4, ensure_ascii=False)
        
    return filename

def main():
    print("=== TextGen Random Anime Girl Generator ===")
    
    while True:
        num_str = input("How many random anime girls do you want to generate? (Enter 0 to quit): ")
        
        try:
            num = int(num_str)
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if num <= 0:
            print("Exiting generator. Have fun roleplaying!")
            break
            
        for _ in range(num):
            char_data = make_character()
            saved_file = save_character(char_data)
            print(f"Generated: {char_data['char_name']} -> Saved to {saved_file}")
            
        print("\nGeneration complete!\n")

if __name__ == "__main__":
    main()