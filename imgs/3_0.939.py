d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)

d.end()
