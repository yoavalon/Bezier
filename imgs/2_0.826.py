d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)

d.end()
