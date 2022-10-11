d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.S, Length.long)

d.end()
