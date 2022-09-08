d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.position_pen(2,3)
d.position_pen(1,2)

d.end()
