d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.position_pen(1,0)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.E, Length.long)

d.end()
