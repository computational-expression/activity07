# Activity 7: Halloween Parade Candy Calculator

## Learning Objectives
- Write functions from scratch using parameters and return values
- Practice function design and organization principles
- Apply mathematical calculations within functions
- Use functions to solve real-world problems
- Understand function scope and variable passing
- Practice collaborative Git workflow with teammates

## Overview
Inspired by Meadville's **58th Annual Halloween Parade** with this year's "Under the Sea" theme, you are creating a **Halloween Parade Candy Calculator** to help parade participants and spectators plan their Halloween parade experience! This activity focuses on writing functions from scratch to handle parade logistics, candy distribution from floats, and crowd planning.

**🤝 COLLABORATIVE ACTIVITY:** Work in pairs or small groups (3 students) to complete this activity.

## The Halloween Parade Challenge
Your group is participating in Meadville's Halloween Parade and wants a digital tool to help plan your float and candy distribution. In this parade, **participants on floats and in costumes give out candy to the crowd** watching along the parade route. Your group needs to calculate:

- How much candy to bring on their float for the crowd
- Calculate costs for float decorations and costumes
- Estimate how many people will be watching along the route
- Plan candy distribution strategy during the parade
- Compare different candy purchasing options
- Create a summary of their parade participation

## Group Collaboration Structure

### 🎯 **Function Development & Collaboration (Individual → Team of 2-3)**
- **Individual:** Each person picks 2-3 different functions to implement on their own computer
- **Git Collaboration:** Push and pull code as you work together to complete all 6 functions
- **Code Review:** Test each other's functions and provide feedback

## Required Functions to Create

Write these 6 Halloween parade-themed functions from scratch. Each function should be **tested individually** as you write it.

### 1. `calculate_candy_needed(spectators, pieces_per_person)`
**Purpose:** Calculate the total number of candy pieces needed based on expected crowd size and how many pieces to give each person. Multiply the number of spectators by pieces per person to get the total.

### 2. `pieces_to_bags(total_pieces, pieces_per_bag)`
**Purpose:** Convert individual candy pieces into the number of bags needed for easy purchasing and loading onto your float. Divide total pieces by pieces per bag (typically 50 pieces per bag).

### 3. `calculate_total_cost(decoration_cost, costume_cost, candy_cost, tax_rate)`
**Purpose:** Calculate the total cost of participating in the parade including decorations, costumes, candy, and tax. Add all costs together, then multiply by tax rate to get total cost.

### 4. `estimate_total_spectators(route_blocks, spectators_per_block)`
**Purpose:** Estimate how many people will be watching along the entire parade route. Multiply the route length in blocks by average number of spectators per block.

### 5. `compare_candy_deals(option1_cost, option1_pieces, option2_cost, option2_pieces)`
**Purpose:** Compare two different candy purchasing options to find which gives you more candy for your money. Calculate cost per piece for each option and recommend the better deal.

### 6. `create_parade_summary(float_theme, total_spectators, total_candy, total_cost)`
**Purpose:** Create a nicely formatted text summary of your parade participation including your float theme, crowd size, candy amount, and total cost with the "Under the Sea" theme reference.

## Implementation Guidelines

### Function Design Principles
- **Single Purpose**: Each function does one specific parade calculation
- **Clear Names**: Function names describe exactly what they calculate
- **Parameters**: Use parameters to make functions flexible for different parade scenarios
- **Return Values**: Always return calculated results
- **Documentation**: Include docstrings explaining what each function does

### Testing Your Functions

Test each function with multiple inputs to ensure it works correctly. Try different values and make sure you get the expected results.

## Example Program Output

```
🎃 === Halloween Parade Candy Calculator === 🎃
Welcome to the Meadville Parade Planner!
This year's parade theme: "Under the Sea"

🌊 Enter your float details:
Float theme: Mermaid Kingdom
Parade route length (blocks): 8
Candy pieces per spectator: 2
Decoration budget: $50.00
Costume budget: $30.00
Candy budget: $25.00

=== 👥 Crowd Estimation ===
Estimated spectators along route: 200 people
Total candy pieces needed: 400 pieces
Candy bags to buy: 8.0 bags

=== 💰 Cost Breakdown ===
Float decorations: $50.00
Costumes: $30.00
Candy: $25.00
Subtotal: $105.00
Tax (6%): $6.30
Total cost: $111.30

=== 🍬 Candy Deal Comparison ===
Option 1: $15.00 for 150 pieces ($0.10 per piece)
Option 2: $20.00 for 300 pieces ($0.067 per piece)
💡 Best deal: Option 2 saves you money at $0.067 per piece!

=== 🌊 Parade Summary ===
🧜‍♀️ Under the Sea: Mermaid Kingdom Float
👥 Ready for 200 spectators with 400 candy pieces
💰 Total parade cost: $111.30
🎃 Meadville Halloween Parade - here we come!

Ready for the Meadville Halloween Parade! 🎃🌊👻
```

## 🎨 Adding Emojis to Your Program

Make your output festive and fun with emojis! Here's how to find and use them:

