d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.position_pen(1,0)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)

d.end()
