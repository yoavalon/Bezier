d = DslBezier()

d.position_pen(1,0)
d.position_pen(3,2)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,2)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)

d.end()
