d = DslBezier()

d.position_pen(1,0)
d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,1)
d.position_pen(2,0)

d.end()
