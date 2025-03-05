# Discord Reminder Bot

This is a simple Discord bot that allows users to set reminders and create polls.

## Features

- Set reminders for specific dates and times.
- Set reminders for a custom amount of time (e.g., seconds, minutes, hours).
- Delete reminders.
- Modify reminders.
- Create polls with up to 10 options.

## Development Process

### Initial Setup

1. **Project Initialization**: Set up a new Python project with a virtual environment to manage dependencies.
2. **Install Required Libraries**: Install `discord.py` for interacting with Discord's API and `certifi` for SSL certificate verification.

### Adding Features

1. **Reminder Command**: Implement the `!setReminder` command to allow users to set reminders for specific dates and times.
2. **Custom Time Reminder**: Add the `!setReminderIn` command to support setting reminders for a custom amount of time (e.g., "10s", "5m", "2h").
3. **Delete Reminder Command**: Implement the `!deleteReminder` command to allow users to delete reminders by their index.
4. **Modify Reminder Command**: Add the `!modifyReminder` command to enable users to modify existing reminders.
5. **Poll Command**: Implement the `!createPoll` command to create polls with up to 10 options.

## Next Steps

Given more time, the following steps would be taken to further improve the bot:

1. **Enhance Reminder Functionality**:
    - Add support for recurring reminders (e.g., daily, weekly).
    - Allow users to specify time zones for reminders.

2. **Improve Poll Functionality**:
    - Add functionality to close polls and display results.
    - Support anonymous voting.

3. **Add Moderation Features**:
    - Implement moderation commands to manage users and content.
    - Allow moderators to delete inappropriate messages and mute users.

By following these steps, the bot can be made more robust, user-friendly, and feature-rich, enhancing the overall user experience.
