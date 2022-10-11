d = DslBezier()

d.position_pen(3,2)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,3)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)

d.end()
