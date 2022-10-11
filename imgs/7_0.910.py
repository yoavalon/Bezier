d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.N, Length.short)
d.position_pen(0,1)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)

d.end()
