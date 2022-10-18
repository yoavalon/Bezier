d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.N, Length.medium)

d.end()
