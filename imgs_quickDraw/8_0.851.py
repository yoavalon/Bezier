d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.curve(Direction.E, Orient.right, Length.short, Radius.low)
d.position_pen(0,1)

d.end()
