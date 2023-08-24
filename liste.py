def entferne_wiederholungen(wortliste):
    eindeutige_woerter = []
    wiederholungen = []

    for wort in wortliste:
        if wort in eindeutige_woerter:
            wiederholungen.append(wort)
        else:
            eindeutige_woerter.append(wort)

    for wort in wiederholungen:
        wortliste.remove(wort)

    return wortliste

def formatiere_liste_als_python_code(wortliste):
    formatierter_code = "["
    for wort in wortliste:
        formatierter_code += f'"{wort}", '
    formatierter_code = formatierter_code.rstrip(', ')
    formatierter_code += "]"
    return formatierter_code

# Beispiel
wortliste = ['development', 'software', 'internet', 'computer', 'interaction', 'collaboration', 'project', 
             'enthusiasm', 'opportunity', 'knowledgeable', 'technology', 'innovation', 'knowledge', 'programming', 
             'learning', 'creative', 'solution', 'experience', 'developer', 'framework', 'industry', 'algorithm', 
             'education', 'coding', 'web', 'application', 'interface', 'resource', 'function', 'analysis', 'practice', 
             'challenge', 'effort', 'progress', 'advancement', 'curiosity', 'achievement', 'passion', 'together', 
             'enthusiastic', 'communication', 'community', 'efficiency', 'inspiration', 'platform', 'Apple', 'Table', 
             'Elephant', 'Guitar', 'Window', 'Ocean', 'Butterfly', 'Candle', 'Diamond', 'Sunshine', 'Mountain', 'Rainbow', 
             'Keyboard', 'Flower', 'Moonlight', 'Coffee', 'Dolphin', 'Castle', 'Pillow', 'Firefly', 'Telescope', 'River', 
             'Sandcastle', 'Starfish', 'Turtle', 'Backpack', 'Lemonade', 'Whisper', 'Adventure', 'Balloon', 'Dragonfly', 'Echo', 
             'Friendship', 'Harmony', 'Island', 'Jellyfish', 'Koala', 'Lighthouse', 'Meadow', 'Nightingale', 'Octopus', 'Penguin', 
             'Quilt', 'Seashell', 'Thunder', 'Umbrella', 'Vacation', 'Waterfall', 'Xylophone']
neue_liste = entferne_wiederholungen(wortliste)
print(neue_liste)
