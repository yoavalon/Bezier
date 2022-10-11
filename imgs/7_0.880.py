d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.SE, Length.long)
d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)

d.end()
