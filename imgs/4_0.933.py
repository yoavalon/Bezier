d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.position_pen(2,3)
d.straight_line(Direction.E, Length.medium)

d.end()