### **Where to Find Emojis:**
1. **Mac Users:** Press `Control + Command + Space` to open emoji picker
2. **Windows Users:** Press `Windows key + .` (period) to open emoji panel  
3. **Online:** Visit [emojipedia.com](https://emojipedia.com) or [getemoji.com](https://getemoji.com)
4. **Copy & Paste:** Find emojis online and copy them directly into your code

### **Halloween & Sea Theme Emojis:**
```python
# Halloween emojis
🎃 👻 🦇 🍬 🍭 🧙‍♀️ 🧛‍♂️ 🕷️ 🕸️ 

# Under the Sea emojis  
🌊 🧜‍♀️ 🧜‍♂️ 🐠 🐟 🦈 🐙 🦀 🐚 ⭐ 🏴‍☠️ 🚢

# Money & calculation emojis
💰 💵 💳 🧮 📊 📈 💡 ✨

# People & celebration emojis
👥 👨‍👩‍👧‍👦 🎉 🎊 🏆 🎯
```

### **How to Use Emojis in Your Code:**
```python
print("🎃 Welcome to the Halloween Calculator! 🎃")
print(f"💰 Total cost: ${total_cost:.2f}")
print(f"🍬 Candy needed: {candy_pieces} pieces")
```

### **Pro Tips for Emojis:**
- **Don't overuse** - A few well-placed emojis are better than emoji overload
- **Be consistent** - Use the same emoji for the same type of information
- **Test on different systems** - Some emojis may not display on all computers
- **Use in output only** - Don't put emojis in variable names or comments

## 🚀 Getting Started

The `main.py` file already includes a **complete main function** that shows you exactly how to:

1. **Collect user input** for float details and budgets
2. **Call each function** with the proper parameters  
3. **Display results** in a professional, formatted way
4. **Use emojis effectively** throughout the output

### **Your Task:**
- **Implement the 6 functions** - The main function calls are already written for you!
- **Follow the function signatures** - Parameter names and types are provided
- **Test each function** - The main function will help you see if your functions work
- **Run the program** - You can test your progress as you implement each function

### **Example Function Implementation:**
```python
def calculate_candy_needed(spectators, pieces_per_person):
    """Calculate total candy pieces needed for parade spectators"""
    return spectators * pieces_per_person

def pieces_to_bags(total_pieces, pieces_per_bag):
    """Convert candy pieces to number of bags needed"""
    return total_pieces / pieces_per_bag
```

## Steps to Complete

### 🔄 **Git Setup & Collaboration**
1. **One team member clicks** the assignment link and creates a team
2. **Other team members click** the same assignment link and join the existing team
3. **All members clone** the team repository to their computers using the provided Git URL
4. **Work directly on main branch** for simplicity in this collaborative activity

### 💻 **Function Implementation with Git**
1. **Divide functions** - each person takes 2-3 functions initially and announces which ones
2. **Work on separate computers** - implement your assigned functions
3. **Push your functions** - commit and push your completed functions
4. **Pull and integrate** - pull others' code and work together on remaining functions
5. **Test together** - run the complete program and debug as a group

## Git Collaboration Tips

**Basic Git Workflow for this Activity:**
1. **Before starting work:** `git pull` or `git pull origin main`
2. **After completing functions:** `git add .` → `git commit -m "message"` → `git push`
3. **When integrating:** `git pull` to get teammates' work
4. **If conflicts occur:** Work together to resolve them - this is great practice!

**Communication is Key:**
- **Announce** which functions you are working on to avoid conflicts
- **Coordinate** who pushes first when multiple people finish at the same time
- **Help each other** with Git commands if someone gets stuck

## What to Submit

- `src/main.py` - Your complete Halloween Parade Candy Calculator with all 6 functions
- Each function should work correctly and include proper docstrings
- Your main program should demonstrate using all the functions with a parade theme

## Grading Rubric

This activity is assessed on a **pass/fail basis**:

- **1 point**: Awarded if 50% or more of the functions are implemented correctly (3 or more working functions)
- **0 points**: Awarded if less than 50% of the functions work correctly

## Tips for Success

- **Start with one function at a time** - don't try to write everything at once
- **Test each function immediately** after writing it with different inputs
- **Use descriptive variable names** in your functions (e.g., `total_spectators` not `x`)
- **Include helpful docstrings** explaining what each function does and its parameters
- **Remember to return values** from your calculation functions
- **Use the `round()` function** to make output look cleaner (e.g., `round(result, 2)` for 2 decimal places)
- **Add emojis strategically** - see the emoji guide above for ideas!
- **Collaborate effectively** - communicate who's working on what functions
- **Test your Git workflow** early to avoid last-minute issues

## Local Halloween Connection

This calculator is inspired by Meadville's 58th Annual Halloween Parade that just happened on October 25th! The parade features floats and costumed participants who throw candy to spectators lining the parade route. This year's theme "Under the Sea" means lots of mermaid, pirate, and sea creature floats distributing candy to excited crowds along Diamond Park. Use sea-themed float ideas like underwater kingdoms, pirate ships, or coral reefs in your examples!
