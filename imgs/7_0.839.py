d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,1)

d.end()
