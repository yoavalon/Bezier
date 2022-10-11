d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,0)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,2)

d.end()
