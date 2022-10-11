d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,2)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)

d.end()
