d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.SE, Length.long)
d.position_pen(2,3)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)

d.end()
