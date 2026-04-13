# Power Manager App

A simple Windows power manager app with 4 buttons:
- `Log out`
- `Shut down`
- `Restart`
- `Sleep`

## Files

- `main.py` - the main Python script that creates the UI and runs the power commands.

## Run

1. Install Python 3 on Windows if needed.
2. Open the folder in Visual Studio Code.
3. Run `main.py` from the terminal or Debug pane:
   ```bash
   python main.py
   ```

## Notes

- `Log out`, `Shut down`, and `Restart` use Windows `shutdown` commands.
- `Sleep` uses the Windows power API and may require administrator privileges on some machines.
