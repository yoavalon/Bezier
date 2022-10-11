d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,3)
d.curve(Direction.NW, Orient.left, Length.long, Radius.low)

d.end()
