d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.position_pen(2,1)
d.position_pen(1,2)
d.position_pen(2,3)

d.end()
