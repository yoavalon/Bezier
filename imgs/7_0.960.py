d = DslBezier()

d.position_pen(2,0)
d.position_pen(0,3)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.position_pen(3,0)

d.end()
