d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.N, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.medium)

d.end()
