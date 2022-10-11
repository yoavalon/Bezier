d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,0)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)

d.end()
