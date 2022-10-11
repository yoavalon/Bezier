d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.position_pen(0,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,1)

d.end()
