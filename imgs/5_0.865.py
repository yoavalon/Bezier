d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,0)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.short)

d.end()
