d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.NW, Length.medium)

d.end()
