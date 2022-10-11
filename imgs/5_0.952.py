d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.N, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.SE, Length.short)

d.end()
