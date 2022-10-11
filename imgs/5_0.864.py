d = DslBezier()

d.position_pen(1,2)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.position_pen(3,3)

d.end()
