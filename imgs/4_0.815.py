d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)

d.end()
