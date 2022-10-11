d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.position_pen(1,2)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.position_pen(1,2)

d.end()
