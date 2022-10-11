d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)
d.position_pen(1,1)

d.end()
