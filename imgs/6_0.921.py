d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.position_pen(3,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)

d.end()
