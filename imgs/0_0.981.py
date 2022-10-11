d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(3,1)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)

d.end()
