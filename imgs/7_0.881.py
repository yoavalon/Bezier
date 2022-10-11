d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,2)
d.position_pen(2,1)

d.end()
