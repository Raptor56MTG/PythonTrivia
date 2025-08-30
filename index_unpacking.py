def problem8():
    site = ["Javan", "Sam", "James", "Kutay"]
    idx = 2
    site[idx], idx = 'Julian', 3
    print(site)

def problem9():
    site = ["Javan", "Sam", "James", "Kutay"]
    idx = 2
    idx, site[idx], = 3, 'Julian'
    print(site)

if __name__ == '__main__':
    problem8()
    problem9()

def explanation():
    """
    This boils down to how variable assignment works during unpacking.
    They are evaluated from left to right.

    One thing to note is that this is bad practice and should never be done.
    This is more so a nice piece of trivia on how unpacking works.
    """