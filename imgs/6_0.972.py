d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.position_pen(3,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(2,3)

d.end()
