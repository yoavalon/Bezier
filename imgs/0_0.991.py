d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)

d.end()
