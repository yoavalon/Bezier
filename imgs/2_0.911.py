d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SW, Length.long)
d.position_pen(3,2)

d.end()
