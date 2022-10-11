d = DslBezier()

d.position_pen(0,3)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(3,0)

d.end()
