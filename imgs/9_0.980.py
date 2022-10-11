d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.N, Length.medium)

d.end()
