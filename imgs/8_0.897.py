d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,2)

d.end()
