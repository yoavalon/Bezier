d = DslBezier()

d.position_pen(0,0)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,2)

d.end()
