d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)

d.end()
