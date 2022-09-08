d = DslBezier()

d.position_pen(2,0)
d.position_pen(3,0)
d.position_pen(1,2)
d.position_pen(0,0)
d.position_pen(2,2)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
