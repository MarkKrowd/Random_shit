import cx_Freeze



executables = [cx_Freeze.Executable("MichSnake.pyw")]

cx_Freeze.setup(name="MichSnake",options={"build_exe":{"packages":["pygame"],"include_files":["Apple.png","Head.png","Apple2.png"]}},description = "Serpent quoi", executables = executables)

