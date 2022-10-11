d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.N, Length.long)

d.end()
