d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.curve(Direction.N, Orient.right, Length.long, Radius.high)

d.end()
