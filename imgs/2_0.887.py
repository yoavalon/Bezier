d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.NE, Length.long)
d.position_pen(2,2)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,2)

d.end()
