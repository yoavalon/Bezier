d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)

d.end()
