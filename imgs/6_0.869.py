d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,1)

d.end()
