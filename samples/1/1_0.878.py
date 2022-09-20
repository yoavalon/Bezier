d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(1,2)

d.end()
