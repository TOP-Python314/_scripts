def point(x: int, y: int, /):
    ...


# >>> point(1, 3)
# >>>
# >>> point(2, y=2)
# ...
# TypeError: point() got some positional-only arguments passed as keyword arguments: 'y'
# >>>
# >>> point(x=-1, y=5)
# ...
# TypeError: point() got some positional-only arguments passed as keyword arguments: 'x, y'
# >>>
# >>> point(y=1, x=3)
# ...
# TypeError: point() got some positional-only arguments passed as keyword arguments: 'x, y'


def process_track_info(
        *,
        title: str,
        artist: str,
        disk: str,
        year: int,
        channels: int,
        bit_depth: int,
        sample_rate: float
):
    ...


process_track_info(
    title='Boom-Boom',
    artist='Boomers',
    disk='BOOM!',
    year=2020,
    channels=6,
    bit_depth=8,
    sample_rate=44.1
)


