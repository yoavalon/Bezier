d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.position_pen(1,2)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,1)

d.end()
