d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
