d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.S, Length.short)
d.position_pen(0,0)
d.straight_line(Direction.SW, Length.medium)

d.end()
