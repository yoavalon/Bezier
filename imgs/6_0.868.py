d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(3,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)

d.end()
