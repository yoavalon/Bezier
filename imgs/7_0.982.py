d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)

d.end()
