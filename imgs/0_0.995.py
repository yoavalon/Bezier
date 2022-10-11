d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)

d.end()
