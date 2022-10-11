d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
