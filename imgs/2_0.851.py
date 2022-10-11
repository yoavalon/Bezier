d = DslBezier()

d.position_pen(2,2)
d.position_pen(2,3)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
