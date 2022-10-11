d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.position_pen(2,0)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)

d.end()
