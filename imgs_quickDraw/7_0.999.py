d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.position_pen(3,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SE, Length.medium)

d.end()
