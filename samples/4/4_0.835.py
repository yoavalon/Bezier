d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.SW, Length.medium)

d.end()
