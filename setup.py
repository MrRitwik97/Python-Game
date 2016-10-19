import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="Dodger",
    version="1.0",
    description="Dodge The Blocks",
    options={"build_exe":{"packages":["pygame"],
                          "include_files":["racecar.png","carIcon.png","crash.wav","music.mp3"]}},

    executables = executables

    )
