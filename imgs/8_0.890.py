d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.NE, Length.short)

d.end()
