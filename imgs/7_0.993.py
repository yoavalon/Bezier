d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,3)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)

d.end()
