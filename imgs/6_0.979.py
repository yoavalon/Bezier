d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
