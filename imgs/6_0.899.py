d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)
d.position_pen(2,3)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.NE, Length.short)

d.end()
