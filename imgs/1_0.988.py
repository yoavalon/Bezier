d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.curve(Direction.E, Orient.left, Length.short, Radius.low)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
