d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.position_pen(1,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.NW, Length.short)

d.end()
