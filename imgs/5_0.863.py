d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SE, Length.long)
d.position_pen(3,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.position_pen(2,1)

d.end()
