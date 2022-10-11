d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,1)

d.end()
