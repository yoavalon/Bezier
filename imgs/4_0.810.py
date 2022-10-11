d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.NW, Length.long)

d.end()
