# Bankroll

Bankroll is a script for Blox Strike. It features a Beutiful UI, legitbot, visuals, and skin changers.

Status: Early Access (expect bugs).

## Usage

```lua
loadstring(game:HttpGet("https://raw.githubusercontent.com/Zylang104/bankroll/main/bankroll.lua"))()
```

1. Inject the script in your executor.
2. Execute the script.
3. Enter the key.

## Key System

For getting the key you need to join the [discord server](https://discord.gg/Pmnk9e6egS).

## Features

### Legitbot
- Aimbot (Smoothness, FOV, Target Part)
- Triggerbot (Hold/Toggle, Delay)
- Checks: Team, Alive, Wall
- Draw FOV

### Visuals
- ESP: Box, Skeleton, Name, Health, Distance, Head Dot, Chams
- World: Flash/Smoke Remover
- Third Person, Speed Graph

### Skin Changer
- Weapon Skins
- Glove Changer
- Knife Changer (it needs the require function, executor like xeno or solara don't have it so you need a high unc executor)

### Misc
- Movement: Auto Bhop, Speedhack
- Anti-Aim
- Anti-Kick (might now work for now needs to be fixed),
- Spectator List
- Config System (Save/Load)

## Requirements

Your executor needs to support:
- `mousemoverel`
- `mouse1click`
- `writefile` / `readfile`
- `getcustomasset` (optional for music at the start)
- `require` (optional if you don't need knife changer)

## Optional Music
If you want some cool music on the intro of the script run the python script on the main branch, you need to put the location of your executor workspace.