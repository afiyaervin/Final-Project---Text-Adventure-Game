# Text Adventure Game

## Introduction
For this project, you'll participate in one of the oldest and most enduring video game genres in history: the text adventure game. You can find some examples of good text adventure games here: https://www.makeuseof.com/tag/browser-text-based-games/

## Objectives
The functionality required from this project is:

- Allow the user to access a help menu whenever they want
- Allow the user to pick up 1 or more items and store them in their inventory
- Allow the user to choose between multiple options
- Have some sort of storyline and ending (this can be as simple or complex as you'd like)


You may find that some of the work for one feature overlaps with some of the work for another feature. In that case, consider creating a helper function that can be used for both cases.

### Extra challenges
If you would like to take your project a step further, consider these:

- User
    - Allow the user to input personal features, like a username
    - Allow the user to ask for hints if they are stuck
- Game
    - Have multiple rooms/areas that the user can move between
    - Have tasks that can only be done if the user has a certain combination of items (e.g. starting a fire requires a matchbox and a match)
- Ending
    - Have multiple endings, depending on the user's choices
    - Introduce ways the player can "lose" and have to start over

Here are some more ideas: https://www.davidepesce.com/2020/02/26/13-tips-for-writing-a-good-text-adventure-game/

## Example
**NOTE** This is just a sample. You may choose a different format.

```
Welcome to Escape the Room!
You find yourself in a locked room.
Type commands to try to escape. For example, try typing 'look around'.
(Type 'h' for help)
> h
Type 'h' for help
Type 'i' to check your inventory
Type 'look around' to look around
Type 'pick up [item]' to pick something up
Try other commands too!
> open door
You need a key to do that.
> look around
The room is empty except for a key on a table.
> i
Your inventory is empty
> pick up key
You pick up the key.
> i
Your inventory contains:
key
> walk left
I don't understand. (Type 'h' for help)
> open door
Door unlocked! Congratulations, you've escaped!
```
