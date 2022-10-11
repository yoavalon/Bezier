d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.N, Length.medium)
d.position_pen(2,3)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.long)

d.end()
