d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.S, Length.medium)

d.end()
