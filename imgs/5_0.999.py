d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,1)

d.end()
