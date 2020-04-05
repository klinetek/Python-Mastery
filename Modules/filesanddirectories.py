import os
"""this program searches and displays things neatly to the console so you
wouldn't actually need that stuff in a real application.  This could be reused
in a sorting program or maybe even looking for recursive data in a file lookup
system.  or not, i do't really know what's goign on mostly haha"""
def list_directories(s):
    def dir_list(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + " does not exit")

list_directories('.')
