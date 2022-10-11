d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.position_pen(1,3)
d.straight_line(Direction.S, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,3)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)

d.end()
