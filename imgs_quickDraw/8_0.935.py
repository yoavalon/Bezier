d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.E, Length.short)
d.position_pen(0,1)

d.end()
