d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.long)

d.end()
