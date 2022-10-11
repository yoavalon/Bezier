d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)

d.end()
