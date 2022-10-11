d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)

d.end()
