d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(2,1)

d.end()
