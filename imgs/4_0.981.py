d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.S, Length.long)

d.end()
