d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,1)

d.end()
