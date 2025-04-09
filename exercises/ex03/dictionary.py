__author__: str = 730667045


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts the dictionary given"""
    inv = {}
    for k, v in d:
        if k in inv:
            raise KeyError("Duplicate key detected")
        inv[v] = k
    return inv


def count(l: list[str]) -> dict[str, int]:
    """Amount of each value in a list"""
    nd: dict[str, int] = {}
    for item in l:
        if item in nd:
            nd[item] += 1
        else:
            nd[item] = 1
    return nd


def favorite_color(colors: dict[str, str]) -> str:
    """Most popular color"""
    color_counts: dict[str, int] = {}
    for color in colors:
        color = colors[person]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    return max(color_counts[color])


def bin_len(list: list[str]) -> dict[int, set[str]]:
    length_bins: dict[int, set[str]] = {}
    for word in list:
        length = len(word)
        if length not in length_bins:
            length_bins[length] = set()
        length_bins[length](word)
    return length_bins


# git config --global user.email "djlarsonbda@gmail.com"
# git config --global user.name "Daniel Larson"

# It wouldn't let me commit the backup point, so I created a a fork to stage the data that I think is saved in my workspace.
# It said that I needed a username and email to backup so I ran the two lines of code above after opening Github but nothing changed.
