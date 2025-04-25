from colorama import *
import random
import os
import sys
import json
import datetime
import numpy as np
import sounddevice as sd
import webbrowser
import pygetwindow as gw
import pyautogui
import time
import traceback
import subprocess
import logging

logging.basicConfig(
    filename=f'gdlg-log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("The program has been started.")
if os.name == 'nt':  # Windows kontrolü
    os.system("attrib +h gdlg-log.log")

init(autoreset=True)

def logError():
    with open("error_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now()}]\n")
        f.write(traceback.format_exc())
        f.write("\n\n")

def main():

    names = ["Celestial Drift", "Quantum Bloom", "Pixel Mirage", "Echo Pulse", "Lunar Tides", "Silent Shatter", "Fractal Bloom", "Plasma Vault", "Eclipse Run", "Voltage Rush",
    "Twilight Prism", "Phantom Gear", "Gravity Twist", "Oblivion Beat", "Frozen Circuit", "Nova Spark", "Abyss Walker", "Crimson Bounce", "Hollow Lights", "Nebula Glitch",
    "Cyber Howl", "Dream Collapse", "Wired Illusion", "Inferno Switch", "Arcane Pulse", "Zenith Drive", "Midnight Delta", "Bitstorm", "Chaos Vector", "Sky Reboot",
    "Phantom Loops", "Retroblast", "Cosmic Fuse", "Blizzard Warp", "Electric Veins", "Shatterpath", "Ignite the Void", "Shadowstream", "Turbo Bloom", "Solar Crush",
    "Darktrace", "Crystal Run", "Flux Reality", "Nebulock", "Astro Swing", "Tempest Code", "Magnetrain", "Dimflash", "Virus Bloom", "Vortex Veil",
    "Stellar Hook", "Sapphire Climb", "Turbulent Glow", "Riftwave", "Meltdown Orbit", "Reactor Bloom", "Frozen Pulse", "Strobe Skies", "Quantum Trail", "Skybreak Nova",
    "Velvet Trigger", "Frosted Leap", "Twister Path", "Silent Delta", "Data Rush", "Aurora Clash", "Twilight Crunch", "Circuit Maze", "Glitchsphere", "Static Rush",
    "Lumina Shift", "Deadbyte", "Neon Reverie", "Hex Drop", "Faded Prism", "Shock Nova", "Binary Dash", "Lightbreaker", "Phase Shift", "Echo Gear",
    "Voiddream", "Icebreaker Rush", "Arc Mirage", "Pixelated Pulse", "Radiant Collapse", "Turbo Spiral", "Skyglitch", "Voltaic Edge", "Prism Ascend", "Polarity Flow",
    "Null Path", "Cyber Crystals", "Gravity Burn", "Twilight Glitch", "Dimensional Bloom", "Starlit Rift", "Dark Nova", "Pixelstorm", "Nightflare", "Silent Revolt"]

    difficultys = ["Effortless", "Recent Tab", "Easy AF", "Easiest", "Auto", "Easy", "Normal", "Hard (4)", "Hard (5)", "Harder (6)", "Harder (7)", "Insane (8)", "Insane (9)", "Easiest Demon", "Easy Demon", "Medium Demon", "Hard Demon", "Insane Demon", "Extreme Demon", "Top 100 Demon", "Top 50 Demon", "Top 25 Demon", "Top 10 Demon", "Top 1 Demon", "...Final Boss..."]

    songs = random.randint(1, 1420812)

    decos = ["So special and revolutionary that it will go down in GD history",
    "Electric blue and black, futuristic, based on laser traps",
    "Red and gold, royal theme with shifting thrones",
    "Muted pastel colors, soft glowing blocks, dreamlike atmosphere",
    "Neon green and gray, tech jungle overrun by wires",
    "Dark purple and silver, ancient alien ruins",
    "Sepia tones, vintage filmstrip effects and flicker",
    "Orange and white, speed tunnel vibe with motion blur",
    "Pink and teal, cyberpunk graffiti walls",
    "Grayscale, pixel art dungeon with traps",
    "Dark red and navy, haunted train ride with flickering lanterns",
    "Turquoise and sand, underwater ruins with air bubbles",
    "Lime and violet, glitchy arcade circuit",
    "Yellow and dark blue, bee hive with honey drips",
    "Bright primary colors, toy factory with mechanical arms",
    "Black and crimson, vampire castle with blood moon",
    "White and transparent, ice temple with crystal reflections",
    "Bronze and moss, steampunk swamp with bubbling gears",
    "Dark green and ash, toxic wasteland with mutated plants",
    "Blue and orange, sky islands with floating propellers",
    "Lavender and silver, space garden with shimmering petals",
    "Red and teal, mecha scrapyard with sparks and smoke",
    "Charcoal and rust, industrial zone with spinning saws",
    "Bright neon rainbow, rhythm-reactive visualizers",
    "Mint and black, time warp distortion theme",
    "Golden yellow and black, Egyptian tomb with traps",
    "Rose and peach, sakura temple with falling petals",
    "Teal and coral, ocean cave with glowing fish",
    "Indigo and pearl, nebula field with slow motion stars",
    "Dark bronze and white, old cathedral with stained glass",
    "Vibrant green and pink, toxic candy factory",
    "Cobalt and magenta, corrupted server theme",
    "Dark orange and violet, volcanic jungle",
    "Sky blue and rose gold, heavenly palace theme",
    "Beige and navy, library full of floating books",
    "Black and electric purple, demon netherworld",
    "Icy blue and chrome, robotics lab in the arctic",
    "Dark yellow and soot, burned village ruins",
    "Red and blue, police vs thief chase scene",
    "Light gray and aqua, snowstorm cityscape",
    "Emerald and black, serpent cave with shifting walls",
    "Gold and red, celebration parade with confetti",
    "Light blue and crimson, high-speed hover car highway",
    "Indigo and cyan, mirrored world with reflection effects",
    "Black and white, chessboard illusion with war pieces",
    "Orange and steel, rocket hangar with countdowns",
    "Silver and dark green, toxic rainstorm forest",
    "Coral and mint, underwater laboratory with leaks",
    "Dark blue and fire red, lava and frost collision theme",
    "Pure white and pale gold, angelic ruins in the sky",
    "Dark green and brown, overgrown castle",
    "Ivory and dark rose, enchanted mirror forest",
    "Electric pink and black, corrupted TV glitch world",
    "Rust and cobalt, ancient mech titan interior",
    "Yellow and gray, abandoned mining operation",
    "Navy and silver, underwater military base",
    "Burnt orange and beige, desert city at sunset",
    "Soft violet and black, dream void of forgotten memories",
    "Sky blue and lemon, cloud theme with air balloons",
    "Deep red and foggy gray, vampire crypt with fog",
    "Crimson and bronze, battle arena with crowd effects",
    "Light green and brown, overgrown temple in ruins",
    "Neon purple and black, rave party with strobe lights",
    "Gray and amber, mountain temple struck by lightning",
    "Light cyan and rose, calm seaside town with waves",
    "Dark pink and indigo, mystical potion lab",
    "Bright red and yellow, circus with dangerous tricks",
    "Green and silver, tech forest controlled by AI",
    "Ash and teal, collapsing tower with falling stones",
    "Pearl white and bronze, ancient angel statue zone",
    "Dark blue and tan, underwater oil rig",
    "Sunset orange and plum, sky bridge during eclipse",
    "Ivory and ice blue, arctic city under the aurora",
    "Brown and teal, archaeological dig site",
    "Black and flame red, fire cult chamber",
    "Cyan and magenta, broken crystal world",
    "Gold and dark gray, ancient time machine lab",
    "Rose gold and mint green, futuristic fashion runway",
    "Midnight blue and indigo, moonlit forest path",
    "Yellow and blood red, cursed treasure vault",
    "Soft brown and cream, cozy coffee shop level",
    "Silver and jet black, corporate cyber maze",
    "Bright green and purple, alien carnival",
    "Steel blue and black, icy abandoned prison",
    "Pastel rainbow, candy dream with marshmallow blocks",
    "Forest green and brown, squirrel village in the trees",
    "Teal and navy, ancient ocean observatory",
    "White and red, snowy battlefield with banners",
    "Fuchsia and pale yellow, magical orb chamber",
    "Orange and blue, lava-powered tech zone",
    "Violet and copper, lightning-charged castle",
    "Blue-gray and white, frozen train ride in the mountains",
    "Black and bright gold, casino vault break-in",
    "Tan and pale green, windmill village on floating cliffs",
    "Pink and lilac, bubble world with bouncy platforms",
    "Brown and maroon, clock tower with moving gears",
    "Dark violet and flame orange, phoenix arena",
    "Navy and coral, underwater ruins with jellyfish glow",
    "Ivory and green, fairy glade with light particles",
    "Black and bronze, gear labyrinth in the dark",
    "Pearl and gold, royal temple on sky stairs"]

    features = ["None",
    "Player shrinks and grows rhythmically with the beat",
    "Every transition includes a screen flip",
    "Entire level in slow-motion",
    "Only one jump orb is used repeatedly with variations",
    "All movement synced to a vocal sample",
    "No background — only solid black void",
    "Gameplay changes based on player’s y-position",
    "Every platform appears at the last second",
    "Only dash orbs, no jumps or pads",
    "Entire level shaped like a creature that the player moves through",
    "Player rides on rotating gears instead of blocks",
    "Each section themed around a different emotion",
    "Level rotates 90 degrees every 5 seconds",
    "Only one color is used, but lighting changes dynamically",
    "Gameplay mimics snake-like movement",
    "Entire level made of invisible objects outlined by particles",
    "All gameplay happens on the ceiling",
    "Reverse gravity is default",
    "Every structure made of text or letters",
    "Each spike is part of a word spelling out a sentence",
    "Visuals react to pitch changes in the music",
    "All obstacles pulse with the music’s bass",
    "Camera zooms in and out constantly",
    "Gameplay relies on fake spikes and mind tricks",
    "Level feels like you're moving downward endlessly",
    "Background constantly morphs into different shapes",
    "Each jump transforms the level’s visuals",
    "Level built around a moving light source",
    "Only uses the cube form but with extreme speed shifts",
    "Level structured as a spiral path inward",
    "Zoomed-in camera throughout the level",
    "Player switches forms every 2 seconds like clockwork",
    "Orbs and pads are disguised as decorations",
    "Entire level shaped like a massive heart",
    "Checkpoint-based puzzle-style gameplay",
    "Every obstacle has a reflection below it",
    "Level changes depending on number of jumps",
    "Platforming while constantly dodging lasers from the sides",
    "Vertical gameplay only — no horizontal movement",
    "Player teleports between mini-scenes",
    "All gameplay is hidden until player gets close",
    "Entire level is a Morse code message",
    "Player shadow lags behind like a ghost trail",
    "Geometry reacts to simulated wind physics",
    "Background tells a progressing story through symbols",
    "Rhythm-based color swaps guide the player",
    "Blocky art style turns into smooth vector mid-level",
    "Mid-level rewind section that replays part of the level backward",
    "Level shrinks in view until it becomes pixelated",
    "Each jump rotates the screen slightly",
    "Falling blocks that change the path dynamically",
    "Enemies actively chase or mirror the player",
    "Uses custom music created for the level only",
    "All spikes slowly fade in, testing memory",
    "Stage is built like a giant machine that activates as you progress",
    "Every object rotates continuously",
    "Camera follows from a weird angle (like diagonal tracking)",
    "Visuals simulate a thunderstorm with flashes and shakes",
    "Obstacles explode into particles when passed",
    "One side of the screen is a mirror of the other",
    "Every block emits a sound effect on contact",
    "Level made of musical instruments that play notes",
    "Spikes bounce up and down in sync with beat",
    "Entire level is grayscale until the drop",
    "Gameplay built entirely from curved custom objects",
    "Story-driven gameplay with pauses and mini-cutscenes",
    "Color palette is randomly generated at runtime",
    "Objects dissolve or reform depending on proximity",
    "No ground or ceiling — player bounces between obstacles",
    "Everything pulses in and out like breathing",
    "Enemies that block the path unless you hit switches",
    "Split-screen — left and right show different timelines",
    "Player leaves a glowing trail that becomes the path",
    "Only uses user coins as platforms",
    "Fake exit paths that loop infinitely",
    "Every gameplay section based on a different geometric shape",
    "Player has to stay inside a moving spotlight to survive",
    "Illusions of depth created with layered parallax",
    "Every block is a character reacting to the music",
    "Level responds to microphone input (via triggers)",
    "Each obstacle rotates around a central axis",
    "Player must dodge falling shapes from the top",
    "Level design mimics old platformer levels (Mario/Sonic style)",
    "Background spells out lyrics of the music",
    "Gameplay syncs with thunder/lightning sound effects",
    "Visual elements mimic an ECG monitor",
    "Camera shakes on every bass kick",
    "Color switches every time the player jumps",
    "Mid-level transformation into a completely new art style",
    "Gameplay reverses horizontally halfway through",
    "Maze-style gameplay where wrong paths lead to resets",
    "Everything made from dots and lines, no solid blocks",
    "Uses non-standard aspect ratio for zoom effect",
    "Entire level is a countdown timer",
    "Orbs that change gravity multiple times in one click",
    "Every block is transparent and pulsates with the song",
    "Gameplay wraps around the screen edges",
    "Level is themed as a single, massive boss fight",
    "Enemies that visually grow the longer you survive",
    "All gameplay occurs inside a spinning shape"]

    vers = ["1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9", "2.0", "2.1", "2.2"]

    durations = random.randint(60, 120)

    objects = random.randint(5100, 40000)

    gameModes = ["Cube", "Ship", "Ball", "UFO", "Wave", "Robot", "Spider", "Swingcopter"]

    portals = ["Up Gravity", "Swap Gravity", "Left Mirror", "Mini-Size", "Dual"]

    randomName = random.choice(names)
    randomDifficulty = random.choice(difficultys)
    randomDeco = random.choice(decos)
    randomFeature = random.choice(features)
    randomVersion = random.choice(vers)
    randomGM = random.sample(gameModes, 5)
    randomPortals = random.choices(portals, k=8)

    def bytebeat(t):
        return t *(7 if (t & 16384) else 5) *(3 - (3 & (t >> 9)) + (3 & (t >> 8)))>> (3 & -t >> (2 if (t & 4096) else 16))| (t >> 3) & 0xFF  # 8-bit çıkış

    duration = 999
    sample_rate = 11025

    t_values = np.arange(0, duration * sample_rate)
    audio_data = np.array([bytebeat(t) for t in t_values], dtype=np.int8)

    def bytebeat2(t):
        return ((8*t if t<35000 else 9*t if t<84000 else 8*t) | ((t>>2)+(13*t if t<67500 else 12*t if t<98000 else 13*t)) | (t>>3) | (t>>5)) if t<129000 else 0 & 0xFF

    duration2 = 999
    sample_rate2 = 8000

    t_values2 = np.arange(0, duration2 * sample_rate2)
    audio_data2 = np.array([bytebeat2(t) for t in t_values2], dtype=np.int8)

    def bytebeat3(t):
        return ((t >> 10 ^ t >> 11) % 5 * ((t >> 14 & 3 ^ t >> 15 & 1) + 1) * t % 99 + ((3 + (t >> 14 & 3) - (t >> 16 & 1)) // 3 * t % 99) & 64) & 0xFF

    duration3 = 999
    sample_rate3 = 8000

    t_values3 = np.arange(0, duration3 * sample_rate3)
    audio_data3 = np.array([bytebeat3(t) for t in t_values3], dtype=np.int8)

    sd.play(audio_data, sample_rate)

    print(Fore.RED + Style.BRIGHT + "   ####    ####    #     ####")
    print(Fore.RED + Style.BRIGHT + "  #    #   #   #   #    #    #")
    print(Fore.GREEN + Style.BRIGHT + " #         #   #  #    #")
    print(Fore.GREEN + Style.BRIGHT + " #        #    #  #    #")
    print(Fore.BLUE + Style.BRIGHT + "#   ###   #   #   #   #   ###")
    print(Fore.BLUE + Style.BRIGHT + "#     #  #    #  #    #     #")
    print(Fore.YELLOW + Style.BRIGHT + "#    #   #   #   #    #    #")
    print(Fore.YELLOW + Style.BRIGHT + " #####   ####    ####  #####\tv1.7.22")
    print(Fore.RESET + "")
    print(Fore.WHITE + Style.BRIGHT + "*****", end=' ')
    print(Fore.WHITE + Style.BRIGHT + "WELCOME TO THE ", end=' ')
    print(Fore.YELLOW + Style.BRIGHT + "GEOMETRY ", end=' ')
    print(Fore.CYAN + Style.BRIGHT + "DASH ", end=' ')
    print(Fore.WHITE + Style.BRIGHT + "LEVEL GENERATOR! ", end=' ')
    print(Fore.WHITE + Style.BRIGHT + "*****", end=' ')
    print(Fore.RESET + "\n")
    print(Fore.WHITE + Style.BRIGHT + "Here is the info about your newly created level: ")
    print("\n")
    print(Fore.WHITE + Style.BRIGHT + "Name:", end=' ')
    print(Fore.RED + Style.BRIGHT + randomName + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "Difficulty:", end=' ')
    print(Fore.GREEN + Style.BRIGHT + randomDifficulty + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "Song:", end=' ')
    print(Fore.BLUE + Style.BRIGHT + "https://www.newgrounds.com/audio/listen/" + str(songs) + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "Deco:", end=' ')
    print(Fore.YELLOW + Style.BRIGHT + randomDeco + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "Distinctive Feature:", end=' ')
    print(Fore.MAGENTA + Style.BRIGHT + randomFeature + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "Version:", end=' ')
    print(Fore.CYAN + Style.BRIGHT + randomVersion + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "Duration:", end=' ')
    print(Fore.LIGHTRED_EX + Style.BRIGHT + str(durations), Fore.LIGHTRED_EX + Style.BRIGHT + "seconds" + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "Objects:", end=' ')
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + str(objects), Fore.LIGHTGREEN_EX + Style.BRIGHT + "objects" + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "Game Modes:", end=' ')
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(randomGM) + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "Portals:", end=' ')
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + ", ".join(randomPortals) + Style.RESET_ALL)
    print("\n")
    print(Fore.WHITE + Style.BRIGHT + "R = Reset Program, C = Credits, S = Shutdown Program, J = Save JSON (new level)")
    print(Fore.WHITE + Style.BRIGHT + "F = Feedback, SS = Screenshot, L = Open All Logfile(s), T = Open Tutorial")
    secim = input(Fore.WHITE + Style.BRIGHT + "Make your choice: ").upper()

    def restartProgram():
        python = sys.executable
        os.execv(python, [python] + sys.argv)

    def saveJSON():
        data = {
            "name": randomName,
            "difficulty": randomDifficulty,
            "songID": songs,
            "deco": randomDeco,
            "feature": randomFeature,
            "version": randomVersion,
            "duration": durations,
            "object": objects,
            "gameMode": ", ".join(randomGM),
            "portal": ", ".join(randomPortals),
            "timestamp": datetime.datetime.now().isoformat()
        }

        fileName = f"gdlg_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(fileName, "w", encoding="utf-8") as File:
            json.dump(data, File, indent=4, ensure_ascii=False)


    def screenshot(filename=f"gdlg_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"):
        titles = ["cmd", "Python", "Terminal"]

        for title in titles:
            windows = gw.getWindowsWithTitle(title)
            if windows:
                win = windows[0]
                try:
                    win.activate()
                    time.sleep(1)
                    x, y = win.left, win.top
                    w, h = win.width, win.height
                    screenshot = pyautogui.screenshot(region=(x, y, w, h))
                    screenshot.save(filename)
                    print(Fore.GREEN + Style.BRIGHT + f"Screenshot saved: {filename}")
                    input(Fore.WHITE + Style.BRIGHT + "")
                    return True
                except Exception as e:
                    print(Fore.RED + Style.BRIGHT + "Error:", e)
                    input(Fore.WHITE + Style.BRIGHT + "")
                    return False
        print(Fore.RED + Style.BRIGHT + "Console window not found.")
        input(Fore.WHITE + Style.BRIGHT + "")
        return False
    
    def openLog():
        print(Fore.GREEN + Style.BRIGHT + "All files ending with .log in the folder will be opened.")
        folder = os.getcwd()
        logFiles = [f for f in os.listdir(folder) if f.endswith('.log')]
        
        for File in logFiles:
            filePath = os.path.join(folder, File)
            try:
                subprocess.Popen(['notepad.exe', filePath])
            except Exception as e:
                print(Fore.RED + Style.BRIGHT + f"Could not open {File} with Notepad: {e}")

    if secim == "R":
        restartProgram()
    elif secim == "C":
        print("\n")
        print(Fore.RED + Style.BRIGHT + "Main Coder: sxdu.dev (discord)")
        print(Fore.CYAN + Style.BRIGHT + "Debug / Additional Coder: ChatGPT")
        print(Fore.BLACK + Style.BRIGHT + "Tester: myniw_guels (discord)")
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "S":
        sys.exit()
    elif secim == "J":
        saveJSON()
        print(Fore.GREEN + Style.BRIGHT + "Done!")
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "F":
        webbrowser.open("Resources\\feedback.html")
        sd.stop()
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "SS":
        screenshot()
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
    elif secim == "L":
        openLog()
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "T":
        webbrowser.open("Resources\\tutorial.html")
        sd.stop()
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "1":
        sd.stop()
        sd.play(audio_data, sample_rate)
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "2":
        sd.stop()
        sd.play(audio_data2, sample_rate2)
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "3":
        sd.stop()
        sd.play(audio_data3, sample_rate3)
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "NAME":
        print(Fore.WHITE + Style.BRIGHT + "Name:", end=' ')
        print(Fore.RED + Style.BRIGHT + random.choice(names))
        print(Fore.WHITE + Style.BRIGHT + "Name:", end=' ')
        print(Fore.RED + Style.BRIGHT + random.choice(names))
        print(Fore.WHITE + Style.BRIGHT + "Name:", end=' ')
        print(Fore.RED + Style.BRIGHT + random.choice(names))
        print(Fore.WHITE + Style.BRIGHT + "Name:", end=' ')
        print(Fore.RED + Style.BRIGHT + random.choice(names))
        print(Fore.WHITE + Style.BRIGHT + "Name:", end=' ')
        print(Fore.RED + Style.BRIGHT + random.choice(names))
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "DIFF":
        print(Fore.WHITE + Style.BRIGHT + "Difficulty:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(difficultys))
        print(Fore.WHITE + Style.BRIGHT + "Difficulty:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(difficultys))
        print(Fore.WHITE + Style.BRIGHT + "Difficulty:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(difficultys))
        print(Fore.WHITE + Style.BRIGHT + "Difficulty:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(difficultys))
        print(Fore.WHITE + Style.BRIGHT + "Difficulty:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(difficultys))
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "SONG":
        print(Fore.WHITE + Style.BRIGHT + "Song:", end=' ')
        print(Fore.BLUE + Style.BRIGHT + "https://www.newgrounds.com/audio/listen/" + str(random.randint(1, 1420812)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Song:", end=' ')
        print(Fore.BLUE + Style.BRIGHT + "https://www.newgrounds.com/audio/listen/" + str(random.randint(1, 1420812)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Song:", end=' ')
        print(Fore.BLUE + Style.BRIGHT + "https://www.newgrounds.com/audio/listen/" + str(random.randint(1, 1420812)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Song:", end=' ')
        print(Fore.BLUE + Style.BRIGHT + "https://www.newgrounds.com/audio/listen/" + str(random.randint(1, 1420812)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Song:", end=' ')
        print(Fore.BLUE + Style.BRIGHT + "https://www.newgrounds.com/audio/listen/" + str(random.randint(1, 1420812)) + Style.RESET_ALL)
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "DECO":
        print(Fore.WHITE + Style.BRIGHT + "Deco:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(decos))
        print(Fore.WHITE + Style.BRIGHT + "Deco:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(decos))
        print(Fore.WHITE + Style.BRIGHT + "Deco:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(decos))
        print(Fore.WHITE + Style.BRIGHT + "Deco:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(decos))
        print(Fore.WHITE + Style.BRIGHT + "Deco:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(decos))
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "FTR":
        print(Fore.WHITE + Style.BRIGHT + "Distinctive Feature:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(features))
        print(Fore.WHITE + Style.BRIGHT + "Distinctive Feature:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(features))
        print(Fore.WHITE + Style.BRIGHT + "Distinctive Feature:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(features))
        print(Fore.WHITE + Style.BRIGHT + "Distinctive Feature:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(features))
        print(Fore.WHITE + Style.BRIGHT + "Distinctive Feature:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(features))
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "VER":
        print(Fore.WHITE + Style.BRIGHT + "Version:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(vers))
        print(Fore.WHITE + Style.BRIGHT + "Version:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(vers))
        print(Fore.WHITE + Style.BRIGHT + "Version:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(vers))
        print(Fore.WHITE + Style.BRIGHT + "Version:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(vers))
        print(Fore.WHITE + Style.BRIGHT + "Version:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + random.choice(vers))
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "DUR":
        print(Fore.WHITE + Style.BRIGHT + "Duration:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + str(random.randint(60, 120)))
        print(Fore.WHITE + Style.BRIGHT + "Duration:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + str(random.randint(60, 120)))
        print(Fore.WHITE + Style.BRIGHT + "Duration:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + str(random.randint(60, 120)))
        print(Fore.WHITE + Style.BRIGHT + "Duration:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + str(random.randint(60, 120)))
        print(Fore.WHITE + Style.BRIGHT + "Duration:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + str(random.randint(60, 120)))
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "OBJ":
        print(Fore.WHITE + Style.BRIGHT + "Objects:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + str(random.randint(5100, 40000)))
        print(Fore.WHITE + Style.BRIGHT + "Objects:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + str(random.randint(5100, 40000)))
        print(Fore.WHITE + Style.BRIGHT + "Objects:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + str(random.randint(5100, 40000)))
        print(Fore.WHITE + Style.BRIGHT + "Duration:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + str(random.randint(5100, 40000)))
        print(Fore.WHITE + Style.BRIGHT + "Objects:", end=' ')
        print(Fore.GREEN + Style.BRIGHT + str(random.randint(5100, 40000)))
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    elif secim == "GM":
        print(Fore.WHITE + Style.BRIGHT + "Game Modes:", end=' ')
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(random.sample(gameModes, 5)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Game Modes:", end=' ')
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(random.sample(gameModes, 5)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Game Modes:", end=' ')
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(random.sample(gameModes, 5)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Game Modes:", end=' ')
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(random.sample(gameModes, 5)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Game Modes:", end=' ')
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(random.sample(gameModes, 5)) + Style.RESET_ALL)
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
    elif secim == "PORTAL":
        print(Fore.WHITE + Style.BRIGHT + "Portals:", end=' ')
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(random.choices(portals, k=8)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Portals:", end=' ')
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(random.choices(portals, k=8)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Portals:", end=' ')
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(random.choices(portals, k=8)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Portals:", end=' ')
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(random.choices(portals, k=8)) + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Portals:", end=' ')
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(random.choices(portals, k=8)) + Style.RESET_ALL)
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
    elif secim == "ROPOPO":
        sd.stop()
        time.sleep(1)
        print(Fore.RED + Style.BRIGHT + "Huh? Wym?")
        time.sleep(1)
        print(Fore.RED + Style.BRIGHT + "Oh K, I got it. Here you go.")
        time.sleep(1)
        webbrowser.open("Resources\\ee.html")
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()
    else:
        print(Fore.RED + Style.BRIGHT + "Improper use.")
        input(Fore.WHITE + Style.BRIGHT + "")
        print(Fore.GREEN + Style.BRIGHT + "The program will restart.")
        restartProgram()

if __name__ == "__main__":
    try:
        main()
    except Exception:
        logError()