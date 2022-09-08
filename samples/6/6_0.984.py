d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(3,2)
d.straight_line(Direction.NW, Length.long)
d.position_pen(0,3)

d.end()
