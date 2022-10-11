d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.long)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.short)

d.end()
