d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.W, Length.short)
d.position_pen(3,2)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.N, Orient.left, Length.short, Radius.high)

d.end()
