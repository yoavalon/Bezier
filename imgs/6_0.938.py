d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.long)

d.end()
