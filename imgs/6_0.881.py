d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.NW, Length.long)
d.position_pen(3,2)
d.curve(Direction.NW, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.S, Length.medium)

d.end()
