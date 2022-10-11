d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,0)
d.straight_line(Direction.E, Length.long)
d.position_pen(0,0)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(2,0)

d.end()
