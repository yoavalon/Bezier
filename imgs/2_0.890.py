d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.W, Length.medium)

d.end()
